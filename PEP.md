# PEP Python Enhancemenet Proposal

author: Guido Von Rossum (olanda)

I pep sono una serie molto ampia di documenti che danno a volte delle linee guida, a volte dei limiti su come debba essere fatta una cosa.

Abbiamo 3 tipo di PEP:

- **Standard:** propongono vincoli sul linguaggio stesso
- **Infomational:** danno informazioni su varie sulle linee guida e sulle scelte di design.
- **Process:** danno delle indicazioni su come dovrebbero essere eseguiti processi che includono la creazione di codice, come la progettazione o la gestione della community.

## PEP 8 - Style Guide for Python Code

Deriva dalle linee guida dettate da Von Rossum e le estende in base ai cambiamenti del linguaggio.<br>

Ricordiamoci che il codice è letto molte più volte di quanto è scritto. Quindi il nostro obiettivo è di rendere il nostro codice il più possibile leggibile, anche violando le regole seguenti.

### Indentazione

Per quanto potremmo avevere degli editor che ci permettono di avere soltanto due spazi di indetazione per python, ci atteniamo sempre a 4 spazi.

Quando abbiamo delle linee di codice troppo lunghe, possiamo spezzarle su più righe in maniera da rendere il codice più accessibile. Nel caso di una assegnazione o funzioni con molti parametri, allineeremo la nuova riga con un indentazione maggiore dell'indentaione standard. ideale sarebbe allineare le nuove righe con l'inizio delle parentesi

```python
def long_function_name(var_one, var_two, var_three,
                       var_four):
    print(var_one)
```

Nel caso abbiamo degli if con condizioni complesse, dovremmo allineare le nuove righe con l'inizio della parentesi, ma in questa maniera avremmo un indentazione di 4 spazi (`if (`). Per non creare confunsione ulteriore, si sceglie di mettere un indentazione arbirtariamente maggiore. A sentimento.

quando andiamo a creare array molto lunghi o matrici, è bene mettere la parentesi di fine dichiarazione in una nuova riga. verrà allineata con la parentesi di inizio oppure con l'inizio del nome della variabile, a discrezione.

### Lunghezza delle righe

La lunghezza massima di una riga è di **79 caratteri**

Questo limite inizialmente era imposto per matchare con lo schermo standard, adesso viene imposto per riuscire a visionare correttamente il codice. Si prenda per esempio il marge fra diversi file della stessa repo che non fanno merge automatico. Per confrontarli dobbiamo aprire 3 finestre contemporanreamente, con i due codici sorgente e quello finale. Se abbiamo righe più lunghe di 79 caratteri potremmo non riuscire a leggere correttamente il codice che stiamo trattando.

In alcuni casi, in corcondanza con gli altri membri del team di sviluppo, possiamo estendere il limite a 100 caratteri.

### Operatori binari

Ricordiamo che gli operatori binari sono tutte quelle funzioni implicite che prendono due parametri; ad esempio somma, prodotto, modulo.

Per rendere più leggibile il codice siamo abituati a mettere uno spazio sia prima che dopo l'operatore. Questo potrebbe portare ad avere degli acapo subito dopo l'operatore in conformità con la regola di lunghezza delle righe. <br>
Adesso potremmo avere il problema di dover capire quale operatore viene appplicato a quale variabile. Per risolvere il problema andiamo a mettere l'operatore all'inizio della nuova riga.

```python
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

### Linee vuote

Usiamo due linee vuote per delimitare le classi e le funzioni al di fuori delle classi.<br>
All'interno delle classi una linea per delimitare i metodi, a meno che non siano metodi online che fanno circa le stesse cose. In questo caso possiamo anche omettere le linee di separazione.

## Module Level Dunder Names (da capire)

### Spazi

quando metterli:

- dopo le virgole
- prima e dopo opertatori binari
- prima e dopo le assegnazioni

quando **non** metterli:

- prima delle virgole
- dopo una partentesi aperti e prima di una parentesi chiusa
- fra il nome di una funzione e i suoi attributi
- mai metterne più di uno, fa casino

### Commenti

Fare commenti di senso compiuto, quindi con frasi complete e relative al codice che si sta scrivendo.<br> 
Ogni frase deve cominciare con la lettera maiuscola. <br>
La lingua ufficiale di python è l'inglese. Se il nostro codice potrebbe venir letto da persone che parlano una ligua differente dalla nostra, dobbiamo commentare in inglese e non nella nostra lingua madre.

Nel caso dei commenti inline, evitare commenti ovvi e separare il commento dal codice con almeno due spazi.

Per andare in contro alla documentazione, definiamo i commenti tra """triple doppie virgolette""". Questi commenti potranno essere presi dai software di documentazione per creare la documentazione del nostro codice. 