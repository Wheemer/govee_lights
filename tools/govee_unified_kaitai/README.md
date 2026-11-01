# Govee Unified Kaitai sources

This directory vendors the Kaitai schemas used to generate
`custom_components/govee_unified/generated_protocol`. They were imported from
Teh-Hippo's `ha-govee-led-ble` under its MIT licence; see
`LICENSE.teh-hippo-MIT` at repository root.

Regenerate the runtime package with Kaitai Struct Compiler 0.11:

```bash
KAITAI_STRUCT_COMPILER=/path/to/kaitai-struct-compiler \
  bash scripts/generate-govee-unified-kaitai.sh runtime
```

The checked-in runtime output is intentional. Home Assistant installs the
`kaitaistruct` Python runtime, not the Kaitai compiler, so users must not need
generator tooling on their Home Assistant host.
