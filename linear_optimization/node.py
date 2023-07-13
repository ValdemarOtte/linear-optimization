class Node:
    def __init__(self, ind: str, ud: str, cost: int) -> None:
        # FIXME : Find better names to "ind" and "ud"
        self.ind = ind
        self.ud = ud
        self.cost = cost
        # NOTE : Add self.amount. Find a better name

    def __str__(self) -> str:
        return f"({self.ind} {self.ud} {self.cost})"

    def __repr__(self) -> str:
        return f"({self.ind} {self.ud} {self.cost})"
