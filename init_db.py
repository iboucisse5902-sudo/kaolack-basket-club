import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS joueurs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    poste TEXT,
    numero INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS matchs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    adversaire TEXT NOT NULL,
    score_nous INTEGER NOT NULL,
    score_adversaire INTEGER NOT NULL,
    date TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS matchs_a_venir (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    adversaire TEXT NOT NULL,
    date TEXT NOT NULL,
    lieu TEXT
)
""")

# On vide les tables avant de réinsérer (évite les doublons si tu relances)
cursor.execute("DELETE FROM joueurs")
cursor.execute("DELETE FROM matchs")
cursor.execute("DELETE FROM matchs_a_venir")

joueurs = [
    ("Khalil", "Meneur", 7),
    ("Moussa Diop", "Ailier", 10),
    ("Ibrahima Fall", "Pivot", 23),
    ("Cheikh Ndiaye", "Arrière", 5),
    ("Ousmane Ba", "Ailier fort", 11),
    ("Mamadou Sarr", "Meneur", 3),
    ("Abdoulaye Gueye", "Arrière", 14),
    ("Modou Niang", "Pivot", 21),
    ("Serigne Diagne", "Ailier", 9),
    ("Babacar Sy", "Ailier fort", 15),
    ("Lamine Cissé", "Meneur", 8),
    ("Pape Thiam", "Pivot", 25),
]
cursor.executemany("INSERT INTO joueurs (nom, poste, numero) VALUES (?, ?, ?)", joueurs)
matchs_a_venir = [
    ("ASC Ville", "2026-09-20", "Gymnase Municipal"),
    ("Étoile Basket", "2026-09-27", "Extérieur"),
]
cursor.executemany(
    "INSERT INTO matchs_a_venir (adversaire, date, lieu) VALUES (?, ?, ?)",
    matchs_a_venir
)

matchs = [
    ("DUC", 76, 56, "2026-09-05"),
    ("Jeanne d'Arc", 68, 71, "2026-09-12"),
]
cursor.executemany(
    "INSERT INTO matchs (adversaire, score_nous, score_adversaire, date) VALUES (?, ?, ?, ?)",
    matchs
)

conn.commit()
conn.close()

print("Base de données mise à jour !")