from app import create_app
from app.config.db import db
from app.models.usuario import Usuario
from app.config.config import Config

app = create_app(Config)

with app.app_context():
    admin = Usuario(username="admin", password="1234", es_admin=True)
    usuario = Usuario(username="usuario", password="5678", es_admin=False)

    db.session.add(admin)
    db.session.add(usuario)
    db.session.commit()

    print("Usuarios insertados correctamente")