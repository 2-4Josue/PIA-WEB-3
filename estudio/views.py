import json
import os
from django.shortcuts import render, redirect
from django.contrib import messages

# Rutas de los archivos JSON
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

# 1. RUTA DE LOGIN
def login_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('usuario')
        pass_input = request.POST.get('password')
        usuarios = leer_json(USERS_FILE)
        
        for u in usuarios:
            if u['usuario'] == user_input and u['password'] == pass_input:
                return redirect('dashboard')
                
        messages.error(request, 'El grimorio rechaza estas credenciales.')
    
    return render(request, 'login.html')

# 2. RUTA DEL DASHBOARD
def dashboard(request):
    clientes = leer_json(CLIENTS_FILE)
    
    if request.method == 'POST':
        nuevo_cliente = {
            "nombre": request.POST.get('nombre'),
            "tatuaje": request.POST.get('tatuaje'),
            "fecha": request.POST.get('fecha')
        }
        clientes.append(nuevo_cliente)
        guardar_json(CLIENTS_FILE, clientes)
        return redirect('dashboard')
        
    return render(request, 'dashboard.html', {'clientes': clientes})

# 3. RUTA DE EDITAR
def editar(request, id):
    clientes = leer_json(CLIENTS_FILE)
    
    if request.method == 'POST':
        clientes[id]['nombre'] = request.POST.get('nombre')
        clientes[id]['tatuaje'] = request.POST.get('tatuaje')
        clientes[id]['fecha'] = request.POST.get('fecha')
        guardar_json(CLIENTS_FILE, clientes)
        return redirect('dashboard')
        
    return render(request, 'editar.html', {'cliente': clientes[id], 'id': id})