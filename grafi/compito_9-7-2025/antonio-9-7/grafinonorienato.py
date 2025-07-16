import networkx as nx
import matplotlib.pyplot as plt

# Creazione di un grafo non orientato
grafo = nx.Graph()

# Aggiunta di nodi
grafo.add_nodes_from([1, 2, 3, 4])

# Aggiunta di archi (connessioni tra nodi)
grafo.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

# Disegno del grafo
nx.draw(grafo, with_labels=True, node_color='lightblue', node_size=800, font_size=10, font_color='black')
plt.title("Grafo Non Orientato")
plt.show()
