# Windows Feature Matrix

This matrix maps current repository features to Windows V1 decisions.

## Legend
- `Keep`: keep behavior as-is.
- `Adapt`: preserve user outcome with Windows-native backend.
- `Drop`: not in V1.

## Feature Inventory
| Area | Current State in Repo | Source Files | V1 Decision | Windows Replacement | Notes |
|---|---|---|---|---|---|
| Application entry point | Boots desktop app via `run_app()` | `src/windows_system_manager/main.py` | Keep | Keep Python entry point (`python -m windows_system_manager.main`) | No platform coupling here |
| Desktop UI shell with 5 tabs | PySide6 tab shell exists, now provider-backed read views | `src/windows_system_manager/ui.py` | Keep | Keep PySide6 | Preserve sections: Metrics, Packages, Devices, Storage, Logs |
| System metrics model | Typed `SystemMetrics` dataclass | `src/windows_system_manager/models.py` | Keep | Keep model contract | Backend provider-specific |
| Package model | Typed `PackageEntry` dataclass | `src/windows_system_manager/models.py` | Adapt | `winget` read/action services | Read path pending real parser |
| Bluetooth device model | Typed `BluetoothDeviceEntry` dataclass | `src/windows_system_manager/models.py` | Adapt | PowerShell CIM / PnP query | Currently provider skeleton only |
| Partition model | Typed `PartitionEntry` dataclass | `src/windows_system_manager/models.py` | Adapt | `Get-Disk`, `Get-Partition`, `Get-Volume` | Linux reference provider added |
| System metrics backend | New provider architecture with Linux+Windows implementations | `src/windows_system_manager/providers/base.py`, `src/windows_system_manager/providers/windows/system_info.py`, `src/windows_system_manager/providers/linux/system_info.py` | Adapt | Windows: `psutil` (`C:\` disk usage) | Implemented for read-only metrics |
| Provider architecture | New interfaces + bundle + resolver | `src/windows_system_manager/providers/base.py`, `src/windows_system_manager/providers/factory.py` | Keep | Platform-selected provider bundle (`sys.platform` / `WSM_PROVIDER`) | Completed Phase 2 baseline |
| Package actions (update/remove) | Contracts and placeholders only | `src/windows_system_manager/providers/*/packages.py` | Adapt | `winget upgrade` / `winget uninstall` | Phase 4 work |
| Partition actions (mount/unmount/repair) | Contracts and placeholders only | `src/windows_system_manager/providers/*/partitions.py` | Adapt | Windows mount + `chkdsk` | Phase 4 work |
| Logs tab | Placeholder text | `src/windows_system_manager/ui.py` | Keep | Structured operation log feed | Pending Phase 5/4 integration |

## Out-of-Repo Linux Dependencies
The Linux/Ubuntu legacy app is not part of this repository. Linux behavior is represented via reference providers only to maintain architecture parity during development.
