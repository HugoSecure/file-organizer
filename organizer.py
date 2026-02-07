import os
import shutil

# Carpeta donde está el script
BASE_DIR = os.getcwd()

# Tipos de archivos y sus carpetas
FILE_TYPES = {
    "Imágenes": [".jpg", ".png", ".jpeg"],
    "Documentos": [".pdf", ".docx", ".txt"],
    "Audio": [".mp3", ".wav"],
    "Videos": [".mp4", ".avi"]
}

# Recorre todos los archivos de la carpeta
for archivo in os.listdir(BASE_DIR):
    ruta_archivo = os.path.join(BASE_DIR, archivo)

    # Solo archivos (ignora carpetas)
    if os.path.isfile(ruta_archivo):
        for carpeta, extensiones in FILE_TYPES.items():
            if archivo.lower().endswith(tuple(extensiones)):
                ruta_carpeta = os.path.join(BASE_DIR, carpeta)
                os.makedirs(ruta_carpeta, exist_ok=True)  # crea carpeta si no existe
                shutil.move(ruta_archivo, ruta_carpeta)   # mueve el archivo
                break

print("¡Archivos organizados!")
