# Basi di Markdown

## Titoli

I titoli vengono indicati con una serie di #. Tanti più ## abbiamo, tanto meno sono importanti e messi in risalto i titoli che creiamo.\
Di fatto i # determinano i paragrafi del nostro testo, quindi se dopo un titolo con ## ne creo uno con ###, il secondo sarà un sottoparagrafo di quello precedente.

Buona pratica è semore quella di mettere una linea vuota prima e dopo i titoli in maniera da evidenziare dove questi siano.

## Paragrafi

I paragrafi vengono definiti da del testo compreso fra due linee vuote.<br>
Se si vuole andare a capo senza creare per forza un altro paragrafo, ci sono molti comandi differenti a seconda dell'editor che stiamo utilizzando. <br> 
Un metodo è mettere due spazi alla fine della frase dove vogliamo andare a capo. il problema è che è difficile riconoscere dove siano gli spazi, quindi è preferibile inserire **\<br>** che viene supportato da tutti gli editor che gestiscono anche HTML. Altrimenti possiamo usare \ alla fine della frase, ma non è riconosciuto da tutti gli editor.

## Enfasi

Possiamo dare enfasi alle nostre frasi usando l'*italico* e il **grassetto**. Questo viene fatto aggiungendo semplicemente un asterisco \* alla fine e all'inizio del testo che vogliamo enfatizzare per creare l'*italico*. Per il grassetto useremo due \*\* all'inizio e alla fine.

Attenzione a non usare il grassetto per identificare l'inizio di paragrafi. Questo ridurrebbe l'utilità e la navigabilità del nostro testo.

## Elenchi

### Elenchi puntati

Semplicemente anteponiamo un -, + o * all'inizio di ogni punto del nostro elenco.

### Elenchi numerati

Come negli elenchi puntati, anteponiamo ai vari elementi un numero seguito da un punto; ad esempio 1.

## Link e Immagini

Per aggiungere i link messiamo tra quadre il testo a cui vogliamo legare il link e fra tonde il link vero e proprio.<br>

Similmente faremo con le immagini, ma qui anteponiamo un ! al testo.

## Blocchi di codice

Possiamo anche aggiungere facilmente dei blocchi di codice al nostro testo. Potrebbe essere codice in-line `int f = 0;` aggiungendo prima e dopo il codice il carattere backtick. In alcuni sistemi operativi viene inserito con `alt Gr + '` in altri (come windows) lo si inserisce con `alt + 96`.

Se dobbiamo inserire dei blocchi di codie più lunghi possiamo inserire tre backtick all'inizio e alla fine del codice.

```python
while true:
    print("that's so wired code")
```

Accanto alla prima riga di backtick possiamo inserire anche il nome del linguaggio di programmazione che viene utilizzato in maniera che venga formattato in una maniera consona.

## Matematica

Se dovessimo inserire delle formule matematiche all'interno del nostro testo, possiamo usare \$ all'inizio e alla fine della nostra espressione. Questo ci permette di usare una notazione [latex](https://www.latex-project.org/get/) all'interno del testo.

## Conclusioni

[Markdown](https://www.markdownguide.org/) è definibile un linguaggio di programmazione di testo come lo sono HTML, XML, LaTeX e molti altri. La comodità principale di questi metodi è che il testo viene salvato in un semplicissimo file di testo che quindi può essere interpretato facilmente da quasi tutte le macchine e le persone.

Oltre a questo, c'è da dire che comunque è qualcosa che viene usata soltanto dalle nicchie, è difficile da interpretare e molto meno versatie di altri editor di testo come Word, google document e altri più potenti. 

Infatti viene utilizzato molto poco. Di seguito alcuni sparuti esempi:<br>
![tele](telegram.png)
![chat](chat.png)
![what](what.jpeg)
![git](git.png)
