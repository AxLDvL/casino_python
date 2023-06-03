Le but de ce programme est de créer un mini casino avec 2 jeux : une machine a sous et une roulette. Un tableau des scores est tenu dans un fichier score.txt

1. (3pts) Lors de début de la partie le tableau des scores est affiché. Les scores sont enregistré dans le fichier score.txt. La première ligne enregistre l'utilisateur qui a le plus d'argent. La dernière celui qui en as le moins. (Le cas d'égalité ne sera pas traité et laissé sur un ordre arbitraire). Une ligne est constituée du nom et de son argent, séparé par un ';'.
ex: Gressier;999

2. (3pts) Un utilisateur est défini par son nom et son argent. Il ne peut pas avoir moins de 0€. Il doit être représenté par une classe dans un fichier a part.

3. (3pts) Ensuite, l'utilisateur doit pouvoir entrer son nom. Si son nom n'est pas dans le fichier score.txt 100€ lui son donné.

4. (3 pts) Un menu lui demande s'il veut utiliser la machine a sous (choix 1) ou la roulette (choix 2) ou quitter (choix q). S'il entre une autre valeur, redemander.

5. (3 pts) S'il choisi quitter, afficher le tableau à jour et sauvegarder le nouveau tableau dans le fichier score.txt pour une prochaine partie.

6. (3 pts) Créer une classe jeu qui contient un attribut 'nom_du_jeu'. Cette attribué est initialisé par le constructeur. ( ex flechette =
Jeu("Flechette") ). Cette classe doit être dans le fichier 'jeu.py' lui même dans le dossier 'jeux' (ainsi le chemin relatif est : ./jeux/jeu.py). La classe Jeu possède une méthode "bienvenue()" qui affiche "Bienvenu dans [nom du jeu]"

7. (3 pts) Créer une classe MachineASous qui hérite de Jeu. MachineASous définie automatiquement le nom du jeu a "Machine à sous". Si l'utilisateur a  choisi 1 au menu défini au point 4, le message de bienvenu est affiché (via la méthode hérité de jeu). Puis le jeu est lancé via la méthode run (machine_a_sous.run(user)). l'utilisateur peut choisir de jouer 1€ (via la touche 1) ou quitter (via la touche q). En cas de mauvaise entrée, on redemande la saisie. S'il quitte, l'utilisateur revient au menu défini au point 4.

8. (3 pts) Si 1€ est joué, il perd 1€. La machine a sous tire au hasard alors 3 chiffres entre 1 et 6 compris. Si les 3 chiffres sont identiques, il gagne 500€, sinon il ne gagne rien. De nouveau il peut choisir entre jouer 1€ ou quitter

9. (3 pts) Créer une classe Roulette qui hérite de Jeu. Roulette définie automatiquement le nom du jeu a "Roulette". Si l'utilisateur a choisi 2 au menu défini au point 4, le message de bienvenu est affiché (via la méthode hérité de jeu). Puis le jeu est lancé via la méthode run (roulette.run(user)). L'utilisateur peut choisir de jouer une somme (doit être un nombre (contrôle 1) positif (contrôle 2) et il doit posséder l'argent joué (contrôle 3)) ou quitter (via touche q). En cas de mauvaise entrée, on redemande la saisie. S'il quitte, l'utilisateur revient au menu défini au point 4.

10. (3 pts) Une fois la somme joué, il doit choisir un numéro entre 0 et 49 compris. La roulette tire un numéro au hasard entre 0 et 49. Si le numéro tire est celui choisi par l'utilisateur, il reçoit 3 fois la somme misée (âpres l'avoir donnée a la roulette). Si le numéro choisi par l'utilisateur est paire et que la roulette tire un paire, il récupère seulement 50% de sa somme initial. De même si le numéro de l'utilisateur est impaire  et celui de la roulette est impaire. Dans le cas où le numéro de l'utilisateur est  paire mais pas la roulette (ou inversement) alors l'utilisateur ne reçoit rien. L'utilisateur peut de nouveau choisir de rejouer une somme ou quitter etc.

================

11 bonus (3 pts) Ajouter un mot de passe a l'étape 2, via getpass et stocker le mot de passe en sha512 dans score. Si l'utilisateur existe mais le  mdp n'est pas bon, c'est la fin du programme avec erreur custom. Si le mdp est bon le programme continue. Si l'utilisateur n'existe pas, le programme continue et enregistre le sha du mdp pour le sauvegarder a la fin (classe User probablement à modifier)
# casino_python
