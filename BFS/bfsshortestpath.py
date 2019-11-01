graph = {'A': ['B', 'C', 'E'],'B': ['A','D', 'E'], 'C': ['A', 'F', 'G'],'D': ['B'], 'E': ['A', 'B','D'], 'F': ['C'],'G': ['C']}
# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal):
    explored = []
    queue = [[start]]
    if start == goal:
        return "That was easy! Start = goal"
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path
            explored.append(node)
    return "So sorry, but a connecting path doesn't exist :("
print(bfs_shortest_path(graph, 'G', 'D') ) # returns ['G', 'C', 'A', 'B', 'D']
