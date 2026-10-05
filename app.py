import os
import csv
import requests
from flask import Flask, render_template, abort, jsonify
from markupsafe import Markup

app = Flask(__name__)

ATU_INFO = {
    "nom": "Atlantis Transport Union",
    "tag": "ATU",
    "philosophie": "Simulation hardcore, rigueur économique et politique KM 0",
    "auteur": "Trans_Europe_Rail"
}

HUBS_PRINCIPAUX = [
    {"ville": "Madrid", "pays": "Espagne", "type": "Hub Sud / Péninsule Ibérique"},
    {"ville": "Paris", "pays": "France", "type": "Hub Central"},
    {"ville": "Berlin", "pays": "Allemagne", "type": "Hub Centre-Europe"},
    {"ville": "Istanbul", "pays": "Turquie", "type": "Hub Transcontinental"},
    {"ville": "Varsovie", "pays": "Pologne", "type": "Hub Est"},
    {"ville": "Hambourg", "pays": "Allemagne", "type": "Hub Nord"}
]

LIGNES_PHARES = [
    {
        "id": 1,
        "depart": "Madrid (Espagne)",
        "arrivee": "Istanbul (Turquie)",
        "km": 3850,
        "type_convoi": "Transcontinental / Longue distance",
        "statut": "Actif",
        "description": "L'épreuve reine de l'ATU à travers l'Europe entière. Concentration maximale requise."
    },
    {
        "id": 2,
        "depart": "Madrid (Espagne)",
        "arrivee": "Paris (France)",
        "km": 1270,
        "type_convoi": "Liaison Ibéro-Française",
        "statut": "Actif",
        "description": "Axe régulier pour le fret prioritaire entre l'Espagne et la France."
    },
    {
        "id": 3,
        "depart": "Hambourg (Allemagne)",
        "arrivee": "Varsovie (Pologne)",
        "km": 890,
        "type_convoi": "Corridor Nord-Est",
        "statut": "Ouvert",
        "description": "Parcours rapide à travers les plaines d'Europe centrale."
    }
]

@app.route('/')
def index():
    return render_template('index.html', atu=ATU_INFO)

@app.route('/lignes')
def lignes():
    return render_template('lignes.html', atu=ATU_INFO, lignes=LIGNES_PHARES, hubs=HUBS_PRINCIPAUX)

@app.route('/classement')
def classement():
    return render_template('classement.html', atu=ATU_INFO)

@app.route('/gestion-flotte')
def gestion_flotte():
    return render_template('factures.html', atu=ATU_INFO)

@app.route('/recrutement')
def recrutement():
    return render_template('recrutement.html', atu=ATU_INFO)

if __name__ == '__main__':
    app.run(debug=True)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', atu=ATU_INFO), 404
