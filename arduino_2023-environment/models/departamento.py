from api_config import db


class Departamento(db.Model):
    __tablename__ = "departamento"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    sueldo_fk = db.Column(db.Integer, db.ForeignKey("sueldo.id"))
    sueldo = db.relationship('Sueldo' , backref='deptos_sueldos')
    # fk_persona = db.Column(db.Integer, db.ForeignKey("persona.id"))
    # persona = db.relationship("Persona")
