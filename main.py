from flask import Flask, render_template, request, redirect
from config import *
import random

app = Flask(__name__)
app.config['SECRET_KEY']= 'dannapaola'

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/juegos')
def pagina_juegos():
    return render_template('pagina_principal.html')

@app.route('/signup')
def retornar_registrarse():
    return render_template('registro.html')

@app.route('/iniciar/sesion/', methods=['POST'])
def iniciar_sesion():
    
    usuario = request.form['username']
    contraseña = request.form['password']
    
    contenedor_clase = usuarios(usuario, contraseña)
    alerta = True
    
    if contenedor_clase.Iniciar_sesion() == True:
        nombre = contenedor_clase.nombre_usuario()
        return render_template('pagina_principal.html', nombre= nombre)
    
    return render_template('index.html', alerta=alerta)

@app.route('/registrarse', methods=['POST'])
def registrarse():
    
    nombre = request.form['nombre']
    usuario = request.form['usuario']
    contraseña = request.form['contraseña']
    contenedor_clase = usuarios(usuario, contraseña)
    
    if contenedor_clase.registrarse(nombre) == True:
        return render_template('index.html', estado=True)
    
    return render_template('registro.html', estado=False)

if __name__=='__main__':
    app.run(debug=True, port=900)

