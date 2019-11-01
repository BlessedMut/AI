import queue as queue
from A_Star_Algo_Graph import a_star_graph, H

def best_first_search(graph, start_node, dest_node):
    expanded_nodes = []  
    visited_nodes_queue = queue.PriorityQueue()  
    maximum_memory_usage = 0  
    expanded_nodes.append(start_node)
    start_node.visited = True
    current_node = start_node
    while True:
        
        if dest_node.visited:
            break
        for x in current_node.children:
            if not x.visited:
                x.visited = True
                x.parent = current_node
                
                x.costFromOrigin = current_node.costFromOrigin + current_node.children[x]
                visited_nodes_queue.put((x.heuristic, x))
        maximum_memory_usage = max(maximum_memory_usage, visited_nodes_queue.qsize())
        current_node = visited_nodes_queue.get(0)[1]
        expanded_nodes.append(current_node)
    return expanded_nodes.__len__(), visited_nodes_queue.qsize(), maximum_memory_usage
print(best_first_search(graph,A,C))


# def tree_best_first_search(graph, start_node, dest_node):
#     expanded_nodes = []  
#     visited_nodes_queue = queue.PriorityQueue()  
#     maximum_memory_usage = 0  
#     expanded_nodes.append(start_node)
#     current_node = start_node
#     while True:
#         if expanded_nodes.__contains__(dest_node):
#             break
#         for x in current_node.children:
#             x.parent = current_node
#             visited_nodes_queue.put((x.heuristic, x))
#         maximum_memory_usage = max(maximum_memory_usage, visited_nodes_queue.qsize())
#         current_node = visited_nodes_queue.get(0)[1]
#         expanded_nodes.append(current_node)
#     return expanded_nodes.__len__(), visited_nodes_queue.qsize(), maximum_memory_usage
