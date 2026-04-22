from __future__ import annotations

from windows_system_manager.models import BluetoothDeviceEntry
from windows_system_manager.providers.base import BluetoothServiceProvider


class WindowsBluetoothServiceProvider(BluetoothServiceProvider):
    def list_devices(self) -> list[BluetoothDeviceEntry]:
        return []
