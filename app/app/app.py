from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from .constantes import SECRET_KEY

chemin_actuel = os.path.dirname(os.path.abspath(__file__))

#Le chemin vers les templates est stocké dans la variable templates:

templates = os.path.join(chemin_actuel, "templates")

#Le chemin vers les statics est stocké dans la variable statics:

statics = os.path.join(chemin_actuel, "static")

app = Flask(
    "Application",
    template_folder=templates,
    static_folder=statics
)
# On configure ici la base de données:

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./bdd.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#TRACK_MODIFICATIONS configuré en False pour retirer le message d'alerte à chaque lancement de l'application.
app.config['SECRET_KEY'] = SECRET_KEY

# On initie l'extension
db = SQLAlchemy()

login = LoginManager()

#On met en place le gestionnaire d'utilisateurs.

from .routes import generic
from .routes import api


