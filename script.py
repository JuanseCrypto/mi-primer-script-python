import requests
import json
from datetime import datetime

def obtener_datos(url: str) -> dict:
    """Llama a una API y devuelve los datos en JSON."""
    respuesta = requests.get(url, timeout=10)
    respuesta.raise_for_status()
    return respuesta.json()

def guardar_json(datos: dict, nombre_archivo: str) -> None:
    """Guarda un diccionario como archivo JSON."""
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)
    print(f"✅ Datos guardados en '{nombre_archivo}'")

def main():
    # API pública de ejemplo: información sobre un usuario de GitHub
    usuario = "octocat"
    url = f"https://api.github.com/users/{usuario}"

    print(f"🔍 Consultando datos de: {usuario}")
    datos = obtener_datos(url)

    # Extraer solo lo que nos interesa
    resumen = {
        "usuario":      datos.get("login"),
        "nombre":       datos.get("name"),
        "repositorios": datos.get("public_repos"),
        "seguidores":   datos.get("followers"),
        "consulta_en":  datetime.now().isoformat(),
    }

    print(json.dumps(resumen, indent=2, ensure_ascii=False))
    guardar_json(resumen, "resultado.json")

if __name__ == "__main__":
    main()
