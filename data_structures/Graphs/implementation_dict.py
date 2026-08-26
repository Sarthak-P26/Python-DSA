class Graphs:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacent_list = {}

    def add_vertex(self, node):
        if node in self.adjacent_list:
            print("vertex/Node already exits")
            return node
        else:
            self.adjacent_list[node] = []
            self.number_of_nodes += 1
            return node
        


    def add_edge(self, node1, node2):
        if node1 not in self.adjacent_list:
            self.add_vertex(node1)
        if node2 not in self.adjacent_list:
            self.add_vertex(node2)

        if node2 in self.adjacent_list[node1] and node1 in self.adjacent_list[node2]:
            return "already exist"
        
        self.adjacent_list[node2].append(node1)
        self.adjacent_list[node1].append(node2)






graph = Graphs()

graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "D")

print(graph.adjacent_list)
print(graph.number_of_nodes)