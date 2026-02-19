class graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def print_Graph(self):
            for i in range(self.V):
                for j in range(self.V):
                    print(self.graph[i][j], end=' ')
                print()

if __name__ == "__main__":
    g = graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.print_Graph()
  