graph_dfs = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'D']),
         'D': set(['B', 'C']),
         'E': set(['B', 'F']),
         'F': set(['E', 'G']),
         'G': set(['F', 'H']),
         'H': set(['G', 'I']),
         'I': set(['H', 'J']),
         'J': set(['I', 'K']),
         'K': set(['J', 'L']),
         'L': set(['K'])
         }

graph_bfs = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'D'],
         'D': ['B', 'C'],
         'E': ['B', 'F'],
         'F': ['E', 'G'],
         'G': ['F', 'H'],
         'H': ['G', 'I'],
         'I': ['H', 'J'],
         'J': ['I', 'K'],
         'K': ['J', 'L'],
         'L': ['K']
         }



rep = {'A': '3M3CL',
        'B': '2MCB',
        'C': 'CMR',
        'D': '3MC2L',
        'E': '3MCL',
        'F': '2M2CR',
        'G': '2M2CL',
        'H': '3MCR',
        'I': '3CL',
        'J': '3M2CR',
        'K': '2CL',
        'L': '3M3CL'
       }
