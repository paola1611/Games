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

tablero = [' '] * 9
jugadores = ['X', 'O']
jugador_actual = jugadores[random.randint(0, 1)]
ganador = None

@app.route('/tictac/')
def index():
    global tablero, jugador_actual, ganador
    tablero = [' '] * 9
    jugador_actual = jugadores[random.randint(0, 1)]
    ganador = None
    return render_template('tictac/index.html', tablero=tablero)

@app.route('/play', methods=['POST'])
def play():
    global tablero, jugador_actual, ganador
    posicion = int(request.form['posicion'])
    tablero[posicion] = jugador_actual
    if check_win():
        ganador = jugador_actual
        return render_template('tictac/win.html', ganador=ganador)
    elif check_draw():
        return render_template('tictac/draw.html')
    else:
        jugador_actual = jugadores[(jugadores.index(jugador_actual) + 1) % 2]
        return render_template('tictac/index.html', tablero=tablero, jugador_actual=jugador_actual)

def check_win():
    global tablero
    for i in range(3):
        if tablero[i*3] == tablero[i*3+1] == tablero[i*3+2] != ' ':
            return True
        if tablero[i] == tablero[i+3] == tablero[i+6] != ' ':
            return True
    if tablero[0] == tablero[4] == tablero[8] != ' ':
        return True
    if tablero[2] == tablero[4] == tablero[6] != ' ':
        return True
    return False

def check_draw():
    global tablero
    for i in range(9):
        if tablero[i] == ' ':
            return False
    return True


@app.route('/piedra/papel/tijeras/')
def index_ppt():
    return render_template('ppt/index.html')

@app.route('/play/ppt/', methods=['POST'])
def play_ppt():
    user_choice = request.form['choice']
    options = ['piedra', 'papel', 'tijeras']
    cpu_choice = random.choice(options)
    
    if user_choice == cpu_choice:
        result = 'Empate'
    elif (user_choice == 'piedra' and cpu_choice == 'tijeras') or (user_choice == 'papel' and cpu_choice == 'piedra') or (user_choice == 'tijeras' and cpu_choice == 'papel'):
        result = 'Ganaste!'
    else:
        result = 'Perdiste'
    
    return render_template('ppt/index.html', user_choice=user_choice, cpu_choice=cpu_choice, result=result)

if __name__=='__main__':
    app.run(debug=True, port=900)

