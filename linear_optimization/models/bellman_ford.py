from math import inf


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
    ("E", "G", 6)
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

class Node():
    def __init__(self, ind: str, ud: str, cost: int) -> None:
        # FIXME : Find better names to "ind" and "ud" 
        self.ind = ind
        self.ud = ud
        self.cost = cost
        # NOTE : Add self.amount. Find a better name
    
    def __str__(self):
        return f"({self.ind} {self.ud} {self.cost})"
    
    def __repr__(self):
        return f"({self.ind} {self.ud} {self.cost})"


class Graph():
    def __init__(self):
        self.nodes = []
        self.nodes_names = []
    
    def add_node(self, node):
        node = Node(node[0], node[1], node[2])
        self.nodes.append(node)

        if node.ind not in self.nodes_names:
            self.nodes_names.append(node.ind)
        if node.ud not in self.nodes_names:
            self.nodes_names.append(node.ud)



    



class BellmandFord():

    def create_tabel(self, names) -> list[list[str]]:
        tabel = []
        tabel.append([" "] + names)
        for name in names:
            tabel.append([name] + [" "]*len(names))
        return tabel


    def solver(self, graph, start):
        #tabel = self.create_tabel(graph.nodes_names)
        tabel = [[inf for name in graph.nodes_names]]

        i = graph.nodes_names.index(start)

        tabel[0][i] = 0

        for i in range(len(graph.nodes_names) - 1):
            t = tabel[-1][:]
            t1 = tabel[-1][:]
            for node in graph.nodes:
                if t[graph.nodes_names.index(node.ud)] != inf and t[graph.nodes_names.index(node.ud)] + node.cost < t[graph.nodes_names.index(node.ind)]:
                    t1[graph.nodes_names.index(node.ind)] = t[graph.nodes_names.index(node.ud)] + node.cost
                print(t1)
            print()
            tabel.append(t1)


        # Print
        for row in tabel:
            print(row)
        


if __name__ == "__main__":
    g = Graph()

    for node in tree:
        g.add_node(node)
    
    b = BellmandFord()
    b.solver(g, "6")
