from __future__ import annotations

import os
import sys

from windows_system_manager.providers.base import ProviderBundle
from windows_system_manager.providers.linux.devices import LinuxBluetoothServiceProvider
from windows_system_manager.providers.linux.packages import (
    LinuxPackageActionsProvider,
    LinuxPackageServiceProvider,
)
from windows_system_manager.providers.linux.partitions import (
    LinuxPartitionActionsProvider,
    LinuxPartitionServiceProvider,
)
from windows_system_manager.providers.linux.system_info import LinuxSystemInfoProvider
from windows_system_manager.providers.windows.devices import WindowsBluetoothServiceProvider
from windows_system_manager.providers.windows.packages import (
    WindowsPackageActionsProvider,
    WindowsPackageServiceProvider,
)
from windows_system_manager.providers.windows.partitions import (
    WindowsPartitionActionsProvider,
    WindowsPartitionServiceProvider,
)
from windows_system_manager.providers.windows.system_info import WindowsSystemInfoProvider


def _linux_bundle() -> ProviderBundle:
    return ProviderBundle(
        system_info=LinuxSystemInfoProvider(),
        package_service=LinuxPackageServiceProvider(),
        package_actions=LinuxPackageActionsProvider(),
        bluetooth_service=LinuxBluetoothServiceProvider(),
        partition_service=LinuxPartitionServiceProvider(),
        partition_actions=LinuxPartitionActionsProvider(),
    )


def _windows_bundle() -> ProviderBundle:
    return ProviderBundle(
        system_info=WindowsSystemInfoProvider(),
        package_service=WindowsPackageServiceProvider(),
        package_actions=WindowsPackageActionsProvider(),
        bluetooth_service=WindowsBluetoothServiceProvider(),
        partition_service=WindowsPartitionServiceProvider(),
        partition_actions=WindowsPartitionActionsProvider(),
    )


def resolve_provider_bundle() -> ProviderBundle:
    forced = os.getenv("WSM_PROVIDER", "").strip().lower()
    if forced == "linux":
        return _linux_bundle()
    if forced == "windows":
        return _windows_bundle()

    if sys.platform.startswith("win"):
        return _windows_bundle()
    return _linux_bundle()
