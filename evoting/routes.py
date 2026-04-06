from flask import Blueprint, request, jsonify
from app import db
from models import Electeur, Candidat, Vote, Election

main = Blueprint('main', __name__)


# ─── ELECTEURS ────────────────────────────────────────────────

@main.route('/electeurs', methods=['POST'])
def create_electeur():
    data = request.json
    if not data or not data.get('nom') or not data.get('email') or not data.get('mot_de_passe'):
        return jsonify({"error": "Champs manquants"}), 400

    if Electeur.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email déjà utilisé"}), 400

    e = Electeur(nom=data['nom'], email=data['email'])
    e.set_password(data['mot_de_passe'])
    db.session.add(e)
    db.session.commit()
    return jsonify({"id": e.id, "message": "Électeur créé ✅"}), 201


@main.route('/electeurs', methods=['GET'])
def get_electeurs():
    electeurs = Electeur.query.all()
    return jsonify([
        {"id": e.id, "nom": e.nom, "email": e.email, "has_voted": e.has_voted}
        for e in electeurs
    ])


@main.route('/electeurs/<int:id>', methods=['GET'])
def get_electeur(id):
    e = Electeur.query.get_or_404(id)
    return jsonify({"id": e.id, "nom": e.nom, "email": e.email, "has_voted": e.has_voted})


# ─── ELECTIONS ────────────────────────────────────────────────

@main.route('/elections', methods=['POST'])
def create_election():
    data = request.json
    if not data or not data.get('titre'):
        return jsonify({"error": "Titre manquant"}), 400

    election = Election(titre=data['titre'])
    db.session.add(election)
    db.session.commit()
    return jsonify({"id": election.id, "message": "Élection créée ✅"}), 201


@main.route('/elections', methods=['GET'])
def get_elections():
    elections = Election.query.all()
    return jsonify([{"id": el.id, "titre": el.titre} for el in elections])


# ─── CANDIDATS ────────────────────────────────────────────────

@main.route('/candidats', methods=['POST'])
def create_candidat():
    data = request.json
    if not data or not data.get('nom') or not data.get('election_id'):
        return jsonify({"error": "Champs manquants"}), 400

    c = Candidat(nom=data['nom'], election_id=data['election_id'])
    db.session.add(c)
    db.session.commit()
    return jsonify({"id": c.id, "message": "Candidat créé ✅"}), 201


@main.route('/candidats', methods=['GET'])
def get_candidats():
    candidats = Candidat.query.all()
    return jsonify([{"id": c.id, "nom": c.nom, "election_id": c.election_id} for c in candidats])


# ─── VOTE ─────────────────────────────────────────────────────

@main.route('/vote', methods=['POST'])
def voter():
    data = request.json
    if not data or not data.get('electeur_id') or not data.get('candidat_id'):
        return jsonify({"error": "Champs manquants"}), 400

    electeur = Electeur.query.get(data['electeur_id'])
    if not electeur:
        return jsonify({"error": "Électeur introuvable"}), 404

    if electeur.has_voted:
        return jsonify({"error": "Cet électeur a déjà voté ❌"}), 400

    candidat = Candidat.query.get(data['candidat_id'])
    if not candidat:
        return jsonify({"error": "Candidat introuvable"}), 404

    vote = Vote(electeur_id=electeur.id, candidat_id=candidat.id)
    electeur.has_voted = True
    db.session.add(vote)
    db.session.commit()
    return jsonify({"message": "Vote enregistré ✅"})


# ─── RESULTATS ────────────────────────────────────────────────

@main.route('/resultats/<int:election_id>', methods=['GET'])
def resultats(election_id):
    election = Election.query.get_or_404(election_id)
    candidats = Candidat.query.filter_by(election_id=election_id).all()
    resultats = []
    for c in candidats:
        nb_votes = Vote.query.filter_by(candidat_id=c.id).count()
        resultats.append({"candidat": c.nom, "votes": nb_votes})
    return jsonify({"election": election.titre, "resultats": resultats})
