# 🗳️ Mini E-Voting — Flask & MySQL

## Installation

```bash
pip install -r requirements.txt
```

## Configuration
Dans `config.py`, modifier la ligne :
```python
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:VOTRE_MOT_DE_PASSE@localhost/evoting_db"
```

## Lancer le projet

```bash
# 1. Créer la base de données MySQL
mysql -u root -p -e "CREATE DATABASE evoting_db;"

# 2. Migrations
flask db init
flask db migrate -m "initial schema"
flask db upgrade

# 3. Lancer le serveur
flask run
```

## Tests Postman

### 1. Créer un électeur
- **POST** `http://127.0.0.1:5000/electeurs`
```json
{
  "nom": "Ali",
  "email": "ali@test.com",
  "mot_de_passe": "1234"
}
```

### 2. Créer une élection
- **POST** `http://127.0.0.1:5000/elections`
```json
{
  "titre": "Election Président 2025"
}
```

### 3. Créer un candidat
- **POST** `http://127.0.0.1:5000/candidats`
```json
{
  "nom": "Candidat A",
  "election_id": 1
}
```

### 4. Voter
- **POST** `http://127.0.0.1:5000/vote`
```json
{
  "electeur_id": 1,
  "candidat_id": 1
}
```

### 5. Voir les résultats
- **GET** `http://127.0.0.1:5000/resultats/1`

### 6. Lister tous les électeurs
- **GET** `http://127.0.0.1:5000/electeurs`

### 7. Lister tous les candidats
- **GET** `http://127.0.0.1:5000/candidats`

## Structure
```
evoting/
├── app.py
├── models.py
├── routes.py
├── config.py
├── requirements.txt
└── templates/
```
