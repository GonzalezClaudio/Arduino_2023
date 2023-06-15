from api_config import db


class Sueldo(db.Model):
    __tablename__ = "sueldo"
    id = db.Column(db.Integer, primary_key=True)
    monto = db.Column(db.Integer)