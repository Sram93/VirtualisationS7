# VirtualisationS7
# VirtualizationProject
# Gestion des Dépenses Personnelles

## Description

Une application web pour gérer ses finances personnelles en ajoutant, visualisant et supprimant des transactions. Cette application offre une interface utilisateur intuitive et une API REST backend pour la gestion des données.

---

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

1. **Python 3.9+**
2. **Docker** et **Docker Compose** (optionnel, mais recommandé pour une exécution simplifiée)
3. **MongoDB** (local ou cloud, comme MongoDB Atlas)
4. **Un navigateur web moderne**

---

## Installation et exécution

### 1. Clonez le dépôt

```bash
git clone <url_du_dépôt>
cd <nom_du_dossier>
```

### 2. Configurez les variables d'environnement

Gérer par le docker-compose et app.py

### 3. Installez les dépendances backend

```bash
cd backend
pip install -r requirements.txt
```
Gérer par le docker-compose

### 4. Installez les dépendances frontend

```bash
cd ../frontend
npm install
```

Gérer par le docker-compose

### 5. Démarrez l'application

#### Avec Docker Compose (recommandé)

```bash
docker-compose up --build
```
(à la racine du repo github)

## Endpoints de l’API

### 1. **GET /transactions**

- **Description** : Récupère la liste de toutes les transactions.
- **Retour** :
  ```json
  [
    {
      "id": "64a5b2c7f2c123456789abcd",
      "amount": 100,
      "type": "income",
      "description": "Exemple",
      "date": "2024-12-22T10:00:00Z"
    }
  ]
  ```

### 2. **POST /transactions**

- **Description** : Ajoute une nouvelle transaction.
- **Corps de la requête** :
  ```json
  {
    "amount": 100,
    "type": "income",
    "description": "Exemple",
    "date": "2024-12-22T10:00:00Z"
  }
  ```
- **Retour** :
  ```json
  {
    "message": "Transaction ajoutée avec succès",
    "id": "64a5b2c7f2c123456789abcd"
  }
  ```

### 3. **DELETE /transactions/**

- **Description** : Supprime une transaction par son ID.
- **Retour** :
  - Succès :
    ```json
    {
      "message": "Transaction supprimée avec succès"
    }
    ```
  - Erreur (ID invalide ou inexistant) :
    ```json
    {
      "error": "Transaction non trouvée"
    }
    ```

---

## Fonctionnalités de l’interface utilisateur

1. **Ajout de transaction** :

   - Remplissez le formulaire avec le montant, le type (revenu ou dépense) et une description.
   - La transaction est ajoutée avec la date actuelle.

2. **Visualisation des transactions** :

   - Les transactions sont affichées dans un tableau avec la date, le montant, le type et la description.

3. **Suppression de transaction** :

   - Chaque ligne du tableau a un bouton « Supprimer » pour supprimer une transaction.

4. **Résumé des finances** :

   - Total des revenus.
   - Total des dépenses.
   - Solde calculé (revenus − dépenses).

---

## Technologies utilisées

- **Frontend** : HTML, CSS, JavaScript
- **Backend** : Flask (Python)
- **Base de données** : MongoDB
- **Conteneurisation** : Docker & Docker Compose
- **Autres** : Flask-CORS, Flask-PyMongo

---

## Auteur

Projet réalisé par

AIT MAMAR Sharif

JOUEID Boubaker


