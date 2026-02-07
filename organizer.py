from pathlib import Path
import shutil
import argparse

# ----------------------------------
# Configuración: tipos de archivos y exclusiones
# ----------------------------------
FILE_TYPES = {
    "Imágenes": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Audio": [".mp3", ".wav"],
    "Videos": [".mp4", ".avi", ".mov"]
}

EXCLUDE_FILES = ["organizer.py", "README.md"]  # archivos que no se moverán

# ----------------------------------
# Argumentos desde la terminal
# ----------------------------------
parser = argparse.ArgumentParser(description="Organiza archivos en subcarpetas por tipo")
parser.add_argument("--path", type=str, default=".", help="Ruta de la carpeta a organizar")
args = parser.parse_args()
BASE_DIR = Path(args.path).resolve()

# ----------------------------------
# Contador de archivos movidos
# ----------------------------------
count = 0

# ----------------------------------
# Organización de archivos
# ----------------------------------
for archivo in BASE_DIR.iterdir():
    if archivo.is_file() and archivo.name not in EXCLUDE_FILES:
        for carpeta, extensiones in FILE_TYPES.items():
            if archivo.suffix.lower() in extensiones:
                carpeta_path = BASE_DIR / carpeta
                carpeta_path.mkdir(exist_ok=True)
                shutil.move(str(archivo), carpeta_path)
                count += 1
                break

# ----------------------------------
# Resultado final
# ----------------------------------
print(f"¡Archivos organizados! Se movieron {count} archivo(s).")
