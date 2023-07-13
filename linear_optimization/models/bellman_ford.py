from math import inf

from linear_optimization.graph import Graph

tree = [
    ("A", "B", 5),
    ("A", "C", 1),
    ("A", "D", 3),
    ("B", "E", 4),
    ("C", "B", 2),
    ("C", "D", 4),
    ("C", "E", 5),
    ("D", "G", 9),
    ("E", "D", 1),
    ("E", "G", 6),
]

tree = [
    ("1", "2", 1),
    ("1", "3", 1),
    ("1", "4", 3),
    ("2", "5", 4),
    ("3", "2", 2),
    ("3", "5", 5),
    ("3", "4", 4),
    ("4", "6", 9),
    ("5", "4", 1),
    ("5", "6", 6),
]


class BellmandFord:
    def solver(self, graph: Graph, start: str):
        tabel = [[inf for name in graph.egdes]]

        i = graph.egdes.index(start)

        tabel[0][i] = 0

        for _ in range(len(graph.egdes) - 1):
            t = tabel[-1][:]
            t1 = tabel[-1][:]
            for node in graph.nodes:
                if (
                    t[graph.egdes.index(node.ud)] != inf
                    and t[graph.egdes.index(node.ud)] + node.cost < t[graph.egdes.index(node.ind)]
                ):
                    t1[graph.egdes.index(node.ind)] = (
                        t[graph.egdes.index(node.ud)] + node.cost
                    )

            if t == t1:
                break
            tabel.append(t1)

        # Print
        for row in tabel:
            print(row)


# NOTE : Delete if __name__ == "__main__" when the algorithm is complet
if __name__ == "__main__":
    graph = Graph()

    for node in tree:
        graph.add_node(node)

    b = BellmandFord()
    b.solver(graph, "6")
