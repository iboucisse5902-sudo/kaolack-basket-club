from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, nom, poste, numero FROM joueurs")
    joueurs = cursor.fetchall()

    cursor.execute("SELECT adversaire, score_nous, score_adversaire, date FROM matchs")
    matchs = cursor.fetchall()

    cursor.execute("SELECT adversaire, date, lieu FROM matchs_a_venir")
    prochains_matchs = cursor.fetchall()

    conn.close()

    victoires = sum(1 for m in matchs if m[1] > m[2])

    return render_template("index.html", joueurs=joueurs, matchs=matchs, victoires=victoires, prochains_matchs=prochains_matchs)

@app.route("/joueur/<int:joueur_id>")
def joueur_detail(joueur_id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT nom, poste, numero FROM joueurs WHERE id = ?", (joueur_id,))
    joueur = cursor.fetchone()

    conn.close()

    return render_template("joueur.html", joueur=joueur)
@app.route("/ajouter-match", methods=["GET", "POST"])
def ajouter_match():
    if request.method == "POST":
        adversaire = request.form["adversaire"]
        score_nous = request.form["score_nous"]
        score_adversaire = request.form["score_adversaire"]
        date = request.form["date"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO matchs (adversaire, score_nous, score_adversaire, date) VALUES (?, ?, ?, ?)",
            (adversaire, score_nous, score_adversaire, date)
        )
        conn.commit()
        conn.close()

        return redirect("/")

    if __name__ == "__main__":
        import os
        port = int(os.environ.get("PORT", 5000))
        app.run(host="0.0.0.0", port=port)