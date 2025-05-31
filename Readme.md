# 📺 YouTube Comment Scraper – Veritasium Channel

Este proyecto implementa un script en Python que utiliza la **YouTube Data API v3** para obtener los videos más recientes del canal [Veritasium](https://www.youtube.com/user/1veritasium), junto con los comentarios públicos disponibles de cada video.

---

## 🧰 Funcionalidad

El script realiza las siguientes tareas:

- 🔍 Busca automáticamente el canal de YouTube llamado **Veritasium**.
- 📥 Recupera hasta 50 videos recientes del canal.
- 💬 Extrae hasta 50 comentarios por video:
  - Texto del comentario
  - Autor del comentario
  - Fecha de publicación
  - Número de likes
- 🧾 Almacena metadatos por video:
  - Título del video
  - URL del video
  - Fecha de publicación
  - Nombre del canal
- 📄 Exporta los resultados como archivo `.csv` para su posterior análisis.

---

## ⚙️ Requisitos

Este script requiere Python 3 y las siguientes bibliotecas:
- `pandas`
- `google-api-python-client`
- `python-dotenv`
También puedes usar `openpyxl` si deseas exportar a Excel (actualmente comentado en el código).
### ✅ Instalación
```bash
pip install -r requirements.txt

🔐 Configuración de la API
Crea una clave de API en Google Cloud Console.

Crea un archivo .env en la raíz del proyecto con esta línea:
API_KEY=tu_clave_api


▶️ Cómo ejecutar el script
Asegúrate de tener el entorno configurado.

Ejecuta el script desde la carpeta raíz:

python code/scrape_comments.py
  