import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Creazione di un grafo orientato
G = nx.DiGraph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])
pos = nx.spring_layout(G)  # Layout per posizionare i nodi
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=15)
plt.title("Grafo Orientato")
plt.show()


# Creazione di un grafo non orientato
grafo = nx.Graph()
grafo.add_nodes_from([1, 2, 3, 4])
grafo.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])
nx.draw(grafo, with_labels=True, node_color='lightblue', node_size=800, font_size=10, font_color='black')
plt.title("Grafo Non Orientato")
plt.show()

# Definizione del grafo come matrice di adiacenza
matrice_adiacenza = np.array([
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
])
G = nx.from_numpy_array(matrice_adiacenza)
plt.figure(figsize=(6, 6))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=800, font_size=10)
plt.title("Grafo non orientato")
plt.show()