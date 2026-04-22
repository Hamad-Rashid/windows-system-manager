from __future__ import annotations

from typing import Sequence

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Windows System Manager")
        self.resize(1200, 800)

        tabs = QTabWidget()
        tabs.addTab(self._placeholder_tab("System Metrics"), "Metrics")
        tabs.addTab(self._placeholder_tab("Packages (winget)"), "Packages")
        tabs.addTab(self._placeholder_tab("Bluetooth and USB"), "Devices")
        tabs.addTab(self._placeholder_tab("Partitions and Volumes"), "Storage")
        tabs.addTab(self._placeholder_tab("Operation logs"), "Logs")
        self.setCentralWidget(tabs)

    def _placeholder_tab(self, title: str) -> QWidget:
        page = QWidget()
        layout = QVBoxLayout(page)
        label = QLabel(f"{title}\n\nImplementation will be added in migration phases.")
        label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        label.setWordWrap(True)
        layout.addWidget(label)
        return page


def run_app(argv: Sequence[str]) -> int:
    app = QApplication(list(argv))
    win = MainWindow()
    win.show()
    return int(app.exec())
