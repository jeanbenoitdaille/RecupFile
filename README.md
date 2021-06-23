# RecupFile
Récupérer l'extesion d'un fichier 
Dans cet exercice, nous utilisons le module os, qui contient déjà des fonctions qui nous permettent de gérer ce genre de situations.

Depuis le module os, nous pouvons importer le module path, qui donne accès à tout un tas de fonctions permettant de manipuler des chemins.

La fonction splitext nous permet de séparer un chemin de son extension. Cette fonction nous retourne donc un tuple, qui contient le chemin sans l'extension en premier élément, et l'extension seule en deuxième élément :

    >>> import os
    >>> fichier = "C:/Python36/python.exe"
    >>> extension = os.path.splitext(fichier)[1]
    '.exe'

Pour récupérer l'extension sans le point, il ne nous reste qu'à utiliser la fonction strip :

    extension = extension.strip(".")
