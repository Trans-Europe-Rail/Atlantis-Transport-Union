<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>{{ atu.nom }} - Partenaires</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <header>
        <div class="container" style="display: flex; align-items: center; justify-content: space-between; padding: 10px 20px;">
            <div class="logo-area" style="display: flex; align-items: center; gap: 14px;">
                <img src="{{ url_for('static', filename='Designer.png') }}" alt="Logo ATU" style="height: 50px; width: auto; object-fit: contain;">
                <h1 style="margin: 0; font-size: 1.25rem;">{{ atu.nom }} <span>[{{ atu.tag }}]</span></h1>
            </div>
            <nav style="display: flex; gap: 15px; flex-wrap: wrap;">
                <a href="/">Accueil</a>
                <a href="/actifs">Actifs</a>
                <a href="/lignes">Réseau</a>
                <a href="/carte">Carte & GPS</a>
                <a href="/classement">Classement</a>
                <a href="/factures">Trésorerie</a>
                <a href="/recrutement">Recrutement</a>
                <a href="/reglement">Règlement</a>
                <a href="/conducteur">Mon Profil</a>
                <a href="/garage">Garage</a>
                <a href="/partenariats">Partenaires</a>
                <a href="/discord">Discord</a>
            </nav>
        </div>
    </header>
    <main class="container" style="padding: 20px; min-height: 70vh;">
        <section class="hero" style="padding: 20px 0;">
            <h2>Partenaires & Alliances</h2>
            <p>Liste des entreprises partenaires avec qui nous partageons la route sur les différents axes[cite: 16].</p>
        </section>

        <div class="card" style="padding: 20px; border: 1px solid rgba(255,255,255,0.2); border-radius: 8px; margin-top: 20px; background: rgba(0,0,0,0.5);">
            <h3>Compagnies VTC Alliées</h3>
            <p style="color: var(--text-muted); margin-top: 10px;">Aucun partenariat officiel actif pour le moment. Restez connectés pour de futures collaborations !</p>
        </div>
    </main>
    <footer style="text-align: center; padding: 20px; border-top: 1px solid rgba(255,255,255,0.1); margin-top: 40px; font-size: 0.9rem;">
        <p>&copy; 2026 {{ atu.nom }} — Conçu par {{ atu.auteur }}</p>
    </footer>
</body>
</html>
