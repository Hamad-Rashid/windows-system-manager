from __future__ import annotations

from windows_system_manager.models import PackageEntry
from windows_system_manager.providers.base import (
    ActionResult,
    PackageActionsProvider,
    PackageServiceProvider,
)


class LinuxPackageServiceProvider(PackageServiceProvider):
    def list_packages(self) -> list[PackageEntry]:
        return []


class LinuxPackageActionsProvider(PackageActionsProvider):
    def update_all(self) -> ActionResult:
        return ActionResult(False, "Linux package actions are not implemented in this repository.")

    def update_package(self, package_name: str) -> ActionResult:
        return ActionResult(False, f"Linux package action is not implemented for '{package_name}'.")

    def remove_package(self, package_name: str) -> ActionResult:
        return ActionResult(False, f"Linux package action is not implemented for '{package_name}'.")
