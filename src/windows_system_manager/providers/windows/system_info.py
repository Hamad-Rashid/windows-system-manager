from __future__ import annotations

import psutil

from windows_system_manager.models import SystemMetrics
from windows_system_manager.providers.base import SystemInfoProvider


def _bytes_to_gib_text(value: int) -> str:
    gib = value / (1024**3)
    return f"{gib:.1f} GiB"


class WindowsSystemInfoProvider(SystemInfoProvider):
    def get_metrics(self) -> SystemMetrics:
        vm = psutil.virtual_memory()
        disk = psutil.disk_usage("C:\\")
        return SystemMetrics(
            total_ram=_bytes_to_gib_text(vm.total),
            used_ram=_bytes_to_gib_text(vm.used),
            total_storage=_bytes_to_gib_text(disk.total),
            used_storage=_bytes_to_gib_text(disk.used),
        )
