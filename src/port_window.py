import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, \
    QComboBox, QTableWidget, QTableWidgetItem, QHeaderView, QSizePolicy, QFormLayout, QListWidget
from PyQt6.QtCore import Qt
from ip_scanner import IPScanner
from network_topology import *


class PortOptionsWidget(QWidget):
    def __init__(self, network):
        super().__init__()
        self.network = network
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.ip_scanner = IPScanner()
        self.load_port_layout()

    def load_port_layout(self):
        # Create layout for Scan Ports
        scan_ports_layout = QVBoxLayout()

        target_layout = QHBoxLayout()
        target_input = QLineEdit()

        # Dropdown Box
        service_combo = QComboBox()
        service_combo.addItems(self.network.machines.keys())
#        self.service_combo.currentIndexChanged.connect(self.update_result_table)
        service_combo.showEvent = lambda event: self.update_service_combo(service_combo)
        scan_ports_layout.addWidget(service_combo)

        target_input.setPlaceholderText("Target Machine")
        scan_host_button = QPushButton("Scan Host")
        target_layout.addWidget(target_input)
        target_layout.addWidget(scan_host_button)
        scan_ports_layout.addLayout(target_layout)
        #scan_ports_layout.addWidget(service_combo)

        # Results Table
        result_table = QTableWidget()
        result_table.setRowCount(4)
        result_table.setColumnCount(3)
        result_table.setHorizontalHeaderLabels(["Service", "Version", "Port"])
        result_table.setItem(0, 0, QTableWidgetItem("SSH"))
        result_table.setItem(0, 1, QTableWidgetItem("2.0"))
        result_table.setItem(0, 2, QTableWidgetItem("22"))
        result_table.setItem(1, 0, QTableWidgetItem("HTTP"))
        result_table.setItem(1, 1, QTableWidgetItem("3.3"))
        result_table.setItem(1, 2, QTableWidgetItem("80"))
        result_table.setItem(2, 0, QTableWidgetItem("FTP"))
        result_table.setItem(2, 1, QTableWidgetItem("1.9"))
        result_table.setItem(2, 2, QTableWidgetItem("21"))
        result_table.setItem(3, 0, QTableWidgetItem("DNS"))
        result_table.setItem(3, 1, QTableWidgetItem("123"))
        result_table.setItem(3, 2, QTableWidgetItem("5300"))

        result_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        scan_ports_layout.addWidget(result_table)

        self.layout.addLayout(scan_ports_layout)

    def update_service_combo(self, combo_box):
        combo_box.clear()
        combo_box.addItems(self.network.machines.keys())
