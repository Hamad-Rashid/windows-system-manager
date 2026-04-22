# Windows V1 Scope

## In Scope
- Provider-driven architecture split between UI and OS backends.
- Platform provider selection (`Windows` default on Windows, `Linux` fallback elsewhere).
- Read-only system metrics for Windows (RAM and storage).
- Read-only dashboard shell for packages, devices, and storage using shared typed models.
- Safety-first action contracts for package and partition mutations (defined but not enabled yet).

## Out of Scope (V1 Freeze)
- Real package mutation execution (`winget upgrade/uninstall`) in this milestone.
- Real package inventory parsing from `winget` output.
- Real Bluetooth/USB device discovery integration via PowerShell.
- Real Windows disk/volume enumeration and partition action execution.
- UAC elevation workflow and privileged operation retry logic.
- Installer/signing pipeline and CI release automation.

## V1 Contract
1. App boots with a platform-selected provider and keeps core section layout.
2. Metrics tab shows real values from provider.
3. Other read tabs render predictable provider output and explicit pending-state messages.
4. Mutation APIs exist as typed interfaces with non-destructive placeholders.
5. Architecture supports replacing placeholders with Windows-native implementations without changing UI contracts.

## Exit Criteria for This Scope
- Provider abstraction committed and used by UI.
- Phase 1 planning artifacts present and actionable.
- Checklist updated to reflect completed and pending work accurately.
