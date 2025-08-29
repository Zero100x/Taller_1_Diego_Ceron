import os
import requests

# Carpeta datasets/
folder = "datasets"
os.makedirs(folder, exist_ok=True)

# URL directa del CSV
url = "https://www.datos.gov.co/api/views/tsqy-9zs2/rows.csv?accessType=DOWNLOAD"

# Ruta donde se guardará el archivo
csv_path = os.path.join(folder, "dataset.csv")

# Descargar y guardar el archivo
response = requests.get(url)
with open(csv_path, "wb") as f:
    f.write(response.content)

print(f"✅ Dataset descargado y guardado en: {csv_path}")
