# Windows System Manager

Windows-native desktop system utility project, maintained as a separate repository from the Ubuntu/Linux app.

## Project Goal
Build a Windows application with practical system-management workflows:
- System metrics (RAM, storage)
- Package/app management (Winget-based)
- Bluetooth and USB device visibility
- Partition/volume status and repair actions
- Action logs and operational feedback

## Tech Stack
- Python 3.11+
- PySide6 (desktop UI)
- `psutil` (system metrics)
- PowerShell / Windows-native tools for device, package, and storage operations

## Repository Scope
This repository contains only the Windows project.
Linux/Ubuntu code is intentionally excluded and maintained separately.

## Current Status
- Base project scaffold is ready.
- Migration execution is tracked in `docs/`.

## Directory Structure
- `src/windows_system_manager/`: application source
- `docs/`: migration plan and implementation checklist
- `scripts/`: build and automation scripts (to be added)

## Local Development
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
python -m windows_system_manager.main
```

## Testing (Linux Dev Host)
```bash
source .venv/bin/activate
pip install -e ".[dev]"
pytest -q
```

If you only want backend/provider tests on a headless Linux machine:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pytest psutil
pip install -e . --no-deps
pytest -q
```

Provider override checks:
```bash
WSM_PROVIDER=linux pytest -q
WSM_PROVIDER=windows pytest -q tests/test_provider_resolution.py
```

## Roadmap Documents
- `docs/windows-migration-plan.md`
- `docs/windows-migration-checklist.md`

## Initial Milestones
1. Finalize Windows feature matrix (Keep/Adapt/Drop).
2. Implement read-only Windows backend services.
3. Add privileged action flows with safe elevation handling.
4. Package as distributable Windows `.exe`.

## Contribution Flow
1. Create feature branch from `main`.
2. Implement focused changes with tests where relevant.
3. Open PR with clear change summary and risk notes.
