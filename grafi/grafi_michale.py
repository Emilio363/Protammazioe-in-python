class nodo_grafo:
    orientato = True 
    def __init__(self, valore):
        self.valore = valore
        self.connessioni = set()

    def connetti(self, nodi):
        for nodo in nodi:
            self.connessioni.add(nodo)

    def adiacenti(self):
        return self.connessioni
    
    def __str__(self):
        return self.valore

# carica i nodi
nodo0 = nodo_grafo(0)
nodo1 = nodo_grafo(1)
nodo2 = nodo_grafo(2)
nodo3 = nodo_grafo(3)
nodo4 = nodo_grafo(4)
nodo5 = nodo_grafo(5)
nodo6 = nodo_grafo(6)

#orientato
nodo0.connetti([nodo2])
nodo1.connetti( [nodo3, nodo4, nodo0] )
nodo2.connetti([nodo3, nodo5])
nodo3.connetti([nodo6, nodo5])
nodo4.connetti([nodo3])

# stampa tutti i nodi adiacenti a un nodo dato
print(nodo1.adiacenti())

#grafo non orientato
nodo0.connetti([nodo2, nodo1])
nodo1.connetti([nodo3, nodo4, nodo0])
nodo2.connetti([nodo3, nodo5, nodo0])
nodo3.connetti([nodo6, nodo5, nodo1, nodo4, nodo2])
nodo4.connetti([nodo3, nodo1])
nodo5.connetti([nodo3, nodo2])
nodo6.connetti([nodo3])