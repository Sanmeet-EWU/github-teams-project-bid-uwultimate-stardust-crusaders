import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, \
    QLineEdit, QComboBox, QTableWidget, QTableWidgetItem, QHeaderView, QTabWidget, QStackedWidget
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
from welcomepage import WelcomePage
from networkgui import *
from scan_window import *
from port_window import *


class MainInterface(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.network = NetworkTopology()
        self.stacked_widget = stacked_widget
        main_layout = QVBoxLayout()

        back_button = QPushButton("Back to Home")
        back_button.setMinimumSize(60, 25)
        back_button.setStyleSheet("font-size: 12px; padding: 7px 15px;")
        back_button.clicked.connect(self.go_to_welcome_page)
        main_layout.addWidget(back_button)

        # Tabs
        tab_widget = QTabWidget()
        main_layout.addWidget(tab_widget)

        # Scan IP Tab
        scan_tab = QWidget()
        scan_layout = QVBoxLayout()
        scan_tab.setLayout(scan_layout)

        # Scan Ports Dropdown
        scan_ports_combo = QComboBox()
        self.scan_options_widget = ScanOptionsWidget(self.network)
        scan_layout.addWidget(self.scan_options_widget)
        tab_widget.addTab(scan_tab, "Scan Subnets")


        # Ports Tab
        port_tab= QWidget()
        port_layout = QVBoxLayout()
        self.port_options_widget = PortOptionsWidget(self.network)
        port_layout.addWidget(self.port_options_widget)
        port_tab.setLayout(port_layout)

        tab_widget.addTab(port_tab, "Scan Ports")



        # Display Topology Tab
        display_topology_tab = QWidget()
        display_topology_layout = QVBoxLayout()
        display_topology_tab.setLayout(display_topology_layout)
        display_topology_layout.addWidget(QLabel("Network Topology"))

        self.graph_window = GraphWindow(self.network)
        display_topology_layout.addWidget(self.graph_window)

        tab_widget.addTab(display_topology_tab, "Display Topology")
        tab_widget.currentChanged.connect(lambda: self.graph_window.display_graph(len(self.network.machines)))

        # Exploit Tab
        # exploit_tab = QWidget()
        # exploit_layout = QVBoxLayout()
        # exploit_tab.setLayout(exploit_layout)

        # exploit_layout.addWidget(QLabel("Menu for Exploit Options ex Default Credentials"))
        # tab_widget.addTab(exploit_tab, "Exploit")

        self.setLayout(main_layout)

    def go_to_welcome_page(self):
        self.stacked_widget.setCurrentIndex(0)


class ScanMasterX(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ScanMasterX")
        self.setGeometry(100, 100, 800, 600)

        # Main layout
        main_layout = QVBoxLayout()

        # Stacked widget for switching between welcome page and main interface
        self.stacked_widget = QStackedWidget()
        main_layout.addWidget(self.stacked_widget)

        # Add welcome page and main interface to the stacked widget
        self.stacked_widget.addWidget(WelcomePage(self.stacked_widget))
        self.stacked_widget.addWidget(MainInterface(self.stacked_widget))

        # Set main layout
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)


def main():
    app = QApplication(sys.argv)
    window = ScanMasterX()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()