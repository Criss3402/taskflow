import subprocess
import time
import json
import os

print("Starting server...")
server_process = subprocess.Popen(
    ["python", "manage.py", "runserver", "127.0.0.1:8000", "--noreload"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

try:
    time.sleep(3)

    tests = [
        {
            "code": "200 OK",
            "desc": "Lectura exitosa (GET)",
            "cmd": ["curl.exe", "-s", "-i", "http://127.0.0.1:8000/api/tasks/"]
        },
        {
            "code": "201 Created",
            "desc": "Creación exitosa (POST)",
            "cmd": ["curl.exe", "-s", "-i", "-X", "POST", "http://127.0.0.1:8000/api/projects/",
                    "-H", "Content-Type: application/json",
                    "-d", '{"name": "Proyecto Test Curl", "description": "Creado para prueba"}']
        },
        {
            "code": "204 No Content",
            "desc": "Eliminación exitosa (DELETE)",
            "setup_create": True,
            "cmd": ["curl.exe", "-s", "-i", "-X", "DELETE"] # url will be appended
        },
        {
            "code": "400 Bad Request",
            "desc": "Datos no pasaron validación (falta título obligatorio)",
            "cmd": ["curl.exe", "-s", "-i", "-X", "POST", "http://127.0.0.1:8000/api/tasks/",
                    "-H", "Content-Type: application/json",
                    "-d", '{"description": "Sin titulo"}']
        },
        {
            "code": "401 Unauthorized / 403 Forbidden",
            "desc": "Credenciales inválidas en autenticación",
            "cmd": ["curl.exe", "-s", "-i", "http://127.0.0.1:8000/api/tasks/",
                    "-H", "Authorization: Basic aW52YWxpZDpiYWQ="]
        },
        {
            "code": "404 Not Found",
            "desc": "Recurso no existe (/api/tasks/999/)",
            "cmd": ["curl.exe", "-s", "-i", "http://127.0.0.1:8000/api/tasks/999/"]
        },
        {
            "code": "500 Internal Server Error",
            "desc": "Error no controlado del servidor (capturado por custom_exception_handler)",
            "cmd": ["curl.exe", "-s", "-i", "http://127.0.0.1:8000/api/test-500/"]
        }
    ]

    output_lines = []
    output_lines.append("================================================================================")
    output_lines.append("  TASKFLOW - REGISTRO DE RESPUESTAS REALES CON CURL (CLASE 4 - PARTE 2.1 Y 5.2)")
    output_lines.append("================================================================================\n")

    for i, test in enumerate(tests, 1):
        output_lines.append(f"CASO {i}: {test['code']} - {test['desc']}")
        cmd = list(test["cmd"])
        if test.get("setup_create"):
            # Create a project first to delete it
            create_res = subprocess.run(
                ["curl.exe", "-s", "-X", "POST", "http://127.0.0.1:8000/api/projects/",
                 "-H", "Content-Type: application/json",
                 "-d", '{"name": "Para Borrar"}'],
                capture_output=True, text=True
            )
            data = json.loads(create_res.stdout)
            del_id = data["id"]
            cmd.append(f"http://127.0.0.1:8000/api/projects/{del_id}/")

        cmd_display = " ".join(cmd)
        output_lines.append(f"Comando ejecutado:\n  {cmd_display}\n")

        res = subprocess.run(cmd, capture_output=True, text=True)
        output_lines.append("Respuesta real obtenida:\n")
        output_lines.append(res.stdout.strip())
        output_lines.append("\n" + "-" * 80 + "\n")

    with open("respuestas_curl.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))

    print("respuestas_curl.txt created successfully!")

finally:
    server_process.terminate()
    server_process.wait()
    print("Server stopped.")
