import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
# Definizione del grafo come matrice di adiacenza
# 0 indica nessuna connessione, 1 indica una connessione
matrice_adiacenza = np.array([
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
])

print("Matrice di adiacenza:")
print(matrice_adiacenza)

# Creazione del grafo da una matrice di adiacenza
G = nx.from_numpy_array(matrice_adiacenza)

# Disegno del grafo
plt.figure(figsize=(6, 6))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=800, font_size=10)
plt.title("Grafo non orientato")
plt.show()
