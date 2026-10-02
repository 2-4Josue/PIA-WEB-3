#!/usr/bin/env bash
# Salir inmediatamente si ocurre un error
set -o errexit

# 1. Instalar las dependencias
pip install -r requirements.txt

# 2. Recopilar archivos estáticos (CSS e imágenes)
python manage.py collectstatic --no-input

# 3. Aplicar migraciones a la base de datos
python manage.py migrate