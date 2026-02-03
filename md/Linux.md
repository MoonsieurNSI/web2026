## 1. Système d'exploitation


> Un système d’exploitation (SE) est un programme (ou un ensemble de programmes) qui assure la communication
entre le matériel (hardware) et les logiciels (software).

=> operating system (OS)

-----------------
>  ℹ️ **Note** Principaux OS
>
>   - **Windows** Microsoft
>   - **MacOS** Apple
>   - **Unix** Solaris
>   - **ChromeOs** Google
>   - **Android** Google
>   - **IOS** Apple
>   - **FreeBSD**
>   - **Gnu/Linux**
-----------------

Les 6 premiers sont des logiciels propriétaires tandis que les deux derniers sont **libres**.

A l'exception de **Windows**, tous ces OS appartiennent à la famille *Unix-Like* : les commandes sont standardisées.


Rem:
> « First, the freedom to copy a program and redistribute it to your neighbours, so that they can use
it as well as you. Second, the freedom to change a program, so that you can control it instead of it
controlling you ; for this, the source code must be made available to you » (Richard Stallman, Free Software Fundation)


Quelques exemples de logiciels libres : Linux, Python, FireFox, LibreOffice, Gimp, OBS Studio,...

## 2. Le père de tous les OS : UNIX

Il est developpé en **1971/1972** par K.thompson et D.Ritchie. Ils ont inventé **le langage C** pour écrire leur OS appelé UNIX.

Cet OS est célèbre pour son interpètre de commande appelé *Terminal* ou *Shell*.


En 1991, un étudiant finlandais **Linus Torvald** envoie un mail avec une pièce jointe contenant le noyau d'un système d'expoloitation libre inspiré d'UNIX : **Linux**.


## 3. Quelques commandes dans le shell (bash):

Une commande s'écrit après le prompt qui se termine par le symbole `$`.

Une commande possède toujours une syntaxe:
- `nom` de la commande
- `options` facultatives
- `arguments` facultatifs

Il existe un commande qui affiche le manuel/ la documentation d'une autre commande passée en argument : `man`

Syntaxe générale:    `nom --option argument` ou `nom -option argument`

|nom|rôle|exemple|
|----|----|----|
|`whoami`|affiche le nom de l'utilisateur|`$ whoami`|
|`man`|affiche le manuel d'une autre commande|`$ man whoami`|
|`touch`|créer un fichier *vide*|`$ touch monfichier`|
|`ls`|liste le contenu d'un dossier|`$ ls -l`|
|`mkdir`|créer un dossier *vide*|`$ mkdir monDossier`|
|`nano`|éditer un fichier|`$ nano monfichier`|
|`cat`|affiche le contenu des fichiers |`$ cat monfichier`|
|`tree`|affiche l'arborescence du dossier courant `./` |`$ tree`|
|`pwd`|affiche le nom du dossier courant |`$ pwd`|
|`cd`|changer de répertoire courant |`$ cd ./mondossier`|
|`cp`|copier une source vers une destination|`$ cp ./monfichier ./mondossier`|
|`rm`|supprimer des fichiers ou des dossiers|`$ rm -r ./mondossier`|
|`mv`|couper/renommer des fichiers|`$ mv ./monfichier ./nouveauNom`|
|`chmod`|modifie les permissions|`$ chmod 777 ./monFichier`|
|`head`|affiche les premières lignes d'un fichier|`$ head -n 4 ./monFichier`|
|`tail`|affiche les dernières lignes d'un fichier|`$ tail -n 4 ./monFichier`|
|`grep`|recherche une chaîne de caractère|`$ grep chaine ./monFichier`|
|`echo`|retourne une chaîne de caractère (par défaut sur le terminal)|`$ echo "chaine"`|
----------
Pour éditer un fichier plusieurs commandes/éditeurs sont possibles :
- `nano` (dans ce cours)
- `vi`
- `emacs`

----------------
La commande `cd`(*change directory*) permet de se déplacer dans l'arboresence des
dossiers. Sur Linux, le dossier **racine** (*root*) se note `/`.

On peut donner le chemin vers un dossier (un fichier) de manière:
- relative (on commence par `./` ou `../`)
- absolue (on commence par `/`)

Linux rend facultatif l'utilisation de `./`.

Si on tape la commande `cd` sans argument, on se déplace dans le répertoire "home".
=> `/home/utilisateur`

-------------------

La commande `cp`permet de copier une source vers une destination en la renommant
éventuellement.

```bash
$ cp cheminFichierSource cheminDossierDestination
```
en renommant

```bash
$ cp cheminFichierSource cheminDossierDestination/nouveauNom
```

-------------
La commande `rm -r` permet de supprimer un dossier et tout son contenu

--------------
Il est possible d'écrire des commandes dans un fichier portant l'extension `.sh`
par défaut. Pour exécuter ce fichier,

```bash
./monFichier.sh
```

Par défaut, les fichiers linux ne sont pas exécutables. Quand un fichier (un dossier) est crée, il possède des **permissions** qui peuvent être différentes pour:
- `user` c'est le propriétaire
- `group` c'est un groupe d'utilisateur défini par `user`
- `other` le reste du monde

Les permissions sur un fichier(un dossier) sont:
- *read* : `r` valeur 4
- *write* : `w` valeur 2
- *execute* : `x` valeur 1

La commande `chmod nnn` permet de modifier les permissions ; il existe une autre synatxe avec les lettres `u,g,o` (user, group, other) et les symboles `+, -` pour
ajouter ou retirer des droits.

```bash
chmod 754 ./monFichier.sh   # rwx pour user, rx pour group, r pour other
```

```bash
chmod u-x,g-x,o+w ./monFichier.sh   # retire x pour user et group, ajoute w pour other
```

---------------
L'opérateur `>` ou `>>` permet de rediriger la sortie vers un fichier ; si le fichier n'existe pas alors
il est crée.
```bash
commande > fichier
```

Le signe `>>` permet de ne pas écraser le contenu du fichier. Il est fréquent d'utiliser `echo` avec l'option
`-e` pour remplir un fichier.

```bash
echo -e "code en python
.....
...." > fichier.py
```

La commande `python` suivie du chemin vers un fichier `.py` exécute le code python.

# Ex1
[https://codex.forge.apps.education.fr/exercices/course_cycliste/](https://codex.forge.apps.education.fr/exercices/course_cycliste/)

# Ex 2
[https://codex.forge.apps.education.fr/exercices/syracuse/](https://codex.forge.apps.education.fr/exercices/syracuse/)

# Ex 3
[https://codex.forge.apps.education.fr/exercices/derniere_occurrence/](https://codex.forge.apps.education.fr/exercices/derniere_occurrence/)