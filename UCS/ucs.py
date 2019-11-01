from queue import PriorityQueue
from vertex import *
from Graph import *


def ucs(graph, start, goal):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start))

    while queue:
        cost, node = queue.get()
        if node not in visited:
            visited.add(node)

            if node == goal:
                return
            for i in graph.getVertex(node):
                if i not in visited:
                    total_cost = cost + graph.getWeight(node, i)
                    queue.put((total_cost, i))

ucs(Graph, 'S', 'G')





