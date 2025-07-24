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

### Commenti - PEP 257

Fare commenti di senso compiuto, quindi con frasi complete e relative al codice che si sta scrivendo.<br> 
Ogni frase deve cominciare con la lettera maiuscola. <br>
La lingua ufficiale di python è l'inglese. Se il nostro codice potrebbe venir letto da persone che parlano una ligua differente dalla nostra, dobbiamo commentare in inglese e non nella nostra lingua madre.

Nel caso dei commenti inline, evitare commenti ovvi e separare il commento dal codice con almeno due spazi.

Per andare in contro alla documentazione, definiamo i commenti tra """triple doppie virgolette""". Questi commenti potranno essere presi dai software di documentazione per creare la documentazione del nostro codice. 

### Nomi

È utile riconoscere i diversi stili di nomenclatura:

- Lettera singola minuscola (es. b)
- Lettera singola maiuscola (es. B)
- minuscolo (es. lowercase)
- minuscolo_con_underscore (es. lower_case_with_underscores)
- MAIUSCOLO (es. UPPERCASE)
- MAIUSCOLO_CON_UNDERSCORE (es. UPPER_CASE_WITH_UNDERSCORES)
- CapWords (o CamelCase, StudlyCaps). Quando si usano acronimi in CapWords, maiuscole tutte le lettere dell'acronimo (es. HTTPServerError è preferibile a HttpServerError)
- mixedCase (differisce da CapWords per il carattere iniziale minuscolo)
- Capitalized_Words_With_Underscores (considerato "brutto")
- Prefisso breve e unico per raggruppare nomi correlati (es. st_mode in os.stat(), raro in Python)

#### Forme Speciali con Underscore

Queste possono essere combinate con qualsiasi convenzione di caso:

