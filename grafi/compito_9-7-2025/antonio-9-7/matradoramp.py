from collections import deque
import matplotlib.pyplot as plt
import networkx as nx

def bfs(graph, start):
    """
    Esegue la ricerca in ampiezza (BFS) su un grafo orientato rappresentato da una matrice di adiacenza.
    :param graph: Matrice di adiacenza (lista di liste)
    :param start: Nodo di partenza (indice)
    :return: Lista dei nodi visitati in ordine di visita
    """
    visited = [False] * len(graph)  # Traccia i nodi visitati
    queue = deque([start])          # Coda per la BFS
    visited[start] = True           # Marca il nodo di partenza come visitato
    result = []                     # Lista dei nodi visitati in ordine

    while queue:
        node = queue.popleft()
        result.append(node)

        # Esplora i vicini del nodo corrente
        for neighbor, is_connected in enumerate(graph[node]):
            if is_connected and not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

    return result

# Esempio di matrice di adiacenza per un grafo orientato
adj_matrix = [
    [0, 1, 0, 0, 1],  # Nodo 0 è connesso a 1 e 4
    [0, 0, 1, 0, 0],  # Nodo 1 è connesso a 2
    [0, 0, 0, 1, 0],  # Nodo 2 è connesso a 3
    [0, 0, 0, 0, 0],  # Nodo 3 non ha connessioni
    [0, 0, 1, 0, 0],  # Nodo 4 è connesso a 2
]

# Esegui la BFS partendo dal nodo 0
start_node = 0
visited_nodes = bfs(adj_matrix, start_node)
print(f"Nodi visitati in ordine: {visited_nodes}")

# Visualizzazione del grafo con NetworkX
def plot_graph(adj_matrix):
    G = nx.DiGraph()
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix[i])):
            if adj_matrix[i][j] == 1:
                G.add_edge(i, j)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=10)
    plt.title("Grafo Orientato")
    plt.show()

plot_graph(adj_matrix)
