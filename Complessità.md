
# Complessità degli Algoritmi

### Breve compendio

## Introduzione

Non esiste alcun algoritmo che sia istantaneo. Tutti gli algoritmi che utilizziamo richedono del tempo di esecuzione, per quanto breve questo possa essere. Siccome le nostre risorse di tempo e di spazio sono limitate, vogliamo sapere quali algoritmi siano meglio performanti per i nostri scopi. Abbiamo quindi bisogno di un metro di misura per confrontare due algoritmi. Questo viene chiamato complessità dell'algoritmo.

Ci interessiamo alla complessità di un algoritmo sotto due punti di vista: la complessità spaziale e quella temporale.\
La **complessità spaziale** è quanto spazio usa l'algoritmo per eseguire, quindi quante celle di memoria vengono allocate per salvare valori di variabili, array, matrici... Siccome per ogni elemento che viene salvato in memoria, impieghiamo del tempo, la complessità temporale sarà necessariamente maggiore o uguale della complessità spaziale, quindi quest'ultima viene poco considerata.\
La **complessità temporale** ci da un indicazione di quanto tempo ci mette un algoritmo ad eseguire su una macchina. Ovviamente ogni computer è differente e alcuni sono più veloci altri più lenti. Per questo consideriamo una complessità assoluta e non relativa alla macchina. Ovviamente vanno fatte diverse assunzioni per rendere gli algoritmi paragonabili:

- consideriamo delle operazioni atomiche con uguale tempo di esecuzioni
- consideriamo il caso medio peggiore
- non consideramo ottimizzazioni che potrebbero essere fatte a livello di compilatore

## Notazione O-grande

Vogliamo classificare gli algoritmi in classi di complessità per valutare sostanziali differenze fra un metodo e un altro.

Partiamo dalla formulazione matematica della notazione O-grande:
$$
O(f(n))=^{def} \{g(n)\;|\; \exists c > 0\;, k>0\;\; \exists n_o>0\; |\; \forall m\geq n_0 \Rightarrow g(m)\leq c*f(m)+k\}
$$
Se volessmo tradurre la cosa in parole, potremmo dire che l'insieme $O(f(n))$ è composto da tutte le funzioni $g(n)$ che, trovate tre costanti $c,\;k$  e $n_0$, per ogni valore di $m$ maggiore di $n_0$ abbiamo che $g(m)$ è minore di $f(m)$ moltiplicato per la costante $c$ e aggiunta $k$.\
In altre parole, una funzione $g(n)$ appartiene alla classe $O(f(n))$ se da un certo punto in poi $f(n)$, moltiplicata per una qualsiasi costante e aggiunta un altra costante, riesce a stare sopra alla funzione $g(n)$

**Esempio:**\
Si considerino le funzioni $\frac{x^2}{x+2}+3$ e $x$.\
Possiamo dire che $\frac{x^2}{x+2}+3$ appartiene alla classe $O(x)$ $\left( \frac{x^2}{x+2}+3\in O(x)\right)$ perché $1.1*x \geq \frac{x^2}{x+2}+3$ per $x\geq 12.71$. Per esserne convinti possiamo rappresentare le due funzioni su un motore grafico come [desmos](https://www.desmos.com/calculator). In questo caso vediamo come sia necessario mettere la costante moltiplicativa 1.1 davanti a $x$ perché ci sia la maggiorazione.

Al fine delle nostre analisi di complessità non ci preoccupiamo delle due costanti perché queste dipenderanno poi dal tipo di implementazione che viene fatta e dalla macchina su cui gira il programma.

## Complessità Iterativa

Questa sezione esplora il calcolo della complessità per algoritmi di tipo iterativo.

### Operazioni atomiche

Le operazioni atomiche sono tutte quelle operazioni che assumiamo richiedano soltanto un istante di computazione.

Queste sono:

- le 4 perazio fondamentali fra numeri + * - /
- operazione di riferimento in memoria come l'inserimento in un array
- istruzione di controllo o condizioni booleane
- assegnamento (es. count = 0)

### Cicli

Nel momento in cui incontriamo un ciclo, come qualsiasi altro blocco di codice, occorre valutare quante volte viene ripetuto tale blocco. Quindi semplicemente moltiplicheremo la somma delle complessità delle istruzioni con 

### Chiamate di funzione

## Esempi di algorirmi

due esempi

## Complessità ricorsiva
