import networkx as nx
import matplotlib.pyplot as plt

# Creazione di un grafo orientato
G = nx.DiGraph()

# Aggiunta di nodi
G.add_nodes_from([1, 2, 3, 4])

# Aggiunta di archi orientati (da nodo a nodo)
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

# Disegno del grafo
pos = nx.spring_layout(G)  # Layout per posizionare i nodi
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=15)

# Mostra il grafo
plt.title("Grafo Orientato")
plt.show()

