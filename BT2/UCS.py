import heapq
class Node:
    def __init__(self, label, cost=100000):
        self.label = label
        self.cost = cost
        self.path = []
        self.parents = []
        self.children = []
        self.depth = 0
    def __hash__(self):
        return hash(self.label)
    def __eq__(self, other):
        return self.label == other.label
    def __lt__(self, other):
        return self.cost < other.cost
    def get_label(self):
        return self.label
    def get_children(self):
        return [node.get_label() for node in self.children]
    def get_parents(self):
        return [node.get_label() for node in self.parents]
    def get_neighbors(self):
        return [node.get_label() for node in self.neighbors()]
    def neighbors(self):
        children = self.children
        parents = self.parents
        neigbors = children + parents
        seen = set()
        neigbors = [x for x in children + parents if not (x in seen or seen.add(x))]
        return neigbors
class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
    def get_index(self, node):
        for idx, n in enumerate(self.nodes):
            if n == node:
                return idx
        return -1
    def is_contains(self, node):
        for el in self.nodes:
            if el == node:
                return True
        return False
    def add_node(self, label):
        node = Node(label)
        if not self.is_contains(node):
            self.nodes.append(node)
    def add_node_from(self, array_of_label):
        for el in array_of_label:
            self.add_node(label=el)
    def add_edge(self, start_label, end_label, weight=10000):
        start_node = Node(start_label)
        end_node = Node(end_label)
        if not self.is_contains(start_node):
            self.add_node(start_node)
        if not self.is_contains(end_node):
            self.add_node(end_node)
        start_index = self.get_index(start_node)
        end_index = self.get_index(end_node)
        self.nodes[start_index].children.append(self.nodes[end_index])
        self.nodes[end_index].parents.append(self.nodes[start_index])
        self.edges.append((self.nodes[start_index], self.nodes[end_index], weight))
    def add_edges_from(self, array_of_tuple_node, is_duplicated=False):
        for tup in array_of_tuple_node:
            start = tup[0]
            end = tup[1]
            if len(tup) == 3:
                weight = tup[2] or 10000
            else:
                weight = 10000
            self.add_edge(start, end, weight)
            if is_duplicated:
                self.add_edge(end, start, weight)
    def get_edge(self, start_node, end_node):
        try:
            return [edges for edges in self.edges if edges[0] == start_node
                    and edges[1] == end_node][0]
        except:
            return None

def update_cost(g, current_node, prev_node):
    if g.get_edge(prev_node, current_node) is not None:
        if current_node.cost > prev_node.cost + graph.get_edge(prev_node, current_node)[2]:
            current_node.cost = prev_node.cost + graph.get_edge(prev_node, current_node)[2]
            current_node.path = prev_node.path + [current_node.get_label()]
def find_by_label(array_of_node, node):
    for idx, n in enumerate(array_of_node):
        if n == node:
            return idx
    return -1
def update_frontier(frontier, new_node):
    index = find_by_label(frontier, new_node)
    if index >= 0:
        if frontier[index] > new_node:
            frontier[index] = new_node
def uniform_cost_search(graph, initial_state, goalTest):
    frontier = list()
    explored = list()
    heapq.heapify(frontier)
    heapq.heappush(frontier, initial_state)
    while len(frontier) > 0:
        state = heapq.heappop(frontier)
        explored.append(state)
        if goalTest == state:
            return True
        for neighbor in state.neighbors():
            update_cost(graph, current_node=neighbor, prev_node=state)
            if neighbor.get_label() not in list(set([e.get_label() for e in frontier + explored])):
                heapq.heappush(frontier, neighbor)
            elif find_by_label(frontier, neighbor) is not -1:
                update_frontier(frontier, neighbor)
    return False
if __name__ == "__main__":
    graph = Graph()
    graph.add_node("S")
    graph.add_node_from(["S", "A", "B", "C", "D", "E", "F", "G", "H"])
    graph.add_edges_from(
        [
            ("S", "A", 3),
            ("S", "B", 6),
            ("S", "C", 2),
            ("A", "D", 3),
            ("B", "D", 4),
            ("B", "G", 9),
            ("B", "E", 2),
            ("C", "E", 1),
            ("D", "F", 5),
            ("E", "H", 5),
            ("F", "E", 6),
            ("H", "G", 8),
            ("F", "G", 5),
        ],
        is_duplicated=True
    )
    graph.nodes[0].cost = 0
    graph.nodes[0].path = ['S']
    result = uniform_cost_search(graph, graph.nodes[0], graph.nodes[7])
    print(result)
    if result:
        print("Min path from S to G: ")
        print(graph.nodes[7].path)