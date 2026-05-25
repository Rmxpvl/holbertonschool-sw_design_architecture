# Design Patterns

Ce dossier regroupe plusieurs exercices sur les principaux patrons de conception en Python. L'objectif est de comprendre comment découpler les responsabilités, réduire les dépendances entre objets et rendre le code plus facile à étendre.

## But du projet

Le projet illustre trois familles de design patterns très courantes :

- `Factory` pour centraliser la création d'objets.
- `Observer` pour notifier plusieurs abonnés à partir d'une source d'événements.
- `Decorator` pour ajouter des comportements dynamiquement sans multiplier les classes.

Chaque fichier du dossier `design_patterns` met en pratique un pattern précis à travers un petit exemple autonome.

## Fichiers du projet

- `0-factory.py` : implémentation d'une factory basée sur un registre.
- `1-observer.py` : implémentation d'un sujet qui notifie plusieurs observateurs.
- `2-decorator.py` : implémentation d'un objet de base enrichi par des décorateurs.

## Ce que chaque pattern apporte

### Factory

La factory cache la logique de création derrière une interface simple. Au lieu d'écrire plusieurs instanciations directes dans le code, on demande à la factory de créer l'objet demandé à partir d'une clé.

Avantages :

- centralise la création des objets ;
- facilite l'ajout de nouveaux types ;
- réduit les conditions dispersées dans le code.

### Observer

L'observer permet à un sujet de prévenir automatiquement plusieurs observateurs lorsqu'un événement se produit. Le sujet ne connaît pas les détails des abonnés, il diffuse seulement les informations.

Avantages :

- découple l'émetteur des récepteurs ;
- permet d'ajouter ou de retirer des abonnés facilement ;
- simplifie la gestion des événements.

### Decorator

Le décorateur permet de composer des comportements supplémentaires autour d'un objet existant. Chaque décorateur encapsule l'objet d'origine et modifie ou enrichit son comportement.

Avantages :

- évite la multiplication de sous-classes ;
- rend les combinaisons de comportements flexibles ;
- permet d'ajouter une fonctionnalité sans modifier les classes de base.

## Objectif pédagogique

L'objectif n'est pas seulement de faire fonctionner le code, mais de reconnaître quand utiliser chaque pattern et pourquoi il améliore la structure d'un programme. Ces exercices servent à pratiquer :

- la composition plutôt que l'héritage excessif ;
- la séparation des responsabilités ;
- l'extensibilité du code ;
- la lisibilité des implémentations orientées objet.

## Comment exécuter

Chaque fichier peut être lancé indépendamment avec Python 3 :

```bash
python3 0-factory.py
python3 1-observer.py
python3 2-decorator.py
```

Selon le fichier, le script affiche une suite de sorties démontrant le comportement du pattern.

## Comment réussir le projet

- Lire attentivement le rôle de chaque classe avant de coder.
- Ne pas modifier la logique centrale quand l'énoncé demande d'étendre le comportement depuis l'extérieur.
- Tester chaque fichier séparément pour vérifier que la sortie correspond exactement à celle attendue.
- Garder les classes simples et focalisées sur une seule responsabilité.

## Résumé

Ce projet sert de base pour comprendre trois outils essentiels de conception orientée objet. Une bonne solution doit rester simple, extensible et fidèle au pattern demandé, sans ajouter de logique inutile dans les classes principales.
