# Mi Primer Script Python

Consulta la API pública de GitHub y guarda un resumen en JSON.

## Requisitos

- Python 3.8 o superior

## Instalación

```bash
# 1. Clona el repositorio
git clone https://github.com/TU_USUARIO/mi-primer-script-python.git
cd mi-primer-script-python

# 2. Instala las dependencias
pip install -r requirements.txt
```

## Uso

```bash
python script.py
```

Genera un archivo `resultado.json` con los datos del usuario consultado.

## Ejemplo de salida

```json
{
  "usuario": "octocat",
  "nombre": "The Octocat",
  "repositorios": 8,
  "seguidores": 9000,
  "consulta_en": "2026-05-28T10:30:00"
}
```
