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

# Matrice di adiacenza per un grafo non orientato
# Esempio: Grafo con 5 nodi (0, 1, 2, 3, 4)
adj_matrix = [
    [0, 1, 0, 0, 1],  # Nodo 0 è connesso a 1 e 4
    [1, 0, 1, 1, 0],  # Nodo 1 è connesso a 0, 2 e 3
    [0, 1, 0, 1, 0],  # Nodo 2 è connesso a 1 e 3
    [0, 1, 1, 0, 1],  # Nodo 3 è connesso a 1, 2 e 4
    [1, 0, 0, 1, 0],  # Nodo 4 è connesso a 0 e 3
]

# Avvio della DFS dal nodo 0
print("Ricerca in profondità (DFS):")
dfs(adj_matrix, start=0)

# Visualizzazione del grafo con NetworkX
def plot_graph(matrix):
    G = nx.Graph()
    num_nodes = len(matrix)
    for i in range(num_nodes):
        for j in range(i, num_nodes):  # Solo metà matrice (grafo non orientato)
            if matrix[i][j] == 1:
                G.add_edge(i, j)
    nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold', node_size=700)
    plt.title("Visualizzazione del Grafo")
    plt.show()

plot_graph(adj_matrix)
