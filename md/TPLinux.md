- Ouvrer un terminal puis afficher le répertoire courant
- Utiliser la commande `ls` sans option ni argument
- Créer un nouveau dossier nommé `Dossier1`
- Utiliser la commande `ls` sans option ni argument. Que remarquez-vous ?
- Déplacez-vous dans le répertoire `./Dossier1`
- Vérifier que vous êtes bien arrivé !
- Puis créer un fichier vide nommé `fic1.txt` dans ce dossier.
- Revenir dans le répertoire `/workspaces/web2026`
- Utiliser la commande `ls -F` . Que remarquez-vous ?
- Réaliser deux copies de `fic1.txt` :
    - `fic2.txt` dans le répertoire `./Dossier1`
    - `fic3.txt` dans le répertoire `/workspaces/web2026`
- Renommer le fichier `fic1.txt` en `fichierNSI` . Commenter.
- Utiliser la commande `tree` pour contrôler le résultat.
- Utiliser la commande `cd ../` puis `pwd` . Que remarquez-vous ?
- Supprimer le dossier `/workspaces/web2026/Dossier1` avec la commande `rmdir`. Commenter.
- Utiliser la commande `rm -ir /workspaces/web2026/Dossier1` . Répondez y(yes) ou n(no).
- Afficher une aide sur la commande `rm` . Quel est le rôle de l’option `-i` ?
- Créer les dossiers suivants :
    - `/workspaces/web2026/DA`
    - `/workspaces/web2026/DA/DB`
    - `/workspaces/web2026/DA/DC`
- Utiliser la commande `tree` pour contrôler.
-  Se déplacer dans le dossier `/workspaces/web2026/DA/DC` et vérifier que vous êtes bien arrivé !
-  Utiliser la commande `cd ../../` et commenter.
-  Ouvrir le fichier `fic3.txt` avec l’éditeur `nano`
- Ecrire 3 fois la ligne *"J’aime NSI"*, 2 fois la ligne *"J’aime bien lire aussi"* et 1 fois *"Bye"*
-  Appuyer sur <kbd>Ctrl</kbd>+<kbd>x</kbd> pour demander à quitter l’éditeur et valider avec la touche <kbd>y</kbd>
-  Afficher les 4 premières lignes de `fic3.txt`
-  Afficher les 3 dernières lignes de `fic3.txt`
-  Afficher le contenu du fichier dans la console.
-  Rechercher le mot *"aime"* dans le fichier `fic3.txt` et commenter.
-  Appliquer la commande `uniq` à `fic3.txt` et commenter.
- Appliquer la commande `sort` à `fic3.txt` et commenter.
- Afficher le nombre de lignes et de mots dans `fic3.txt`
- Afficher tous les fichiers et dossiers cachés du répertoire `/workspaces/web2026`


------------
## correction

- pwd
- ls
- mkdir ./Dossier1
- Dossier1 apparaît surligné en vert (comme tous les dossiers)
- cd ./Dossier1
- pwd
- touch ./fic1.txt
- cd ../ ou cd /workspaces/web2026
- l'option -F ajouter un slash après les dossiers
- cp ./Dossier1/fic1.txt ./Dossier1/fic2.txt  puis cp ./Dossier1/fic1.txt ./fic3.txt
- mv ./Dossier1/fic1.txt ./Dossier1/FichierNSI <br>
Les fichiers n'ont pas obligatoirement d'extension.
- tree
- On remonte un rang en arrière dans l'arborescence
- rmdir ne peut pas supprimer un dossier non vide
- rm -i pose une question y/n avant chaque supppression
- mkdir ./DA ./DA/DB ./DA/DC
- cd ./DA/DC puis pwd
- cd ../../ permet de remonter de 2 rangs
- head -n 4 ./fic3.txt
- tail -n 3 ./fic3.txt
- cat ./fic3.txt
- grep aime ./fic3.txt







