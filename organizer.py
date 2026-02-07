from pathlib import Path
import shutil
import argparse

# ----------------------------------
# Configuración básica: tipos de archivos y exclusiones
# ----------------------------------
DEFAULT_FILE_TYPES = {
    "Imágenes": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Audio": [".mp3", ".wav"],
    "Videos": [".mp4", ".avi", ".mov"]
}

EXCLUDE_FILES = ["organizer.py", "README.md"]  # Archivos que no se moverán

# ----------------------------------
# Argumentos desde la terminal
# ----------------------------------
parser = argparse.ArgumentParser(description="Organiza archivos en subcarpetas por tipo")
parser.add_argument("--path", type=str, default=".", help="Ruta de la carpeta a organizar")
parser.add_argument("--custom", nargs="+", help="Agregar carpetas personalizadas: Carpeta:ext1:ext2")
args = parser.parse_args()
BASE_DIR = Path(args.path).resolve()

# ----------------------------------
# Añadir tipos personalizados si los hay
# ----------------------------------
file_types = DEFAULT_FILE_TYPES.copy()
if args.custom:
    for item in args.custom:
        parts = item.split(":")
        carpeta = parts[0]
        extensiones = ["."+ext.lower().lstrip(".") for ext in parts[1:]]
        file_types[carpeta] = extensiones

# ----------------------------------
# Contador de archivos movidos
# ----------------------------------
count = 0

# ----------------------------------
# Organización de archivos
# ----------------------------------
for archivo in BASE_DIR.iterdir():
    if archivo.is_file() and archivo.name not in EXCLUDE_FILES:
        for carpeta, extensiones in file_types.items():
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
print(f"Ruta utilizada: {BASE_DIR}")
