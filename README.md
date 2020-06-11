![](https://github.com/ohanqo/novi/blob/master/docs/article.jpg)

<br>

<p align="center">
    Web App permettant le partage de connaissances via des articles
    <br />  
    Réalisé avec Django, Tailwind et VueJS
    <br />  
    Basé sur le site Medium
    <br />
    http://anqo.eu.pythonanywhere.com/
</p>

<br>

## Prérequis

- Python 3

## Installation

Téléchargement du projet dans le dossier courant

```
$ git clone https://github.com/ohanqo/novi
```

Déplacement vers le projet

```
$ cd novi
```

Création d'un environnement virtuel pour le projet

```
$ python3 -m venv .venv
```

Activation de l'environnement virtuel

```
$ source .venv/bin/activate
```

Éxécution des migrations

```
$ python3 manage.py migrate
```

Lancement du serveur

```
$ python3 manage.py runserver
```

## À propos

Novi est un site web visant à partager des articles sur le monde de la tech. Il s'adresse aux développeurs, designers, chef de projets, analystes, graphistes, etc. Une fois sur le site, un visiteur peut visualiser tous les articles et peut naviguer parmi les profils des auteurs. Ce sont les uniques actions qu'un utilisateur non authentifié peut effectuer.

Pour rédiger un article et suivre une personne, il faut au préalable avoir créé un compte. Une fois cette action effectuée, l'utilisateur est redirigé sur la page d'accueil contenant les derniers articles parus.

![](https://github.com/ohanqo/novi/blob/master/docs/home.jpg)

<br>

L'utilisateur peut se rendre sur son profil et compléter ce dernier. Il peut ajouter une biographie ainsi qu'un lien vers un avatar le représentant. Lorsqu'il accède à un profil d'une autre personne, il peut visualiser les informations de ce dernier, la liste de ses articles et il peut la suivre en cliquant sur le bouton follow.

![](https://github.com/ohanqo/novi/blob/master/docs/profile.jpg)

<br>

La rédaction d'un article s'effectue en cliquant sur le bouton `Write an article` présent dans la barre de navigation. Cette page comporte trois champs qui sont obligatoires: titre, image et texte. Le titre doit être unique parmi la liste de tous les articles, car il permet de générer un slug, ce qui augmente le référencement. Une fois l'article crée, il se retrouve directement en premier sur la page d'accueil.

## Choix techniques

![](https://github.com/ohanqo/novi/blob/master/docs/diagram.png)

<br>

Le projet se base sur la classe `User` fournie par le module d'authentification de Django. Cela permet de pouvoir facilement écrire le code d'inscription, connexion et déconnexion. La classe `Profile` dispose d'une relation <i>one to one</i> avec la classe `User`, ce qui implique que pour chaque inscription d'un utilisateur, un profil lui est automatiquement assigné.

La classe `Profile` est l'élément central. Elle permet d'obtenir les informations comme la liste des articles rédigés par l'utilisateur, la liste de ses favoris, ses followers etc. Cette classe dispose de deux attributs qui sont la biographie et l'avatar. Le fait d'étendre de la classe `User` permet l'ajout de nouveaux attributs plus facilement sans pour autant compromettre le système d'authentification.

Les technologies utilisés en plus de Django sont Tailwind et VueJS:

- Tailwind est un framework CSS centré autour du principe d’utilitaire, facilement et hautement modifiable. Il permet de créer des designs complètement personnalisés sans jamais quitter la page HTML.
- VueJS est une libraire JavaScript qui s'intègre parfaitement à tous type de projet et permet de créer facilement de l'intéraction dynamique sur une page.
