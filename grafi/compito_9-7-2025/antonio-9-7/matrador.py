import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Definizione della matrice di adiacenza
# 0 indica nessuna connessione, 1 indica una connessione
matrice_adiacenza = np.array([
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 1, 1],
    [0, 0, 0, 0]
])

# Creazione del grafo orientato da una matrice di adiacenza
grafo = nx.from_numpy_array(matrice_adiacenza, create_using=nx.DiGraph)

# Visualizzazione della matrice di adiacenza
print("Matrice di adiacenza:")
print(matrice_adiacenza)

# Disegno del grafo
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(grafo)  # Layout per il posizionamento dei nodi
nx.draw(grafo, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
nx.draw_networkx_edge_labels(grafo, pos, edge_labels={(i, j): matrice_adiacenza[i, j] for i, j in grafo.edges()})
plt.title("Grafo Orientato")
plt.show()
