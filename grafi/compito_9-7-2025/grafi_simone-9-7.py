from typing import List
import queue

class Nodo:
    def __init__(self, id: int):
        self.id: int = id
        self.adiacenti: list['Nodo'] = []

    def connetti(self, nodi: list['Nodo'], orientato: bool):
        for nodo in nodi:
            if nodo not in self.adiacenti:
                self.adiacenti.append(nodo)                
                if not orientato:
                    # Il grafo non è orientato: crea un collegamento a sè stesso sull'altro nodo
                    nodo.adiacenti.append(self)

    def __str__(self):
        if len(self.adiacenti) > 0:
            ids = ""
            for item in self.adiacenti:
                ids += f"{item.id}, "
            return f"Nodo {self.id} è connesso con Nodo: {ids[:-2]}"
        else:
            return f"Nodo {self.id} non è connesso ad altri nodi"
        
    def __repr__(self) -> str:
        id_adiacenti = [n.id for n in self.adiacenti]
        return f"Nodo({self.id}, adiacenti={id_adiacenti})"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Nodo) and self.id == other.id

class QueueItem:
    def __init__(self, item: Nodo, path: list['Nodo']) -> None:
        self.item: Nodo = item
        self.path: list['Nodo'] = path

    def __str__(self) -> str:
        ids_path = "->".join(str(n.id) for n in self.path + [self.item])
        return ids_path

class Grafo:
    def __init__(self, orientato: bool) -> None:
        self.nodi:list['Nodo'] = []
        self.orientato = orientato

    def crea_nodo(self, id: int) -> Nodo:
        nodo = Nodo(id)
        if nodo not in self.nodi:
            self.nodi.append(nodo)
            return nodo
        else:
            raise ValueError(f"Nodo già esistente: {id}")
    
    def connetti(self, nodo_partenza: Nodo, nodi_da_connettere: list["Nodo"]) -> bool:
        nodo = next((n for n in self.nodi if n.id == nodo_partenza.id), None)
        if nodo:
            nodo.connetti(nodi_da_connettere, self.orientato)
            return True
        else:
            return False

    def crea_percorso(self, nodo_partenza: Nodo, nodo_destinazione: Nodo) -> list[int] | None:
        if nodo_partenza == nodo_destinazione:
            print("Il nodo di partenza e di destinazione coincidono!")
            return

        nodi_visitati: list[Nodo] = [nodo_partenza]
        coda_ricerca: queue.Queue[QueueItem] = queue.Queue()
        coda_ricerca.put(QueueItem(nodo_partenza, []))

        # Ciclo while per la coda di nodi da visitare
        while not coda_ricerca.empty():
            qitem = coda_ricerca.get()
            nodo_attuale = qitem.item

            # Ciclo per i nodi adiacenti del nodo attuale
            for adiacente in nodo_attuale.adiacenti:
                if adiacente not in nodi_visitati:
                    nuovo_path = qitem.path + [nodo_attuale]
                    if adiacente == nodo_destinazione:
                        # Restituisce una lista di id dei nodi nel path + il nodo finale
                        return [nodo.id for nodo in nuovo_path + [adiacente]]
                    nodi_visitati.append(adiacente)
                    coda_ricerca.put(QueueItem(adiacente, nuovo_path))

        return None


if __name__ == "__main__":
    g = Grafo(orientato=False)
    nodo0 = g.crea_nodo(0)
    nodo1 = g.crea_nodo(1)
    nodo2 = g.crea_nodo(2)
    nodo3 = g.crea_nodo(3)
    nodo4 = g.crea_nodo(4)
    nodo5 = g.crea_nodo(5)
    nodo6 = g.crea_nodo(6)

    g.connetti(nodo0, [nodo2, nodo1])
    g.connetti(nodo1, [nodo3, nodo4, nodo0])
    g.connetti(nodo2, [nodo3, nodo5, nodo0])
    g.connetti(nodo3, [nodo6, nodo5, nodo1, nodo4, nodo2])
    g.connetti(nodo4, [nodo3, nodo1])
    g.connetti(nodo5, [nodo3, nodo2])
    g.connetti(nodo6, [nodo3])

    path = g.crea_percorso(nodo0, nodo6)
    if path:
        print(f"Percorso: {path}")
    else:
        print("Nessun percorso.")