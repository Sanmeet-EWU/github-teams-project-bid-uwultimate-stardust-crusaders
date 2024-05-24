from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class WelcomePage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        layout = QVBoxLayout()
        welcome_label = QLabel("Welcome to ScanMasterX")
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome_label.setStyleSheet("font-size: 24px; font-weight: bold;")

        # Add logo
        logo_label = QLabel()
        logo_pixmap = QPixmap("scanmasterlogo.png")
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(logo_label)

        start_button = QPushButton("Start")
        start_button.setMinimumSize(100, 50)
        start_button.setStyleSheet("font-size: 18px; padding: 10px 20px;")
        start_button.clicked.connect(lambda: stacked_widget.setCurrentIndex(1)) # Switch to main interface
        layout.addWidget(welcome_label)
        layout.addWidget(start_button)
        layout.setAlignment(start_button, Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)
