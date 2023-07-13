from linear_optimization.node import Node


class Graph:
    def __init__(self) -> None:
        self.egdes = []
        self.nodes = []

    def add_node(self, node: list(str | int)):
        node = Node(node[0], node[1], node[2])
        self.nodes.append(node)

        if node.ind not in self.egdes:
            self.egdes.append(node.ind)
        if node.ud not in self.egdes:
            self.egdes.append(node.ud)
