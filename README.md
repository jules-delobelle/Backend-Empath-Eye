# Empath'Eye — Backend

Backend Django REST Framework pour Empath'Eye, un dispositif de lunettes connectées destiné à aider les enfants atteints de troubles du spectre de l'autisme (TSA) à mieux comprendre les émotions faciales.

Ce backend expose une API REST consommée par l'[application mobile Flutter](https://github.com/jules-delobelle/Empath-Eye-App). Il gère l'authentification des utilisateurs, le stockage des données (enfants, sessions, détections) et le calcul de statistiques.

## Stack technique

- **Framework** : Django + Django REST Framework
- **Base de données** : MySQL
- **Authentification** : JWT (djangorestframework-simplejwt)
- **Hébergement** : DigitalOcean App Platform + Managed MySQL
- **Serveur d'application** : Gunicorn

## Architecture de la base de données

Le projet repose sur une hiérarchie de modèles :

```
User (Django) → Enfant → Session → Detection
```

- **Enfant** — profil d'un enfant lié à un utilisateur (prénom, date de naissance, dernier téléchargement)
- **Session** — regroupe toutes les détections d'une journée pour un enfant donné
- **Detection** — une détection d'émotion individuelle (émotion, heure, importance)

Émotions supportées : `joie`, `tristesse`, `colere`, `surprise`, `neutre`.

## Structure du projet

```
backend/
├── api/
│   ├── models.py          # Modèles Enfant, Session, Detection
│   ├── serializers.py      # Conversion JSON ↔ objets Python
│   ├── views.py             # Logique métier (ViewSets + APIViews)
│   ├── urls.py               # Routing des endpoints
│   └── migrations/
├── empatheyebackend/
│   ├── settings.py          # Configuration Django
│   ├── wsgi.py
│   └── urls.py
├── requirements.txt
├── .env                      # Variables d'environnement (non versionné)
└── README.md
```

## Prérequis

- Python 3.x
- MySQL (local ou managé)
- pip

## Installation locale

1. Cloner le dépôt :
```bash
git clone https://github.com/jules-delobelle/Backend-Empath-Eye.git
cd Backend-Empath-Eye
```

2. Créer un environnement virtuel et installer les dépendances :
```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sur Windows
pip install -r requirements.txt
```

3. Créer un fichier `.env` à la racine avec les variables suivantes :
```env
SECRET_KEY=your-django-secret-key
DEBUG=True
DB_NAME=empatheye
DB_USER=root
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=3306
```

4. Appliquer les migrations :
```bash
python manage.py migrate
```

5. Lancer le serveur de développement :
```bash
python manage.py runserver 0.0.0.0:8000
```

> Le paramètre `0.0.0.0` permet d'accepter les connexions depuis d'autres appareils du réseau local (utile pour tester avec un téléphone physique).

## Endpoints principaux

| Méthode | Endpoint | Description |
|---|---|---|
| POST | `/api/register/` | Création d'un compte utilisateur |
| POST | `/api/token/` | Connexion, retourne un token JWT |
| GET / POST / PATCH / DELETE | `/api/enfant/` | Gestion des profils enfants |
| GET / POST | `/api/session/` | Gestion des sessions |
| GET / POST | `/api/detection/` | Gestion des détections (filtres `?session=`, `?important=true`) |
| GET | `/api/stats/?enfant=<id>` | Statistiques des émotions sur les 7 dernières sessions |

Toutes les requêtes (hors `/register/` et `/token/`) nécessitent un header :
```
Authorization: Bearer <token>
```

## Déploiement

Le projet est hébergé sur **DigitalOcean App Platform**, financé via le GitHub Student Pack :

- Redéploiement automatique à chaque push sur la branche principale
- Migrations appliquées automatiquement au démarrage via la commande de lancement :
```bash
python manage.py migrate && gunicorn empatheyebackend.wsgi:application --worker-tmp-dir /dev/shm --bind 0.0.0.0:8080
```
- Variables d'environnement sensibles stockées de manière chiffrée sur la plateforme
- Base de données MySQL managée, connexion sécurisée via SSL

## Sécurité

- Authentification par JWT avec expiration des tokens
- Filtrage systématique des données par utilisateur (chaque utilisateur n'accède qu'à ses propres enfants/sessions/détections)
- Aucune donnée sensible n'est versionnée dans le code (utilisation d'un fichier `.env`)

## Lien avec l'application mobile

Ce backend est consommé par l'[application Flutter Empath'Eye](https://github.com/jules-delobelle/Empath-Eye-App), qui récupère les données des lunettes via Bluetooth et les envoie à cette API pour stockage et analyse.

## Équipe

Projet réalisé dans le cadre du PFE Empath'Eye — ESIEE Paris, 2026.
