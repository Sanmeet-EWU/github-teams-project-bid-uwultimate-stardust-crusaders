from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class WelcomePage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        outer_layout = QVBoxLayout()
        outer_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        welcome_label = QLabel("Welcome To ScanMasterX")
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome_label.setStyleSheet("""
            font-size: 22px;
            color: black;
            font-weight: bold;
            padding: 10px;
            border: 2px solid rgb(206, 41, 41);
            background-color: #FFFFFF;
            border-radius: 5px;
        """)
        welcome_label.setFixedSize(welcome_label.sizeHint().width() + 60, welcome_label.sizeHint().height() + 20)

        logo_label = QLabel()
        logo_pixmap = QPixmap("../Images/logo.png")
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        start_button = QPushButton("Start")
        start_button.setMinimumSize(100, 50)
        start_button.setStyleSheet("""
                    font-size: 20px;
                    font-weight: bold;
                    padding: 10px 20px;
                    border: 2px solid rgb(206, 41, 41);                   
                    border-radius: 10px;
                    background-color: #FFFFFF;
                    color: #000000;
                """)
        start_button.clicked.connect(lambda: stacked_widget.setCurrentIndex(1))  # Switch to main interface

        inner_layout = QVBoxLayout()
        inner_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        inner_layout.addWidget(logo_label)
        inner_layout.addWidget(welcome_label)
        inner_layout.addWidget(start_button)

        outer_layout.addLayout(inner_layout)

        self.setLayout(outer_layout)
