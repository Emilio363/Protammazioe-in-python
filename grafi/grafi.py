import numpy as np

class nodo_grafo:
    def __init__(self, valore):
        self.valore = valore
        self.visit = False
        self.pred = None
    
    def __str__(self):
        return self.valore

class grafo_adiacent_matrix: # implementazione del grafo orientato con matrice di adiacenza
    def __init__(self):
        self.__dimension = 2
        self.__mask = np.ndarray( (self.__dimension, self.__dimension), dtype = bool)
        # mi serve per sapere quali valori ho inserito e quali invece sono
        # lì per sbaglio
        self._matrice = np.empty( (self.__dimension, self.__dimension), dtype = np.float32)
        self.nodi = dict()
        self.indici = dict()
        self.num_nodi = 0
        
        
    def connetti(self, lista):
        for cup in lista:
            if len(cup) == 2:
                self.connetti_int(cup[0], cup[1])
            elif len(cup) == 3:
                self.connetti_int(cup[0], cup[1], cup[2])
            else:
                raise AttributeError("cossa te ga combinà 'ddeso?!?!")
        
    def connetti_int(self, nodo1: nodo_grafo, nodo2: nodo_grafo, value: int = 1):
        '''
        se non presente, aggiungi il nodo alla lista e il suo indice alla lista
            per entrambi i nodi
        se il numero di nodi è maggiore della dimensione della matrice:
            raddoppia la dimensione della matrice
            crea una nuova matrice vuota di dimensione doppia
            riempi la nuova matrice con i valori di quella vecchia
        alla fine metto il valore nel posto giusto
        '''
        if not nodo1 in self.nodi:
            self.nodi[nodo1] = self.num_nodi
            self.indici[self.num_nodi] = nodo1
            self.num_nodi +=1
        if not nodo2 in self.nodi:
            self.nodi[nodo2] = self.num_nodi
            self.indici[self.num_nodi] = nodo2
            self.num_nodi +=1
            
        if self.num_nodi > self.__dimension:
            
            newmatrix = np.empty( (self.__dimension*2, self.__dimension*2), dtype = np.float32)
            newmatrix[:self.__dimension, :self.__dimension] = self._matrice
            self._matrice = newmatrix
            
            newmask = np.ndarray( (self.__dimension*2, self.__dimension*2), dtype = bool)
            newmask[:self.__dimension, :self.__dimension] = self.__mask
            self.__mask = newmask
            self.__dimension *= 2
        
        self._matrice[self.nodi[nodo1], self.nodi[nodo2] ] = value
        self.__mask[self.nodi[nodo1], self.nodi[nodo2] ] = True

    def adiacenti(self, nodo):
        lista = list()
        row = self.nodi[nodo]
        for i in range(self.num_nodi):
            if self.__mask[row, i]:
                lista.append(self.indici[i])
        return lista

    def adiacenti_pesati(self, nodo):
        lista = list()
        row = self.nodi[nodo]
        for i in range(self.num_nodi):
            if self.__mask[row, i]:
                lista.append([self.indici[i], self._matrice[row, i]])
        return lista

    def allNodes(self):
        return self.nodi.keys()
'''

    @property
    def nodi(self):
        return tuple(self.nodi)
    @property
    def indici(self):
        return tuple(self.indici)
    @property
    def num_nodi(self):
            return self.num_nodi




# crea i nodi
nodo0 = nodo_grafo(0)
nodo1 = nodo_grafo(1)
nodo2 = nodo_grafo(2)
nodo3 = nodo_grafo(3)
nodo4 = nodo_grafo(4)
nodo5 = nodo_grafo(5)
nodo6 = nodo_grafo(6)

grafo = grafo

# stampa tutti i nodi adiacenti a un nodo dato

#grafo non orientato
nodo0.connetti([nodo2, nodo1])
nodo1.connetti([nodo3, nodo4, nodo0])
nodo2.connetti([nodo3, nodo5, nodo0])
nodo3.connetti([nodo6, nodo5, nodo1, nodo4, nodo2])
nodo4.connetti([nodo3, nodo1])
nodo5.connetti([nodo3, nodo2])
nodo6.connetti([nodo3])

print(nodo0.adiacenti())

'''