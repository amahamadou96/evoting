# 🗳️ Mini E-Voting — Flask & MySQL
Nom : Mahamadou Soumaila
Prenom : Abdoulahi 
Tp: Persistance des données avec Flask & MySQL 
<img width="1918" height="774" alt="image" src="https://github.com/user-attachments/assets/a4c2d304-37a3-4de1-8a54-1daa6d419183" />


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
<img width="1919" height="1079" alt="Capture d&#39;écran 2026-04-06 223714" src="https://github.com/user-attachments/assets/3f690785-7ba5-45e3-b5d3-b7a92c953d02" />
<img width="1088" height="661" alt="image" src="https://github.com/user-attachments/assets/88e917bc-50f6-4cdc-bd3a-2f7391539520" />

<img width="1105" height="824" alt="Capture d&#39;écran 2026-04-06 224126" src="https://github.com/user-attachments/assets/06ea3dc8-af13-4c68-99f9-0bdbc31e01b4" />
<img width="1027" height="681" alt="Capture d&#39;écran 2026-04-06 225411" src="https://github.com/user-attachments/assets/42b2f1ee-41d4-4c0f-a121-06f6811f6bdf" />


### 1. Créer un électeur
- **POST** `http://127.0.0.1:5000/electeurs`
```json
{
  "nom": "Abdoulahi",
  "email": "mahamadouabdoulahi566@gmail.com",
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
<img width="679" height="189" alt="Capture d&#39;écran 2026-04-06 225855" src="https://github.com/user-attachments/assets/7ea5ba42-af0f-48ee-bdf9-84853f10f9ab" />

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
