from __future__ import annotations

from windows_system_manager.providers.linux.devices import LinuxBluetoothServiceProvider
from windows_system_manager.providers.linux.packages import LinuxPackageServiceProvider
from windows_system_manager.providers.linux.partitions import LinuxPartitionServiceProvider


def test_linux_package_service_returns_list():
    entries = LinuxPackageServiceProvider().list_packages()
    assert isinstance(entries, list)


def test_linux_device_service_returns_list():
    entries = LinuxBluetoothServiceProvider().list_devices()
    assert isinstance(entries, list)


def test_linux_partition_service_returns_typed_rows():
    entries = LinuxPartitionServiceProvider().list_partitions()
    assert isinstance(entries, list)

    for row in entries:
        assert row.device
        assert row.filesystem is not None
        assert row.mountpoint is not None
        assert row.status
