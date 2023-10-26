from flask import Flask, render_template, request, flash, redirect, send_file, url_for

from ..app import app, db, login

# from ..modeles.data import something

# from ..modeles.user import User

from sqlalchemy import and_, or_

from ..constantes import RESULTATS_PAR_PAGES

from flask_login import login_user, current_user, logout_user, login_required
# Import permettant de gérer les connexions et déconnexion des utilisateurs de l'application.
from warnings import warn
# Import permettant d'afficher des messages d'erreurs.
import random, sqlalchemy

@app.route("/")
def accueil():
    return render_template("pages/index.html")