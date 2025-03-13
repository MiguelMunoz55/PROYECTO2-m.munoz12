from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.models.usuario import Usuario
from app.config.db import db

auth_blueprint = Blueprint("auth", __name__)

@auth_blueprint.route("/")
def home():
    return redirect(url_for("auth.login"))

@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = Usuario.query.filter_by(username=username, password=password).first()

        if user:
            login_user(user)
            if user.es_admin:
                return redirect(url_for("admin.dashboard"))
            else:
                return redirect(url_for("user.dashboard"))

        flash("Credenciales incorrectas")
    
    return render_template("login.html")

@auth_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))