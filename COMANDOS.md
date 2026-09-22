# TaskFlow — Comandos de terminal (Clase 1, Clase 2 y Git/GitHub)

Este zip ya trae armados todos los archivos que la Clase 1 y la Clase 2 piden
crear a mano (`.env`, `.gitignore`, `models.py`, `views.py`, `urls.py`,
`import_tasks.py`, los 3 archivos de `data/`, etc.), más `manage.py` y la
estructura de `config/` y `core/` generada por Django.

Lo único que **no** se puede empaquetar es el entorno virtual (`venv/`) ni la
base de datos (`db.sqlite3`): se generan localmente con los comandos de abajo.

## 1) Extraer y ubicarse

```bash
cd taskflow
```

## 2) Crear y activar el entorno virtual

```bash
python3 -m venv venv

# Linux/Mac
source venv/bin/activate
# Windows PowerShell
venv\Scripts\Activate.ps1
# Windows CMD
venv\Scripts\activate.bat
```

## 3) Instalar dependencias (ya están listadas en requirements.txt)

```bash
pip install -r requirements.txt
```

## 4) Aplicar migraciones y crear superusuario

```bash
python manage.py makemigrations core
python manage.py migrate
python manage.py createsuperuser
```

## 5) Importar los datos de ejemplo (Clase 2)

```bash
python manage.py import_tasks
```

## 6) Levantar el servidor

```bash
python manage.py runserver
```

- Health check: http://127.0.0.1:8000/api/health/
- Admin: http://127.0.0.1:8000/admin/

## 7) Git y GitHub (una sola vez, al principio)

```bash
git init
git add .
git commit -m "Setup inicial de TaskFlow: Django + DRF + health check"

git remote add origin https://github.com/su-usuario/taskflow.git
git branch -M main
git push -u origin main
```

## 8) Ciclo diario (cada clase, de ahí en más)

```bash
git status
git add .
git commit -m "Mensaje descriptivo del avance de hoy"
git push
```

## 9) Traer cambios si trabajás desde otra compu o en equipo

```bash
git pull
```

---

### Verificación rápida de Python (intérprete interactivo, Clase 1 - Parte 0)

```bash
python3 --version
python3
>>> 2 + 2
>>> print("Hola, TaskFlow")
>>> exit()
```
