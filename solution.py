# Constants (Input/Output filenames)
PLAYER_INFO_FILE = 'inputs/players_infos.csv'
ROUND_0_FILE = 'inputs/round_0.csv'
MATCHES_FILE = 'matches.csv'

import csv

# 1️⃣ 📂 Charger les informations des joueurs dans un dictionnaire (par nom de joueur)
players_infos = {}
with open(PLAYER_INFO_FILE, newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row['Name']
        round_number = int(row['Round'])  # Le numéro du round
        sign = row['Sign']

        if name not in players_infos:
            players_infos[name] = {}

        players_infos[name][round_number] = sign  # Ajouter le signe pour ce round spécifique

# 2️⃣ 📂 Charger les rounds sous forme de liste de tuples (Player1, Player2)
rounds_0 = []
with open(ROUND_0_FILE, newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    rounds_0 = [(row['Player 1'], row['Player 2']) for row in reader]

# 3️⃣ 🔥 Définition des règles du jeu
rules = {
    "SCISSORS": ["PAPER", "LIZARD"],  # Les ciseaux coupent la feuille et décapitent le lézard
    "PAPER": ["ROCK", "SPOCK"],  # La feuille couvre la pierre et réfute Spock
    "ROCK": ["SCISSORS", "LIZARD"],  # La pierre écrase les ciseaux et le lézard
    "LIZARD": ["SPOCK", "PAPER"],  # Le lézard empoisonne Spock et mange la feuille
    "SPOCK": ["SCISSORS", "ROCK"]  # Spock casse les ciseaux et vaporise la pierre
}

# 4️⃣ 🏆 Fonction pour déterminer le gagnant d'un duel
def determine_winner(player1, player2, round_number):
    """Détermine le gagnant en fonction des signes des joueurs"""
    sign1 = players_infos[player1][round_number]
    sign2 = players_infos[player2][round_number]

    # Si égalité, on choisit le joueur dont le nom vient en premier alphabétiquement
    if sign1 == sign2:
        return min(player1, player2)  # En cas d'égalité, celui dont le nom est avant gagne

    # Sinon, on applique les règles du jeu
    elif sign2 in rules[sign1]:
        return player1
    else:
        return player2

# 5️⃣ 📂 Fonction pour exécuter le tournoi
def run_tournament(players_infos, initial_matches, output_file):
    """Exécute le tournoi et enregistre les résultats dans un fichier CSV"""
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Round", "Winner", "Player 1 name", "Player 1 sign", "Player 2 name", "Player 2 sign"])

        round_number = 0
        rounds = initial_matches  # Duels du premier round

        while len(rounds) > 0:
            next_round = []  # Liste des gagnants du round actuel

            for player1, player2 in rounds:
                winner = determine_winner(player1, player2, round_number)

                sign1 = players_infos[player1][round_number]
                sign2 = players_infos[player2][round_number]

                # Enregistrer le duel
                writer.writerow([round_number, winner, player1, sign1, player2, sign2])

                # Ajouter le gagnant pour le prochain round
                next_round.append(winner)

            # Générer les duels du prochain round
            rounds = [(next_round[i], next_round[i + 1]) for i in range(0, len(next_round) - 1, 2)]
            round_number += 1  # Passer au round suivant

        # Afficher le gagnant final du tournoi
        grand_winner = next_round[0]
        print(f"\nTOURNAMENT WINNER: {grand_winner}")

# 6️⃣ 🚀 Exécution du code
run_tournament(players_infos, rounds_0, MATCHES_FILE)
