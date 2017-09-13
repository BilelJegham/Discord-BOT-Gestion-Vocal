Discord BOT
====

> Bot utilitaire permettant la gestion des canaux vocaux d'un serveur Discord : création, suppression, déplacement des membres,...

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Installation](#installation)
- [Commandes](#commandes)

<!-- /TOC -->

##  Installation
1. Installer les nécessaires :
    - Python 3 minimum
    - Différentes libraires listés dans `requirements.txt`
```bash
python3 -m pip install requirements.txt
```
2. Obtenir un token pour le BOT
    a. Créer une application sur https://discordapp.com/developers/applications/me
    b. Créer un bot
    c. Récupérer le **Token** du bot
    d. Incorporer le Token dans le fichier `config.py` à la place de `XXXXXX`
    ```py
apiBot = 'XXXXXX'
    ```
3. Exécuter le fichier `bot.py`
> **NOTE**  : un canal textuel logbot sera créé au 1er lancement du BOT, il affichera certaines opérations exécutées par le BOT



## Commandes
### Pour tous les membres du serveur

- `!move <channel-name>` : déplace le membre qui saisit la commande dans le canal vocal (uniquement pour les canaux vocaux crée via le bot)

### Seulement aux administrateurs
> Administrateur : membre disposant du rôle classé le plus haut dans la liste des rôles


- `!moveChannelTop <channel-name>` : déplace le canal vocal en haut de la liste (uniquement pour les canaux vocaux crée via le bot)
- `!create` : crée un canal vocal avec un nom aléatoire
- `!create <channel-name>` : crée un canal vocal avec le nom fournir
- `!delete <channel-name>` : Supprime le canal vocal (uniquement pour les canaux vocaux via le bot)
- `!delete ` : Supprime tous les canaux vocaux créent via le bot
- `!deleteAll` : Supprime tous les canaux vocaux sauf le canal vocal *General*


> Bilel JEGHAM : http://bilel.jegham.ml
