from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os

app = Flask(__name__)
app.secret_key = "clave_secreta_examen"

# Rutas de los archivos JSON (bases de datos en texto)
USERS_FILE = 'usuarios.json'
CLIENTS_FILE = 'clientes.json'

def leer_json(filepath):
    if not os.path.exists(filepath):
        return []
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)

def guardar_json(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

# Ruta del Login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_input = request.form['usuario']
        pass_input = request.form['password']
        
        usuarios = leer_json(USERS_FILE)
        
        for u in usuarios:
            if u['usuario'] == user_input and u['password'] == pass_input:
                return redirect(url_for('dashboard'))
                
        flash('Usuario o contraseña incorrectos', 'error')
    
    return render_template('login.html')

# Ruta del Dashboard (Registrar y Consultar)
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    clientes = leer_json(CLIENTS_FILE)
    
    if request.method == 'POST':
        nuevo_cliente = {
            "nombre": request.form['nombre'],
            "tatuaje": request.form['tatuaje'],
            "fecha": request.form['fecha']
        }
        clientes.append(nuevo_cliente)
        guardar_json(CLIENTS_FILE, clientes)
        return redirect(url_for('dashboard'))
        
    return render_template('dashboard.html', clientes=clientes)

# NUEVA RUTA: Actualizar (Editar)
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    clientes = leer_json(CLIENTS_FILE)
    
    if request.method == 'POST':
        # Reemplazar los datos viejos con los nuevos
        clientes[id]['nombre'] = request.form['nombre']
        clientes[id]['tatuaje'] = request.form['tatuaje']
        clientes[id]['fecha'] = request.form['fecha']
        guardar_json(CLIENTS_FILE, clientes)
        return redirect(url_for('dashboard'))
        
    # Mostrar el formulario con los datos actuales
    return render_template('editar.html', cliente=clientes[id], id=id)

if __name__ == '__main__':
    app.run(debug=True)