from collections import deque
import matplotlib.pyplot as plt
import networkx as nx

def bfs(matrix, start_node):
    num_nodes = len(matrix)
    visited = [False] * num_nodes
    queue = deque([start_node])
    visited[start_node] = True
    traversal_order = []

    while queue:
        current_node = queue.popleft()
        traversal_order.append(current_node)

        for neighbor, is_connected in enumerate(matrix[current_node]):
            if is_connected and not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

    return traversal_order

# Esempio di matrice di adiacenza per un grafo non orientato
adj_matrix = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [0, 1, 0, 0]
]

# Nodo di partenza
start_node = 0

# Esegui BFS
result = bfs(adj_matrix, start_node)
print("Ordine di visita BFS:", result)

# Visualizzazione del grafo
def plot_graph(matrix):
    G = nx.Graph()
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            if matrix[i][j] == 1:
                G.add_edge(i, j)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    plt.show()

plot_graph(adj_matrix)
