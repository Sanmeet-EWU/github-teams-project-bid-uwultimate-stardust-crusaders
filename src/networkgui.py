import sys
import random
import networkx as nx
from PyQt6.QtWidgets import QApplication, QWidget, QDialog, QLabel, QGraphicsScene, QGraphicsView, QVBoxLayout, QWidget, QGraphicsEllipseItem, QGraphicsLineItem, QToolTip, QGraphicsPixmapItem
from PyQt6.QtCore import QRectF, QPointF, QTimer, Qt
from PyQt6.QtGui import QBrush, QColor, QPen, QPixmap
from machine import *
from network_topology import *


class GraphNode(QGraphicsEllipseItem):

    def __init__(self, machine, x, y):
        super().__init__(QRectF(x - 30, y - 30, 60, 60))  # Center the ellipse on the coordinates
        # Need to edit this to reflect the hover menu
        self.label = str(machine.IP)
        self.setBrush(QBrush(QColor(machine.color[0],machine.color[1],machine.color[2])))
        self.setFlags(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsSelectable |
                        QGraphicsEllipseItem.GraphicsItemFlag.ItemIsFocusable)
        self.setAcceptHoverEvents(True)
        self.machine = machine
        os_choice = random.choice(["../Images/windows.png", "../Images/tux.png"])
        print(os_choice)
        original_pixmap = QPixmap(str(os_choice))
        scaled_pixmap = original_pixmap.scaled(30, 30, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

        # Add the scaled image over the node
        self.image_item = QGraphicsPixmapItem(scaled_pixmap, self)
        self.image_item.setPos(x - scaled_pixmap.width() / 2, y - scaled_pixmap.height() / 2)  # Center the image at (x, y)
    def hoverEnterEvent(self, event):
        ''' 
        Function to show label over node
        '''
        QToolTip.showText(event.screenPos(), self.label)
        super().hoverEnterEvent(event)
    def hoverLeaveEvent(self, event):
        '''
        Clean up function to remove label
        '''
        QToolTip.hideText()
        super().hoverLeaveEvent(event)


    def mousePressEvent(self, event):
        print(f"Node {self.label} clicked")
        if event.button() == event.buttons().LeftButton:
            self.show_security_report()
        super().mousePressEvent(event)
    
    def show_security_report(self):
        '''
        Might need some pretty edits temp code till I get the data types needed
        '''

        dialog = QDialog()
        dialog.setWindowTitle("Security Report")
        layout = QVBoxLayout()
        report = self.machine.generate_report()
        report_label = QLabel(report)
        layout.addWidget(report_label)
        dialog.setLayout(layout)
        dialog.resize(400, 300)
        dialog.exec()

class GraphWindow(QWidget):
    '''
    This made need to be edited to incorporate into main page.
    Or possible pop up?
    Automatic on page layout?
    '''

    def __init__(self, network):
        super().__init__()
        self.network = network
        # Layout setup
        layout = QVBoxLayout(self)
        self.graphicsView = QGraphicsView()
        layout.addWidget(self.graphicsView)
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.scene.setSceneRect(-800, -800, 1600, 1600)  # Adjusted for potentially larger graph

        # Displays the graph. Function takes the node.
        # Maybe the topology class should be passed in?

    def display_graph(self, num_nodes):
        ''' TODO
        1. Incorporate machines in here.
        2. do we need a get from the topology class
        '''
        self.scene.clear()
        # Mock array for machines.
        nxG = nx.complete_graph(num_nodes)
        # Edit scale for spacing of buttons
        pos = nx.spring_layout(nxG, scale=200)

        # Create nodes and add to scene
        for edge in nxG.edges:
            start_pos = QPointF(*pos[edge[0]])
            end_pos = QPointF(*pos[edge[1]])
            line = QGraphicsLineItem(start_pos.x(), start_pos.y(), end_pos.x(), end_pos.y())
            # Set edge color and thickness
            line.setPen(QPen(QColor(50, 50, 50), 2))  
            self.scene.addItem(line)

        for node in nxG.nodes:
            # Get coordinates of the graph
            x, y = pos[node]
            # Need to add the machine in this constructor
            machine = Machine(f"127.0.0.{node+1}")
            node_item = GraphNode(machine, x, y)  
            self.scene.addItem(node_item)


def main():
    app = QApplication(sys.argv)
    # Random css for the hover events
    app.setStyleSheet("""
    QToolTip {
        background-color: #2a82da; /* Light blue background */
        color: white;             /* White text */
        border: 1px solid white;  /* White border */
        padding: 5px;             /* Padding inside the tooltip */
        border-radius: 5px;       /* Rounded corners */
        font: bold 12px;          /* Bold font and size */
        opacity: 200;             /* Partial transparency (0-255) */
    }
    """)
    window = GraphWindow()
    window.resize(1024, 768)
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

