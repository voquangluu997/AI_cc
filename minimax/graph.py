class Node:
    def __init__(self, data, cost=100000, goal_cost=100000):
        self.data = data
        self.cost = cost
        self.goal_cost = goal_cost
        self.path = []
        self.parents = []
        self.children = []
        self.compare_mode = self.cost
        self.value = None
        self.alpha = -100000000
        self.beta = 100000000
        self.depth = 0
    def get_data(self):
        return self.data
    def get_info(self, reverse=False):
        if reverse:
            return self.data, self.compare_mode
        return self.compare_mode, self.data
    def get_children(self):
        return [node.get_data() for node in self.children]
    def get_parents(self):
        return [node.get_data() for node in self.parents]
    def get_neighbors(self):
        return [node.get_data() for node in self.neighbors()]
    def neighbors(self):
        children = self.children;
        parents = self.parents
        neigbors = children + parents
        seen = set()
        neigbors = [x for x in children + parents if not (x in seen or seen.add(x))]
        return neigbors
    def set_compare_mode(self, mode):
        if mode == 'goal_cost':
            self.compare_mode = self.goal_cost
        elif mode == "A*":
            self.compare_mode = self.goal_cost + self.cost
        else:
            self.compare_mode = self.cost
    def __lt__(self, other):
        return self.compare_mode < other.compare_mode

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
    def clear(self):
        self.nodes = []
        self.edges = []
    def number_of_nodes(self):
        return len(self.nodes)
    def number_of_edges(self):
        return len(self.edges)
    def get_index(self, node):
        for idx, n in enumerate(self.nodes):
            if n.get_data() == node.get_data():
                return idx
        return -1
    def add_node(self, node_name):
        node = Node(node_name)
        if not self.is_contains(node):
            self.nodes.append(node)
    def add_node_from(self, array_of_nodes_name):
        for el in array_of_nodes_name:
            node = Node(el)
            if not self.is_contains(node):
                self.nodes.append(node)
    def is_contains(self, node):
        for el in self.nodes:
            if el.get_data() == node.get_data():
                return True
        return False
    def add_edge(self, start_name, end_name, weight=100000):
        start_node = Node(start_name)
        end_node = Node(end_name)
        if not self.is_contains(start_node):
            self.add_node(start_name)
        if not self.is_contains(end_node):
            self.add_node(end_name)
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
            return [edges for edges in self.edges if edges[0].get_data() == start_node.get_data()
                    and edges[1].get_data() == end_node.get_data()][0]
        except:
            return None
    def show_nodes(self):
        return [node.get_info() for node in self.nodes]
    def show_edges(self):
        return [(edge[0].get_data(), edge[1].get_data()) for edge in self.edges]
    def set_compare_mode(self, mode):
        for node in self.nodes:
            node.set_compare_mode(mode)