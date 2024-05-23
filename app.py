from flask import Flask, render_template, redirect, url_for, request
from utils.db import db
from services.BotonEmergencia import boton_emergencia_blueprint
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION
from model.BotonEmergencia import BotonEmergencia  # Importa el modelo BotonEmergencia

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_CONNECTION

db.init_app(app)
app.register_blueprint(boton_emergencia_blueprint)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        # Obtén los datos del formulario
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        correo = request.form['correo']
        test_puntuacion = request.form['test_puntuacion']
        
        # Crea una instancia del modelo BotonEmergencia con los datos del formulario
        nuevo_boton_emergencia = BotonEmergencia(nombres=nombres, apellidos=apellidos, telefono=telefono,
                                                 direccion=direccion, correo=correo, test_puntuacion=test_puntuacion)
        
        # Agrega la instancia a la sesión y guarda los cambios en la base de datos
        db.session.add(nuevo_boton_emergencia)
        db.session.commit()

        # Redirige a la página de éxito
        return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
