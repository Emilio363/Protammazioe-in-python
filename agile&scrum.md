# AGILE
un manifesto che da un idea di come sviluppare software

## SCRUM
vogiamo avere un lavoro di team compatto e indipendente
genera soluzione adattive a problemi complessi


lo sviluppo software comprende:
l'amdiente di sviluppo deve sopperire molti compiti
 - creazione del codice sorgente
 - verificare il funzionamento di una serie di test
 - confezionare l'applicazione
- e molti altri

le tasks sono: 
- ripetitive
- devono essre veloci
- funzionare su diverse macchine
- automatizzato

l'automatizzaione della struttura è il processo di automatizzare la creazione di un software e i processi associati.

questo processo ci porta ad:
- accellerare la compilazione e i processi associati
- eliminare le rindondanze
- salvare tempo
- minimizzare le strutture mal costruite

## Version Control

parliamo di version control nel momento in cui abbiamo più versioni dello stesso software.
anche quando vogliamo avere controllo sulle varie modifiche che vengono fatte da diversi sviluppatori allo stesso progetto.
vogliamo quindi integrare i vari cambiamenti del codice.

come ci si può aspettare è molto complicato

### Version Control System (VSC)

ci permettono di tenere traccia dei vari cambiamenti che vengono fatti al codice

ne abbiamo di * tipo:

#### VSC centralizzati

sono centralizzati, quindi gli amministratori posso controllare gli accessi, abbiamo un unico luogo di raccolta dei dati per evitare discordanze.

pro:

- molto controllo sulle versioni
- poca discordanza

contro:

- dobbiamo avere del codice molto aggiornato fra i vari developers (difficile lavorare tutti assieme)
- se salta qualcosa nel centrale xe cazzi

#### VSC distribuiti

ogni utente non ha soltanto una copia del codice relativo a una versione ma copia l'intera repository, compresa tutta la storia

pro:

- modifica del codice più rapida per gli sviluppatori
- aggiornamento dei file locali molto più rapido perché incrementale
- le copie funzionano anche da backup

contro:

- comunicazione solo quando il codice viene messo in condivisione
- asincronia delle varie versioni

### Git

uno dei migliori VCS in circolazione.

consideriamo tre luoghi fondamentalmente:

- **La tua working directory:** la cartella fisica del tuo computer dove stai lavorando
- **Staging area:** nel momento in cui vogliamo pubblicare delle modifiche al nostro codice, mandiamo il codice a git e lui lo tiene da parte per capire se le modifiche sono valide
- **.git directory:** il luogo fisico dove viene salvato tutto il codice di un progetto.

Di conseguenza possiamo avere tre stati dei file:

- **Modificato:** l'abbiamo modificato sul nostro computer ma ancora nessuno lo sa
- **Staged:** è nella fase di staging e si prepara per il prossimo snapshot del progetto
- **Commited:** il file fa parte per intero del progetto

#### .gitignore

non tutto quello che abbiamo all'interno della nostra directory serve che sia salvato da git. molti dei file, ad esempio file compilati per la nostra macchina oppure specifiche del nostro ambiente di sviluppo, sono specifici per l'utilizzo privato di ogni utente. Possiamo segnalare i file che vogliamo che siano ignorati nel momento in cui mandiamo il codice.

## GitHub

branches

la prima cosa da fare è creare un progetto. può essere pubblico o privato.
se vogliamo dei collaboratori dobbiamo abilitarli manualmente. qui possiamo vedere tutti i file e cartelle che compongono il nostro progetto, la nostra repo.

fetch
push
pull
commit

reset to commit: riporta la repository a un commit precedente
merge di un ramo:

git clone "url": ci permette di copiare l'intero progetto di git in una nuova cartella salvata nella nostra path attuale

git init: crea una repo github all'interno della nostra cartella

git status: ci torna alcune informazioni su quala branch sia il padre dei file che abbiamo scaricato

git add "file": aggingi un determiato file al prossimo commit che andrà fatto. attenzione che le modifiche successive al file non saranno salvate nel commit.

git add . : aggiunge tutti i file della cartella al prossimo commit

git commit -m "titolo del commit" [-m "eventuale descrizione"]

git log : ci mostra tutti i commit che sono stati fatti su quel branch

git checkout -b "nome branch": mi permette di creare un altro branch con il codice che ho salvato all'interno della mia directory.

git checkout "nome branch": ci carica all'interno della repo il codice di uno specifico branch

git merge "nome brach": fa il merge tra il branch in cui siamo e quello specificato

git reset: pulisce tutti il commit da tutte le modifiche che sono state caricate

git reset "hash": ci permette di riprisinare il commit con l'hash dato

git remote add origin "url":  lega l'origine del mio codice a una specifica repo

git push origin dev: mando il mio codice online

**Good practice:** prima di committare controllare lo stato in maniera da assicurarsi di aver salvato tutte le modifiche.

fare dei titoli e descrizioni molto esplicativi per capire cosa è stato fatto in quel momento

gitkraken
github desktop
