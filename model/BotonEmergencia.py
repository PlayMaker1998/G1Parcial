from utils.db import db
from dataclasses import dataclass

@dataclass
class BotonEmergencia(db.Model):
    __tablename__='botonemergencia'
    id_boton_emergencia: int
    nombres: str
    apellidos: str
    telefono: str
    direccion: str
    correo: str
    test_puntuacion: int
    
    id_boton_emergencia = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(100))
    apellidos = db.Column(db.String(100))
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(255))
    correo = db.Column(db.String(100))
    test_puntuacion = db.Column(db.Integer)


    def __init__(self, nombres, apellidos, telefono, direccion, correo, test_puntuacion):
        self.nombres = nombres
        self.apellidos = apellidos
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo
        self.test_puntuacion = test_puntuacion
