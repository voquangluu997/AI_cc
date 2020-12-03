import networkx as nx
def Depth_First_Search(initialState, goalTest):
    frontier = []
    frontier.append(initialState)
    explored = []
    while len(frontier) > 0:
        print("frontier: ", frontier)
        state = frontier.pop(len(frontier)-1)
        explored.append(state)
        if goalTest == state:
            return True
        for neighbor in G.neighbors(state):
            if neighbor not in list(set(frontier + explored)):
                frontier.append(neighbor)
    return False
if __name__ == "__main__":
    G = nx.Graph()
    G.add_nodes_from(["S", "A", "B", "C", "D", "E", "F", "G", "H"])
    G.add_weighted_edges_from(
        [
            ("S", "A", 3),
            ("S", "B", 6),
            ("S", "C", 2),
            ("A", "D", 3),
            ("B", "D", 4),
            ("B", "E", 2),
            ("B", "G", 9),
            ("C", "E", 1),
            ("D", "F", 5),
            ("E", "H", 5),
            ("E", "F", 6),
            ("H", "G", 8),
            ("F", "G", 5),
        ]
    )
    result = Depth_First_Search("S", "G")
    print(result)