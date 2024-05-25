import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, \
    QComboBox, QTableWidget, QTableWidgetItem, QHeaderView, QSizePolicy, QFormLayout, QListWidget
from PyQt6.QtCore import Qt
from ip_scanner import IPScanner
from network_topology import *


class ScanOptionsWidget(QWidget):
    def __init__(self, network):
        super().__init__()
        self.network = network
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.ip_scanner = IPScanner()
        self.load_scan_network_layout()

    def load_scan_network_layout(self):
        # Create layout for Scan Network
        scan_network_layout = QVBoxLayout()

        form_layout = QFormLayout()

        ip_label = QLabel("Enter IP Address:    ")
        ip_input = QLineEdit()
        ip_input.setPlaceholderText("Enter IP Address")
        ip_input.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        subnet_label = QLabel("Enter Subnet Mask:")
        subnet_input = QLineEdit()
        subnet_input.setPlaceholderText("Enter Subnet Mask")
        subnet_input.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        scan_network_button = QPushButton("Scan Network")
        scan_network_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        ip_layout = QHBoxLayout()
        ip_layout.addWidget(ip_label)
        ip_layout.addWidget(ip_input)

        subnet_layout = QHBoxLayout()
        subnet_layout.addWidget(subnet_label)
        subnet_layout.addWidget(subnet_input)

        form_layout.addRow(ip_layout)
        form_layout.addRow(subnet_layout)
        form_layout.addRow(scan_network_button)

        scan_network_layout.addLayout(form_layout)

        scan_network_button.clicked.connect(lambda: self.on_scan_network_button_clicked(ip_input, subnet_input))

        # Setup result table
        self.result_table = QTableWidget()
        self.result_table.setRowCount(0)
        self.result_table.setColumnCount(1)
        self.result_table.setHorizontalHeaderLabels(["IP Address"])
        self.result_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        scan_network_layout.addWidget(self.result_table)

        self.layout.addLayout(scan_network_layout)

    def on_scan_network_button_clicked(self, ip_input, subnet_input):
        ip = ip_input.text()
        subnet = subnet_input.text()
        self.scan_network(ip, subnet)

    def scan_network(self, ip, subnet):
        # Call the ip_scanner's scan function
        results = self.ip_scanner.scan_subnet(ip, subnet)

        # Example: simulate scan results and update the result table

        # Update the result table with scan results
        self.result_table.setRowCount(len(results))
        for row, ip_address in enumerate(results):
            self.result_table.setItem(row, 0, QTableWidgetItem(ip_address))
            self.network.add_machine(ip_address)
