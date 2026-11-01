# Upstream Porting Plan

This fork is a local-first Home Assistant integration.  New device support is
added only when its transport and packet semantics are independently evidenced;
a matching SKU name is not proof that it accepts this integration's commands.

## Sources accepted for implementation work

| Source | License | Use here | Do not infer |
| --- | --- | --- | --- |
| `teh-hippo/ha-govee-led-ble` | MIT | BLE discovery, per-model profiles, packet tests, ESPHome proxy lifecycle | That a profile's full effect grammar applies to a different SKU family |
| `homebridge-plugins/homebridge-govee` | MIT | Account/AWS routing, encrypted BLE flow, appliance entities and H7172 ice-maker semantics | Local appliance control where its code is using cloud or AWS IoT |
| `wez/govee2mqtt` | MIT | API/MQTT appliance quirks, fixtures and capability interpretation | BLE control; this project deliberately has no BLE controller |
| `Galorhallen/govee-local-api` | Apache-2.0 | LAN discovery, LAN capability data, scenes and segments; it is already a dependency | LAN support for non-LAN appliance products |
| `Beshelmek/govee_ble_lights` | MIT | Scene-library schema and broad SKU catalogue | A unique BLE protocol for each bundled scene JSON file |
| `Bluetooth-Devices/govee-ble` | MIT | Passive BLE advertisements for sensors | Connected BLE control |

Retain each source's required license and attribution notices when code is
adapted.  Reimplement protocol behavior with this integration's own tests;
do not copy undocumented packet code without a frame-level test and a declared
device family.

The server-held APK evidence and the distinction between an app asset and an
observed serializer are tracked in [BLE_EVIDENCE.md](BLE_EVIDENCE.md).

## Transport boundary

`govee_lights` currently owns direct BLE and Govee LAN lighting.  The following
are deliberately separate transports, even when one physical product exposes
more than one of them:

1. direct BLE (including ESPHome Bluetooth proxies);
2. LAN UDP for devices whose LAN control is enabled in Govee Home;
3. Govee account/OpenAPI and AWS IoT MQTT for cloud-connected appliances;
4. passive BLE advertisements for sensor telemetry.

An appliance is not marked local merely because it appears in the Govee app or
has a Bluetooth radio.  H7172 is an example: its known Home Assistant control
paths are cloud/MQTT semantics, not evidence of a local LAN controller.

## Implementation order

1. Add a tested model-profile layer to make command grammar, write policy,
   read-back confidence, and support quality explicit.
2. Port selected MIT BLE profiles from `ha-govee-led-ble` with packet fixtures,
   beginning with models whose base command grammar is independently verified.
3. Refresh the LAN capability dependency and add regression tests around its
   discovered capabilities rather than duplicate its model list.
4. Add a separate appliance transport adapter only after its Home Assistant
   entity model and credential boundary are designed; do not turn a light
   component into a cloud appliance controller by ad-hoc SKU cases.
5. Add H7172 and other appliance families from documented API/MQTT fixtures,
   then pursue local control only where the APK or wire capture proves it.

## Current selective ports

- **H617F:** Teh-Hippo's explicit H617F profile is a direct H617A
  command/status grammar sibling. This project therefore routes H617F through
  its existing H617A-compatible segmented and percentage-brightness handling,
  but labels it `experimental` pending an independent packet capture or
  physical-device validation. This is not an assertion that the advanced
  effects, segment readback, or every H617A feature has been ported.
- **H6076:** The Lyra's command grammar is H617A-compatible, but its status
  grammar is not. The experimental profile has only the independently
  described seven-segment and percentage-brightness write behavior; it does
  not claim Lyra status parsing, music, scenes, or advanced effects.
- **H1A42 and H61F5:** These H617A command siblings receive only their known
  five- and ten-segment write geometry, respectively. Their distinct status,
  music, scene, and colour-temperature behavior remains unported and is not
  represented as supported.

## Acceptance rule for a new family

A new model or family must have all of the following before it is described as
supported:

- a declared transport and capability profile;
- packet or API fixtures that cover every exposed writable feature;
- a focused test for serialization and state read-back;
- a real-device verification or an explicit experimental label;
- release notes stating whether support is BLE-local, LAN-local, or cloud.
