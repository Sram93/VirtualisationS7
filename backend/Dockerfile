FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt requirements.txt
COPY . .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port sur lequel Flask sera exécuté
EXPOSE 5001

# Exécuter le script Python pour attendre MongoDB, puis démarrer Flask
CMD ["sh", "-c", "python wait-for-db.py && flask run --host=0.0.0.0 --port=5001"]
