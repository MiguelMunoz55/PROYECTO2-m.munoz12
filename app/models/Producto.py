from app.models.IProducto import IProducto
from app.config.db import db

class Producto(db.Model):
    __tablename__ = "productos"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio_publico = db.Column(db.Float, nullable=False)
    costo = db.Column(db.Float, nullable=False)
    inventario = db.Column(db.Integer, nullable=False)

    id_ingrediente_1 = db.Column(db.Integer, db.ForeignKey("ingredientes.id"), nullable=True)
    id_ingrediente_2 = db.Column(db.Integer, db.ForeignKey("ingredientes.id"), nullable=True)
    id_ingrediente_3 = db.Column(db.Integer, db.ForeignKey("ingredientes.id"), nullable=True)

    ingrediente_1 = db.relationship("Ingrediente", foreign_keys=[id_ingrediente_1])
    ingrediente_2 = db.relationship("Ingrediente", foreign_keys=[id_ingrediente_2])
    ingrediente_3 = db.relationship("Ingrediente", foreign_keys=[id_ingrediente_3])

    def calcular_rentabilidad(self):
        return self.precio_publico - self.costo

    def tiene_inventario(self):
        return self.inventario > 0

    def consumir_ingredientes(self):
        if self.inventario > 0:
            self.inventario -= 1
        else:
            raise ValueError("No hay inventario disponible")