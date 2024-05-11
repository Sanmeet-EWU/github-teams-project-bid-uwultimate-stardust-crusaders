import sys
import networkx as nx
from PyQt6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QVBoxLayout, QWidget, QGraphicsEllipseItem
from PyQt6.QtCore import QRectF
from PyQt6.QtGui import QBrush, QColor

class GraphNode(QGraphicsEllipseItem):
    def __init__(self, label, x, y):
        super().__init__(QRectF(x - 15, y - 15, 30, 30))  # Center the ellipse on the coordinates
        self.label = label
        self.setBrush(QBrush(QColor(138, 3, 3)))
        self.setFlags(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsMovable)

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
        self.display_graph(55)  # Passing the number of nodes as a parameter

    def display_graph(self, num_nodes):
        G = nx.Graph()
        host_node = "Host"
        G.add_node(host_node)
        for i in range(1, num_nodes):
            node_name = f"Node {i}"
            G.add_node(node_name)
            G.add_edge(host_node, node_name)  # Connect each new node to the host

        # Using Kamada-Kawai layout
        pos = nx.kamada_kawai_layout(G)

        # Create graph nodes and add to scene
        for node, p in pos.items():
            x, y = p[0] * 200, p[1] * 200  # Scale positions for better visibility
            node_item = GraphNode(node, x, y)
            self.scene.addItem(node_item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GraphWindow()
    window.resize(1024, 768)
    window.show()
    sys.exit(app.exec())

