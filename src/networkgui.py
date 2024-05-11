import sys
import networkx as nx
from PyQt6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QVBoxLayout, QWidget, QGraphicsEllipseItem, QGraphicsLineItem, QToolTip
from PyQt6.QtCore import QRectF, QPointF, QTimer
from PyQt6.QtGui import QBrush, QColor, QPen


class GraphNode(QGraphicsEllipseItem):
    ''' TODO
    1. add machine in as an input to associate it to a note
    2. set colors based off machine value.
    3. set labels based on machine tostring
    '''
    def __init__(self, label, x, y):
        super().__init__(QRectF(x - 55, y - 55, 110, 110))  # Center the ellipse on the coordinates
        # Need to edit this to reflect the hover menu
        self.label = label
        self.setBrush(QBrush(QColor(138, 3, 3)))
        self.setFlags(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsSelectable |
                        QGraphicsEllipseItem.GraphicsItemFlag.ItemIsFocusable)
        self.setAcceptHoverEvents(True)

        
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
        '''TODO
        Link generate report to this button
        Do we make a pop up what we do?
        '''
        print(f"Node {self.label} clicked")
        super().mousePressEvent(event)

class GraphWindow(QWidget):
    '''
    This made need to be edited to incorporate into main page.
    Or possible pop up?
    Automatic on page layout?
    '''

    def __init__(self):
        super().__init__()

        # Layout setup
        layout = QVBoxLayout(self)
        self.graphicsView = QGraphicsView()
        layout.addWidget(self.graphicsView)
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.scene.setSceneRect(-800, -800, 1600, 1600)  # Adjusted for potentially larger graph

        # Displays the graph. Function takes the node.
        # Maybe the topology class should be passed in?
        self.display_graph(20)

    def display_graph(self, num_nodes):
        ''' TODO
        1. Incorporate machines in here.
        2. do we need a get from the topology class
        '''

        nxG = nx.complete_graph(num_nodes)
        # Edit scale for spacing of buttons
        pos = nx.spring_layout(nxG, scale=600)

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
            node_item = GraphNode(f"127.0.0.{node + 1}", x, y)  
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

