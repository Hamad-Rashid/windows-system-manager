from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class SystemMetrics:
    total_ram: str
    used_ram: str
    total_storage: str
    used_storage: str


@dataclass(slots=True)
class PackageEntry:
    name: str
    source: str
    installed_version: str
    latest_version: str
    status: str
    update_available: bool
    can_toggle: bool
    enabled: bool


@dataclass(slots=True)
class BluetoothDeviceEntry:
    name: str
    address: str
    connected: bool


@dataclass(slots=True)
class PartitionEntry:
    device: str
    filesystem: str
    mountpoint: str
    expected_mountpoint: str
    size: str
    status: str
    status_detail: str
    can_mount: bool
    can_fix: bool
