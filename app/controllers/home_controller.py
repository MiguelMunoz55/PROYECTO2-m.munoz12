from flask import Blueprint, render_template, request, redirect, url_for, session
from app.models.usuario import Usuario
from app.config.db import db

home_blueprint = Blueprint("home", __name__)

@home_blueprint.route("/")
def home():
    return render_template("login.html")

@home_blueprint.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    user = Usuario.query.filter_by(username=username, password=password).first()
    
    if user:
        session["user_id"] = user.id
        session["is_admin"] = user.es_admin

        if user.es_admin:
            return redirect(url_for("admin.dashboard"))
        else:
            return redirect(url_for("user.dashboard"))

    return "Credenciales incorrectas", 401

@home_blueprint.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home.home"))