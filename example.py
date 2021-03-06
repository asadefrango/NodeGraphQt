import os
import sys

from PySide import QtGui, QtCore

# load in the example nodes.
from NodeGraphQt import nodes
# import the widgets.
from NodeGraphQt.interfaces import NodeGraphWidget, Node


class MyNode(Node):
    """
    This is a example test node.
    """
    NODE_TYPE = 'MyNode'

    def __init__(self):
        super(MyNode, self).__init__()
        self.set_name('my test node')
        self.set_color(81, 54, 88)
        self.add_input('in')
        self.add_output('out')


class NodeGraph(NodeGraphWidget):
    """
    Example node graph widget.
    """

    def __init__(self, parent=None):
        super(NodeGraph, self).__init__(parent)
        self.setWindowTitle('PySide Node Graph')
        self.resize(1100, 800)

    def keyPressEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    # create node graph.
    graph = NodeGraph()
    graph.show()

    # add a node.
    my_node = MyNode()
    graph.add_node(my_node)

    # create the nodes from the "nodes" package dir.
    foo_node = graph.create_node(
        'NodeGraphQt.nodes.simple_nodes.FooNode', name='Foo Node')
    bar_node = graph.create_node(
        'NodeGraphQt.nodes.simple_nodes.BarNode', name='Bar Node')
    text_node = graph.create_node(
        'NodeGraphQt.nodes.text_input_node.TextInputNode', name='Text Node')
    menu_node = graph.create_node(
        'NodeGraphQt.nodes.menu_node.DropdownMenuNode', name='Menu Node')

    # change the color on "foo_node"
    foo_node.set_color(2, 67, 81)

    # change icon on "bar_node"
    this_path = os.path.dirname(os.path.abspath(__file__))
    icon = os.path.join(this_path, 'example', 'example_icon.png')
    bar_node.set_icon(icon)

    # position nodes.
    foo_node.set_pos(-487.0, 141.0)
    bar_node.set_pos(-77.0, 17.0)
    text_node.set_pos(-488.0, -158.0)
    menu_node.set_pos(310.0, -97.0)
    my_node.set_pos(310.0, 10.0)

    # connect nodes
    foo_node.set_output(0, bar_node.input(2))
    menu_node.set_input(0, bar_node.output(1))
    bar_node.set_input(0, text_node.output(0))

    bar_node.disable()

    app.exec_()
