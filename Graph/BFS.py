class graph:
    def __init__(self):
        self.graph={}
    def add_edge(self,u,v):
        if u not in self.graph:
            self.graph[u]=[]
        if v not in self.graph:
            self.graph[v]=[]
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def bfs(self,start):
        visited=set()
        queue=[start]
        visited.add(start)
        while queue:
            node=queue.pop(0)
            print(node,end="->") # Process the node (e.g., print it)
            for neighbor in self.graph.get(node,[]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

if __name__ == "__main__":
    g=graph()
    g.add_edge(0,1)
    g.add_edge(0,6)
    g.add_edge(1,3)
    g.add_edge(1,4)
    g.add_edge(2,5)
    g.add_edge(2,6)

    print("BFS starting from node 0:")
    g.bfs(0)