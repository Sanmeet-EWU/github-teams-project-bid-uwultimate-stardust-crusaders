import sys
import networkx as nx
from PyQt6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QVBoxLayout, QWidget, QGraphicsEllipseItem, QGraphicsLineItem, QToolTip
from PyQt6.QtCore import QRectF, QPointF, QTimer
from PyQt6.QtGui import QBrush, QColor, QPen


class GraphNode(QGraphicsEllipseItem):
    def __init__(self, label, x, y):
        super().__init__(QRectF(x - 55, y - 55, 110, 110))  # Center the ellipse on the coordinates
        self.label = label
        self.setBrush(QBrush(QColor(138, 3, 3)))
        self.setFlags(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsSelectable |
                        QGraphicsEllipseItem.GraphicsItemFlag.ItemIsFocusable)
        self.setAcceptHoverEvents(True)

    def hoverEnterEvent(self, event):
        print(f"Hovered over Node {self.label}")
        QToolTip.showText(event.screenPos(), self.label)
        super().hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        QToolTip.hideText()
        super().hoverLeaveEvent(event)


    def mousePressEvent(self, event):
        print(f"Node {self.label} clicked")
        super().mousePressEvent(event)

class GraphWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Layout setup
        layout = QVBoxLayout(self)
        self.graphicsView = QGraphicsView()
        layout.addWidget(self.graphicsView)
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.scene.setSceneRect(-800, -800, 1600, 1600)  # Adjusted for potentially larger graph

        # Initialize and display graph
        self.display_graph(20)  # Modify the number of nodes as needed

    def display_graph(self, num_nodes):
        # Create a graph
        nxG = nx.complete_graph(num_nodes)
        pos = nx.spring_layout(nxG, scale=800)  # Layout positions

        # Create nodes and add to scene
        for edge in nxG.edges:
            start_pos = QPointF(*pos[edge[0]])
            end_pos = QPointF(*pos[edge[1]])
            line = QGraphicsLineItem(start_pos.x(), start_pos.y(), end_pos.x(), end_pos.y())
            line.setPen(QPen(QColor(50, 50, 50), 2))  # Set edge color and thickness
            self.scene.addItem(line)

        for node in nxG.nodes:
            x, y = pos[node]
            node_item = GraphNode(f"127.0.0.{node + 1}", x, y)  # Creating GraphNode with IP-like label
            self.scene.addItem(node_item)


def main():
    app = QApplication(sys.argv)
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

