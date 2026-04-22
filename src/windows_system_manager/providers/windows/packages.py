from __future__ import annotations

from windows_system_manager.models import PackageEntry
from windows_system_manager.providers.base import (
    ActionResult,
    PackageActionsProvider,
    PackageServiceProvider,
)


class WindowsPackageServiceProvider(PackageServiceProvider):
    def list_packages(self) -> list[PackageEntry]:
        return []


class WindowsPackageActionsProvider(PackageActionsProvider):
    def update_all(self) -> ActionResult:
        return ActionResult(False, "Not implemented yet for Windows package actions.")

    def update_package(self, package_name: str) -> ActionResult:
        return ActionResult(False, f"Not implemented yet for package '{package_name}'.")

    def remove_package(self, package_name: str) -> ActionResult:
        return ActionResult(False, f"Not implemented yet for package '{package_name}'.")