- **`_singolo_underscore_iniziale`**: un debole indicatore di "uso interno". Gli oggetti con nomi che iniziano con un underscore non vengono importati da `from M import *`.
- **`singolo_underscore_finale_`**: utilizzato per convenzione per **evitare conflitti con parole chiave riservate di Python** (es. `class_` è meglio di `clss`).
- **`__doppio_underscore_iniziale`**: quando si denomina un attributo di classe, **invoca il "name mangling"** (all'interno della classe `FooBar`, `__boo` diventa `_FooBar__boo`). Questo è usato per evitare conflitti di nome con attributi nelle classi progettate per essere sottoclassate.
- **`__doppio_underscore_iniziale_e_finale__`**: per oggetti o attributi "magici" (es. `__init__`, `__import__`). **Non inventare mai tali nomi**, usarli solo come documentato.

#### Nomi da Evitare

**Non usare mai i caratteri 'l' (elle minuscola), 'O' (o maiuscola) o 'I' (i maiuscola) come nomi di variabili a singolo carattere**. In alcuni font, sono indistinguibili dai numeri uno e zero. Invece di 'l', usare 'L'. (Anche il "Clean Code" sconsiglia l'uso di 'l' e 'O' per la disinformazione, e suggerisce che i nomi a lettera singola vadano usati solo per contatori di cicli in scope molto piccoli).

#### Convenzioni di Denominazione (Prescrittive)

**Nomi di Pacchetto e Modulo**:

- Dovrebbero essere **brevi, tutti in minuscolo**.
- Gli underscore possono essere usati nei nomi dei moduli se migliorano la leggibilità, ma sono sconsigliati nei nomi dei pacchetti.
- I moduli di estensione scritti in C o C++ con un modulo Python di livello superiore dovrebbero avere un **underscore iniziale** (es. `_socket`).

**Nomi di Classe**:

- Normalmente dovrebbero usare la convenzione **`CapWords`**.
- La convenzione di denominazione delle funzioni può essere usata se l'interfaccia è documentata e usata principalmente come `callable`.

**Nomi di Variabili di Tipo (PEP 484)**:

- Normalmente **`CapWords`**, preferendo nomi brevi (es. `T`, `AnyStr`, `Num`).
- Si raccomanda di aggiungere i suffissi `_co` o `_contra` per variabili covarianti o contravarianti.

**Nomi di Eccezione**:

- Seguono la convenzione di denominazione delle classi (`CapWords`).
- Dovrebbero usare il **suffisso "Error"** se l'eccezione è effettivamente un errore.

**Nomi di Variabili Globali**:

- Le convenzioni sono **simili a quelle delle funzioni** (minuscolo con underscore).
- Nei moduli progettati per `from M import *`, usare il meccanismo `__all__` o prefissare con un underscore per impedire l'esportazione.

**Nomi di Funzioni e Variabili**:

- Dovrebbero essere **minuscoli, con parole separate da underscore** se necessario per migliorare la leggibilità.
- `mixedCase` è consentito solo in contesti in cui è già lo stile prevalente (per compatibilità con le versioni precedenti).
- ("Clean Code" sottolinea l'importanza di nomi che rivelano l'intenzione, evitano la disinformazione, rendono le distinzioni significative, sono pronunciabili e ricercabili, e non usano codifiche. Inoltre, suggerisce l'uso di verbi per i nomi dei metodi).

**Argomenti di Funzioni e Metodi**:

- Usare **`self`** per il primo argomento dei metodi di istanza.
- Usare **`cls`** per il primo argomento dei metodi di classe.
- Se il nome di un argomento si scontra con una parola chiave riservata, è meglio **aggiungere un singolo underscore finale** (es. `class_`).

**Nomi di Metodi e Variabili di Istanza**:

- Seguire le regole di denominazione delle funzioni (minuscolo con underscore).
- Usare un **singolo underscore iniziale per metodi e variabili di istanza non pubblici**.
- Usare **due underscore iniziali** (`__`) per invocare le regole di "name mangling" di Python e prevenire collisioni di nomi con le sottoclassi.

**Costanti**:

- Di solito definite a livello di modulo e scritte **tutte in maiuscolo con underscore** per separare le parole (es. `MAX_OVERFLOW`, `TOTAL`).
- ("Clean Code" concorda sull'uso di costanti con nomi descrittivi al posto di "numeri magici").

#### Progettazione per l'Ereditarietà

Decidere se i metodi e le variabili di istanza ("attributi") devono essere **pubblici o non pubblici**. **In caso di dubbio, scegliere non pubblico**. È più facile rendere un attributo pubblico in seguito che il contrario.

- **Attributi pubblici**: sono quelli che ci si aspetta siano usati da clienti non correlati, con un impegno a evitare modifiche incompatibili con le versioni precedenti.
- **Attributi non pubblici**: non sono destinati all'uso da parte di terzi e non ci sono garanzie che non cambieranno o vengano rimossi.
- Python non ha attributi veramente "privati" senza un lavoro extra.
- Esiste una categoria di attributi che fanno parte dell'"API di sottoclasse" (spesso chiamati "protetti" in altri linguaggi); per questi, è necessario prendere decisioni esplicite.

Le linee guida Pythonic per gli attributi:

- **Gli attributi pubblici non devono avere underscore iniziali**. Se c'è una collisione con una parola chiave riservata, aggiungere un underscore finale.
- Per **attributi di dati pubblici semplici**, è meglio esporre solo il nome dell'attributo. Se in futuro l'attributo dovesse necessitare di un comportamento funzionale, usare le **`properties`** per nascondere l'implementazione funzionale dietro la sintassi di accesso semplice. Evitare `properties` per operazioni computazionalmente costose.
- Se la classe è destinata a essere sottoclassata e si hanno attributi che non si desidera che le sottoclassi utilizzino, considerare di denominarli con **due underscore iniziali** (`__`) per attivare il "name mangling".

#### Interfacce Pubbliche e Interne

Le garanzie di retrocompatibilità si applicano **solo alle interfacce pubbliche**.

- **Le interfacce documentate sono considerate pubbliche**, a meno che la documentazione non le dichiari esplicitamente provvisorie o interne.
- **Tutte le interfacce non documentate devono essere considerate interne**.
- I moduli dovrebbero dichiarare esplicitamente i nomi nella loro API pubblica usando l'attributo **`__all__`**. Un `__all__` vuoto indica nessuna API pubblica.
- Anche con `__all__` impostato, le **interfacce interne** (pacchetti, moduli, classi, funzioni, attributi) dovrebbero comunque essere **prefissate con un singolo underscore iniziale** (`_`).
- Un'interfaccia è considerata interna se qualsiasi namespace contenente è interno.
- **I nomi importati devono essere sempre considerati un dettaglio di implementazione**; non fare affidamento sull'accesso indiretto a meno che non siano esplicitamente documentati come parte dell'API del modulo contenitore.

In sintesi, la denominazione in Python ruota attorno alla **chiarezza**, alla **leggibilità** e alla **comunicazione dell'intento**, con particolare attenzione alla distinzione tra ciò che è pubblico e ciò che è interno, simile a come un artigiano etichetta con precisione ogni attrezzo nel suo laboratorio: quelli di uso comune sono chiaramente visibili e comprensibili a tutti, mentre gli strumenti speciali o interni al suo processo lavorativo sono contrassegnati in modo da non creare confusione a chi non è direttamente coinvolto nella manutenzione o nello sviluppo.
