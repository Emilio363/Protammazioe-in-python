import matplotlib.pyplot as plt
import networkx as nx

# Funzione per la ricerca in profondità (DFS)
def dfs(matrix, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(f"Visito il nodo: {start}")
    
    for neighbor, is_connected in enumerate(matrix[start]):
        if is_connected and neighbor not in visited:
            dfs(matrix, neighbor, visited)
    return visited

# Matrice di adiacenza per un grafo orientato
# Esempio: Nodo 0 -> Nodo 1, Nodo 1 -> Nodo 2, Nodo 2 -> Nodo 0
adj_matrix = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0]
]

# Nodo di partenza
start_node = 0

# Esegui DFS
print("Ricerca in profondità:")
dfs(adj_matrix, start_node)

# Visualizzazione del grafo
def plot_graph(matrix):
    G = nx.DiGraph()  # Grafo orientato
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                G.add_edge(i, j)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=15, font_weight='bold', arrowsize=20)
    plt.title("Visualizzazione del Grafo Orientato")
    plt.show()

plot_graph(adj_matrix)
