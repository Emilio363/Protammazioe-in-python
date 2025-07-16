class nodo_grafo:
    orientato = True 
    def __init__(self, valore):
        self.valore = valore
        self.adiacenti = set()

    def connetti(self, nodi):
        for nodo in nodi:
            self.adiacenti.add(nodo)
            if not nodo_grafo.orientato:
                nodo.adiacenti.add(self)

    def __repr__(self):
        return f"Nodo({self.valore})"

    def stampa_adiacenti(self):
        adiacenti_str = ', '.join(str(nodo.valore) for nodo in self.adiacenti)
        print("Nodi adiacenti a {self.valore}: {adiacenti_str}")


