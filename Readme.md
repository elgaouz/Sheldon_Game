# 🧠 Rock Paper Scissors Lizard Spock Tournament

## 👋 Introduction

Ce projet est une simulation de tournoi basée sur la version enrichie du jeu "Pierre Feuille Ciseaux", rendue célèbre par la série **The Big Bang Theory** :  
> _"Rock Paper Scissors Lizard Spock"_

Cette version introduit deux nouveaux signes – **Spock** et **Lézard** – pour rendre le jeu plus complexe et amusant. Le tournoi se joue selon des règles précises, et les données de chaque joueur sont préétablies.

> 🎯 Ce projet a été réalisé dans le cadre d’un **entretien technique pour le stage de développeur Python en IA générative au sein de l'équipe tech de [datascientist.fr](https://datascientist.fr)**.

---

## 🕹️ Principe du jeu

Chaque joueur possède une séquence de coups (signes) qu’il joue à chaque round du tournoi. Lorsqu’un joueur gagne un match, il passe au round suivant. Le processus continue jusqu’à ce qu’il ne reste plus qu’un vainqueur.

---

## 📚 Règles du jeu

Voici les interactions entre les signes :

- ✂️ **Ciseaux** coupent **Feuille**
- 📄 **Feuille** couvre **Pierre**
- 🪨 **Pierre** écrase **Lézard**
- 🦎 **Lézard** empoisonne **Spock**
- 🖖 **Spock** casse **Ciseaux**
- ✂️ **Ciseaux** décapitent **Lézard**
- 🦎 **Lézard** mange **Feuille**
- 📄 **Feuille** réfute **Spock**
- 🖖 **Spock** vaporise **Pierre**
- 🪨 **Pierre** écrase **Ciseaux**

⚠️ En cas d’égalité (deux joueurs jouent le même signe), le **joueur dont le nom est alphabétiquement en premier gagne**.

---

## 🗃️ Données attendues

Deux fichiers CSV sont nécessaires pour lancer le tournoi :

### 📁 `players_infos.csv`
Décrit les coups que chaque joueur jouera à chaque round.

| Name  | Round | Sign   |
|-------|-------|--------|
| John  | 0     | PAPER  |
| John  | 1     | LIZARD |
| Jack  | 0     | SPOCK  |
| ...   | ...   | ...    |

### 📁 `round_0.csv`
Contient la liste des matchs du premier round.

| Player 1 | Player 2 |
|----------|----------|
| Henry    | Jack     |
| Paul     | John     |

---

## 🔄 Fonctionnement du tournoi

1. 🔢 Le tournoi se joue **par rounds successifs**.
2. 🧠 Chaque joueur utilise **le signe défini pour le round en cours**.
3. ⚔️ Chaque match est joué selon les règles du jeu.
4. ✅ Le gagnant avance au round suivant.
5. 🏆 Une fois qu’il ne reste qu’un joueur, il est **déclaré vainqueur**.

---

## 🎯 Objectifs du programme

- Lire les fichiers `players_infos.csv` et `round_0.csv`.
- Simuler chaque round du tournoi.
- Déterminer le vainqueur final.
- Générer un fichier `matches.csv` contenant l’historique des matchs.

---

## 📤 Sortie attendue

### 📢 Console
Afficher le nom du vainqueur comme suit : TOURNAMENT WINNER : Nom Du Gagnant
