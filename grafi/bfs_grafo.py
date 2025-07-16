from grafi import *
import queue

# crea i nodi
A = nodo_grafo(0)
B = nodo_grafo(1)
C = nodo_grafo(2)
D = nodo_grafo(3)
E = nodo_grafo(4)
F = nodo_grafo(5)
G = nodo_grafo(6)


#grafo non orientato
my_grafo = grafo_adiacent_matrix()

my_grafo.connetti_int(A,B)
my_grafo.connetti([(A,C,5), (A,B,4)])
my_grafo.connetti([(B,D,3), (B,E), (B,A)])
my_grafo.connetti([(C,D,0), (C,F), (C,A)])
my_grafo.connetti([(D,G,5), (D,F), (D,B), (D,E), (D,C)])
my_grafo.connetti([(E,D,2), (E,B)])
my_grafo.connetti([(F,D,4), (F,C)])
my_grafo.connetti([(G,D,7)])

#print(my_grafo.adiacenti(A))

def bfs (graph, node1, node2):
    coda = queue.Queue()
    coda.put(node1)
    cammino = dict()
    cammino[node1] = []
    visited = []
    while not coda.empty():
        node = coda.get()
        for adiacent in graph.adiacenti(node):
            if not adiacent in visited:
                visited.append(adiacent)
                coda.put(adiacent)
                cammino[adiacent] = cammino[node] + [adiacent]
            if adiacent == node2:
                return cammino[node2]
        
print(bfs(my_grafo, A, D))

def dfs (graph : grafo_adiacent_matrix, node1: nodo_grafo, node2: nodo_grafo):
    for node in graph.allNodes:
        node.visit = False
        node.pred = None
    return dfsVisit(graph, node1, node2)

def dfsVisit (graph : grafo_adiacent_matrix, node1: nodo_grafo, node2: nodo_grafo):
    for vicino in graph.adiacenti(node1):
        if not vicino.visit:

            if vicino == node2: 
                # arrivo alla fine, quindi mi ricostruisco 
                # il cammino all'indietro
                path = list()
                back_node = node2
                while back_node != None:
                    path.append(back_node)
                    back_node = back_node.pred
                return path
            else:
                vicino.visit = True
                vicino.pred = node1
                dfsVisit(graph, vicino, node2)

def ucs (graph : grafo_adiacent_matrix, node1: nodo_grafo, node2: nodo_grafo):
    coda = queue.PriorityQueue()
    coda.put((0, node1))
    visited = []
    visited.append(node1)
    while not coda.empty:
        current, cost = coda.get
        if current == node2:
            path = list()
            back_node = node2
            while back_node != None:
                path.append(back_node)
                back_node = back_node.pred
            return path
        for near, dist in graph.adiacenti_pesati(current):
            if near not in visited:
                visited.append(near)
                coda.put((dist + cost, near))



def dijkstra (graph : grafo_adiacent_matrix, node1: nodo_grafo, node2: nodo_grafo):
    coda = queue.PriorityQueue()
    for node in graph.allNodes:
        coda.put((float('inf'), node )) 
        # inizzializzo la distanza di tutti i nodi a infinito in maniera
        # da assicurarci che espandiamo soltanto i nodi dei quali abbiamo
        # già trovato almeno un vicino e quindi un cammino e una distanza
        node.pred = None
    coda.put((0, node1)) # così abbiamo un nodo da cui partire
    visited = []
    costi = {node: float('inf') for node in graph.allNodes}
    # utilizziamo un dizionario per tenere traccia dei costi dei nodi
    # questi sono i stessi che troviamo nella coda, ma dalla coda non possiamo
    # accedere direttamente al costo del nodo nodi, quindi li teniamo in un dizionario
    costi[node1] = 0
    while not coda.empty:
        current, _ = coda.get
        visited.append(current)
        if current == node2:
            path = list()
            back_node = node2
            while back_node != None:
                path.append(back_node)
                back_node = back_node.pred
            return path
        for near, dist in graph.adiacenti_pesati(current):
            if near not in visited:
                tmp = dist + costi[near]
                if tmp < costi[near]:
                    costi[near] = tmp
                    near.pred = current
                    coda.put((tmp, near))
                    # aggiorno il costo del nodo vicino e lo metto nella coda