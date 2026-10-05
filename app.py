import os
import csv
import requests
from flask import Flask, render_template, abort, jsonify
from lignes_data import LIGNES

app = Flask(__name__)

BOT_API_URL = os.environ.get("BOT_API_URL", "").rstrip("/")
API_SECRET = os.environ.get("API_SECRET", "")
FICHIER_FACTURES = "historique_factures.csv"

ATU_INFO = {
    "nom": "Atlantis Transport Union",
    "tag": "ATU",
    "philosophie": "Simulation hardcore, rigueur économique et politique KM 0",
    "auteur": "Trans_Europe_Rail"
}

def get_dashboard_data():
    data = {"actifs": [], "classement": [], "historique": [], "historique_complet": []}
    
    if BOT_API_URL:
        try:
            resp = requests.get(
                f"{BOT_API_URL}/api/dashboard",
                headers={"X-API-Key": API_SECRET},
                timeout=5,
            )
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            print(f"Erreur récupération données bot : {e}")

    factures = []
    total_bus = 0
    total_gazole = 0
    montant_total_depense = 0

    if os.path.exists(FICHIER_FACTURES):
        try:
            with open(FICHIER_FACTURES, "r", encoding="utf-8") as f:
                lignes_fac = list(csv.reader(f))
            if len(lignes_fac) > 1:
                for row in reversed(lignes_fac[1:]):
                    montant = int(row[5]) if row[5].isdigit() else 0
                    type_achat = row[2]

                    if type_achat == "Camion":
                        total_bus += montant
                    elif type_achat == "Carburant":
                        total_gazole += montant
                    
                    montant_total_depense += montant

                    factures.append({
                        "date": row[0], 
                        "conducteur": row[1], 
                        "type": type_achat,
                        "libelle": row[3], 
                        "solde_depart": row[4], 
                        "montant": montant, 
                        "solde_fin": row[6]
                    })
        except Exception as e:
            print(f"Erreur lecture factures CSV : {e}")

    data["factures"] = factures
    data["stats_factures"] = {
        "total_camions": total_bus,
        "total_carburant": total_gazole,
        "total_global": montant_total_depense,
        "nombre_total": len(factures)
    }
    return data

@app.route("/")
def home():
    data = get_dashboard_data()
    return render_template(
        "index.html",
        atu=ATU_INFO,
        actifs=data.get("actifs", []),
        classement=data.get("classement", []),
        historique=data.get("historique", []),
    )

@app.route("/actifs")
def page_actifs():
    data = get_dashboard_data()
    return render_template("actifs.html", atu=ATU_INFO, actifs=data.get("actifs", []))

@app.route("/classement")
def page_classement():
    data = get_dashboard_data()
    return render_template("classement.html", atu=ATU_INFO, classement=data.get("classement", []))

@app.route("/historique")
def page_historique():
    data = get_dashboard_data()
    return render_template("historique.html", atu=ATU_INFO, historique=data.get("historique_complet", data.get("historique", [])))

@app.route("/factures")
def page_factures():
    data = get_dashboard_data()
    return render_template("factures.html", atu=ATU_INFO, factures=data.get("factures", []), stats_factures=data.get("stats_factures", {}))

@app.route("/recrutement")
def recrutement():
    return render_template("recrutement.html", atu=ATU_INFO)

@app.route('/lignes')
def lignes():
    return render_template('lignes.html', atu=ATU_INFO, lignes=LIGNES, total=len(LIGNES))

@app.route('/carte')
def carte():
    return render_template('carte.html', atu=ATU_INFO)

@app.route('/lignes/<numero>')
def ligne_detail(numero):
    ligne = LIGNES.get(numero)
    if not ligne:
        abort(404)
    return render_template('ligne_detail.html', atu=ATU_INFO, numero=numero, ligne=ligne)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html", atu=ATU_INFO), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
