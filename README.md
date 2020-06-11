![](https://github.com/ohanqo/novi/blob/master/docs/article.png)

<br>

<p align="center">
    Web App permettant le partage de connaissances via des articles
    <br />  
    Réalisé avec Django, Tailwind et VueJS
    <br />  
    Basé sur le site Medium
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

Novi est un site web visant à partager des articles sur le monde de la tech. Il s'adresse aux developpeurs, designers, chef de projets, analystes, graphistes etc. Une fois sur le site, un visiteur peut visualiser tous les articles et peut naviguer parmis les profils des auteurs. Ce sont les seuls actions qu'un utilisateur non authentifier peut effectuées.

Pour rédiger un article et suivre une personne, il faut au préalable avoir crée un compte. Une fois cet action effectuée, l'utilisateur est redirigé sur la page d'accueil contenant les derniers articles parus.

![](https://github.com/ohanqo/novi/blob/master/docs/home.png)

L'utilisateur peut se rendre sur son profil et compléter ce dernier. Il peut ajouter une biographie ainsi qu'un lien vers un avatar le représentant. Lorsqu'il accède à un profil d'une autre personne, il peut visualiser les informations de cette denière, la liste de ses articles et il peut la suivre en cliquant sur le bouton follow.

![](https://github.com/ohanqo/novi/blob/master/docs/profile.png)

La rédaction d'un article s'effectue en cliquant sur le bouton `Write an article` présent dans la barre de navigation. Cette page comporte trois champs qui sont obligatoires: titre, image et texte. Le titre doit être unique parmis la liste de tous les articles car il permet de génerer un slug, ce qui augment le référencement. Une fois l'article crée, il se retrouve directement en premier sur la page d'accueil.
