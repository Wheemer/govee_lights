# BLE Evidence Ledger

This ledger distinguishes a packet format observed in Govee Home from a model
name merely present in an app asset or another integration. It is deliberately
not a support list: a model is only promoted after the stated evidence and a
local regression test both exist.

## APK artifacts

The durable, non-repository artifacts are kept on the development server under
`/root/codex-work/govee-apk-evidence/`:

| Artifact | SHA-256 | Use |
| --- | --- | --- |
| Govee Home 7.5.30 | `dc296c49ba6c3837fd09eae22d7045bcae4d99563fbbac9065b4a8de051e582e` | Decompiled legacy BLE serializers and controllers |
| Govee Home 7.7.10 base | `073005281c8c6f6a8cf37dc464bb1e80e7021e0faff7b028148f93d72609bc69` | Current SKU/local-component asset cross-check |

## Packet-family evidence

| Family/model | Evidence | Implementation status |
| --- | --- | --- |
| H613E | 7.5.30 `com.govee.h613839.ble.SubModeColor4Bk`: emits mode `0x0D`, RGB, big-endian Kelvin, then rendered white RGB. The H613E hardware also physically confirmed RGB and white control. | **Verified**. Exact RGB and 5000 K frames are regression tested. |
| H617A legacy family | Upstream packet fixtures provide the shared `33 05 15` segmented static frame. The current APK separately lists H617A/C/E/F in `localSkuComponentConfigs.json`, which proves app-local SKU configuration but not a universal wire equivalence. | Existing H617A behavior retained; every additional sibling remains **experimental**. |
| H6076, H1A42, H61F5 | Upstream profile evidence supplies command grammar, geometry, and response group size; current APK assets list the SKUs as local components. | **Experimental** basic local BLE writes/readback only. No claim for scenes, music, custom effects, or complete status parsing. |

## Rules for the next BLE change

1. Locate the SKU-specific controller/serializer in the APK first. If the app
   uses an encrypted or revision-gated path, do not reuse a legacy frame.
2. Add an exact packet fixture and, where state is exposed, a response fixture.
3. Record whether confirmation is APK-only, hardware-verified, or both.
4. Do not treat a `localSkuComponentConfigs.json` entry as evidence that a SKU
   accepts another SKU's BLE packet grammar.
