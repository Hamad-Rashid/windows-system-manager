# Windows Migration Checklist

Use this as the execution tracker for the Windows app project.

## Phase 1: Scope and Matrix
- [ ] Inventory current Linux feature set and map source files.
- [ ] Build `Keep / Adapt / Drop` matrix.
- [ ] Approve Windows replacements for each adapted feature.
- [ ] Define V1 out-of-scope list.
- [ ] Freeze V1 feature contract.

## Phase 2: Architecture Refactor
- [ ] Create provider interfaces for all service domains.
- [ ] Extract Linux implementation into provider modules.
- [ ] Add Windows provider skeleton classes.
- [ ] Add provider selection logic by platform.
- [ ] Confirm Linux app behavior remains unchanged after refactor.

## Phase 3: Windows Read-Only Services
- [ ] Implement Windows system metrics provider.
- [ ] Implement Windows package read model (`winget` list/update visibility).
- [ ] Implement Windows Bluetooth/USB read model.
- [ ] Implement Windows partition read model.
- [ ] Normalize outputs into shared models.
- [ ] Add tests for command parsing and edge cases.
- [ ] Validate dashboard refresh stability for 30+ cycles.

## Phase 4: Windows Mutating Actions
- [ ] Implement package update-all action.
- [ ] Implement package single-update action.
- [ ] Implement package remove action.
- [ ] Define and implement Windows-safe cache cleanup action.
- [ ] Implement partition mount/unmount actions where supported.
- [ ] Implement partition repair flow (`chkdsk`-based).
- [ ] Add admin privilege preflight and UAC guidance.
- [ ] Add retry/timeout handling and action logs.

## Phase 5: UI Port
- [ ] Create Windows UI project structure (PySide6).
- [ ] Port metrics view and refresh state widgets.
- [ ] Port package management view and action buttons.
- [ ] Port Bluetooth/USB view.
- [ ] Port partitions/fix workflows.
- [ ] Port operation logs and status bar behavior.
- [ ] Validate keyboard and resize behavior on desktop/laptop resolutions.

## Phase 6: Packaging and Installer
- [ ] Add PyInstaller spec and reproducible build script.
- [ ] Build `.exe` artifact in CI or local build pipeline.
- [ ] Create installer and uninstaller.
- [ ] Add startup diagnostics for missing dependencies (e.g. `winget`).
- [ ] Add release notes template and installation guide.

## Phase 7: QA and Release
- [ ] Test on Windows 10 and Windows 11.
- [ ] Test under standard user account.
- [ ] Test under administrator account.
- [ ] Run end-to-end test cases for all primary workflows.
- [ ] Validate failure messaging for denied elevation and command failures.
- [ ] Document known limitations.
- [ ] Produce release candidate and sign-off checklist.

## Acceptance Gates
- [ ] Gate A: V1 scope approved.
- [ ] Gate B: Windows read-only parity approved.
- [ ] Gate C: Privileged action safety approved.
- [ ] Gate D: Packaging/install flow approved.
- [ ] Gate E: Release candidate approved.

## Risks to Track
- [ ] `winget` behavior variance by Windows build.
- [ ] Elevated command reliability and UAC UX friction.
- [ ] Storage repair safety and user guidance quality.
- [ ] Driver/device query inconsistencies for Bluetooth/USB.
- [ ] UI parity regressions during framework switch.
