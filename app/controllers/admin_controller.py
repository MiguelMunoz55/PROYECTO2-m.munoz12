from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models.Producto import Producto
from app.models.Ingrediente import Ingrediente
from app.config.db import db
from app.seeders.insertar_productos import cargar_productos
from app.seeders.insertar_ingredientes import cargar_ingredientes

admin_blueprint = Blueprint("admin", __name__, url_prefix="/admin")

# Dashboard principal
@admin_blueprint.route("/dashboard")
@login_required
def dashboard():
    if not current_user.es_admin:
        return "Acceso denegado", 403

    productos = Producto.query.all()
    ingredientes = Ingrediente.query.all()

    return render_template(
        "admin/dashboard.html",
        user=current_user,
        productos=productos,
        ingredientes=ingredientes
    )

# Ruta para cargar ingredientes
@admin_blueprint.route("/cargar-ingredientes", methods=["POST"])
@login_required
def cargar_ingredientes_route():
    if not current_user.es_admin:
        return "Acceso denegado", 403

    try:
        cargar_ingredientes()
    except Exception as e:
        db.session.rollback()
        
    return redirect(url_for("admin.dashboard"))

# Ruta para cargar productos
@admin_blueprint.route("/cargar-productos", methods=["POST"])
@login_required
def cargar_productos_route():
    if not current_user.es_admin:
        return "Acceso denegado", 403

    try:
        cargar_productos()
    except Exception as e:
        db.session.rollback()
        
    return redirect(url_for("admin.dashboard"))
