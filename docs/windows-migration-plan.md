# Windows Migration Plan

## Goal
Build a Windows-native desktop version of Ubuntu System Manager with equivalent user value, using Windows-compatible subsystems and tools.

## Guiding Rules
- Keep the same core product sections: System Metrics, Packages, Bluetooth/USB, Partitions, Logs.
- Replace Linux-only implementations with Windows-native backends.
- Ship in small phases with testable milestones.
- Treat privileged operations as high-risk and gate with explicit elevation checks.

## Target Platform
- Primary: Windows 11 (latest stable updates)
- Secondary: Windows 10 (latest stable updates)
- Python runtime: 3.11+
- UI stack recommendation: PySide6
- Packaging recommendation: PyInstaller + Inno Setup (or MSIX)

## Phase 1: Scope and Feature Matrix
### Objective
Convert current Linux functionality into approved Windows behavior.

### Work
- Inventory Linux features and commands currently used.
- Decide per feature: `Keep`, `Adapt`, or `Drop`.
- Define Windows replacement command/API for each adapted feature.
- Define explicit "out of scope" items for first Windows release.

### Deliverables
- `docs/windows-feature-matrix.md`
- `docs/windows-v1-scope.md`

### Exit Criteria
- Feature matrix signed off.
- No unowned feature remains.

## Phase 2: Architecture Split (Backend Providers)
### Objective
Separate UI from OS-specific logic to support clean Windows implementation.

### Work
- Introduce provider interfaces for:
  - `system_info`
  - `package_service`
  - `package_actions`
  - `bluetooth_service`
  - `partition_service`
  - `partition_actions`
- Keep Linux provider as reference implementation.
- Add Windows provider skeleton with stubs and typed contracts.

### Deliverables
- `src/ubuntu_system_manager/providers/` abstraction layer
- `src/ubuntu_system_manager/providers/windows/` skeleton

### Exit Criteria
- App can boot with provider selected by platform flag.
- Existing Linux behavior remains unchanged.

## Phase 3: Windows Read-Only Backend
### Objective
Get full dashboard visibility on Windows before mutating actions.

### Work
- System metrics:
  - RAM and storage via `psutil` and/or PowerShell/WMI.
- Packages overview:
  - Installed apps and available upgrades via `winget`.
- Bluetooth/USB visibility:
  - PowerShell CIM / PnP device queries.
- Partitions overview:
  - `Get-Disk`, `Get-Partition`, `Get-Volume`.
- Normalize Windows data into existing model structures.

### Deliverables
- Functional Windows read-only services
- Unit tests with command-output fixtures

### Exit Criteria
- All dashboard tabs show meaningful Windows data.
- Refresh loop stable under repeated use.

## Phase 4: Windows Action Services (Privileged)
### Objective
Enable controlled update/remove/repair operations on Windows.

### Work
- Package actions:
  - Update all / single app via `winget upgrade`
  - Remove app via `winget uninstall`
- Cache cleanup:
  - Replace Linux cache strategy with Windows-safe equivalent.
- Partition actions:
  - Mount/unmount where supported
  - Repair path using `chkdsk` flow
- Add admin-elevation preflight checks and actionable errors.

### Deliverables
- Windows mutation services with operation logs
- Failure taxonomy and user-safe error messages

### Exit Criteria
- All enabled actions run with predictable result states.
- Non-admin execution shows clear remediation.

## Phase 5: UI Port and Parity
### Objective
Deliver a Windows-native UI while preserving core workflows.

### Work
- Rebuild GTK UI in PySide6.
- Preserve section layout and major controls.
- Keep operation logs, refresh status, and activity indicators.
- Add platform-specific labels where behavior differs.

### Deliverables
- Windows UI app runnable from source
- UX parity checklist for feature pages

### Exit Criteria
- Daily workflows complete without Linux dependencies.
- UI responsive on common laptop resolutions.

## Phase 6: Packaging and Installer
### Objective
Produce distributable Windows installer artifacts.

### Work
- Build single-folder or single-file `.exe` with PyInstaller.
- Create installer/uninstaller (Inno Setup or MSIX).
- Add startup diagnostics:
  - `winget` availability
  - Admin requirement hints for privileged actions

### Deliverables
- Signed (or sign-ready) installer package
- Installation and upgrade docs

### Exit Criteria
- Clean install, launch, upgrade, and uninstall paths validated.

## Phase 7: QA and Release Readiness
### Objective
Harden stability and ship first Windows release candidate.

### Work
- Regression testing by feature section.
- Permission mode testing (standard user vs admin).
- Timeout/retry and error handling validation.
- Performance checks on refresh/action operations.

### Deliverables
- QA report
- Known limitations document
- `v1.0-windows-rc` release artifact

### Exit Criteria
- Blocking defects closed.
- Release checklist complete.

## Phase 8: Post-Release Enhancements
### Candidate Work
- Optional support for Chocolatey/Scoop.
- Richer storage repair workflows.
- Better telemetry/log export for troubleshooting.
- Background refresh and startup performance tuning.

## Milestones
1. M1: Scope approved (Phase 1 complete).
2. M2: Read-only Windows backend complete (Phase 3 complete).
3. M3: Privileged actions complete (Phase 4 complete).
4. M4: UI + packaging complete (Phases 5-6 complete).
5. M5: QA passed and first Windows release candidate published (Phase 7 complete).
