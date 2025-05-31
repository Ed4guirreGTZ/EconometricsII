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
---
## 🔐 Configuración de la API

1. Ve a [Google Cloud Console](https://console.cloud.google.com/), crea un nuevo proyecto y habilita la **YouTube Data API v3**.
2. Dirígete a la sección "Credenciales" y genera una **clave de API**.
3. Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido: API_KEY=tu_clave_api

---
> ⚠️ **Importante:** No compartas este archivo públicamente ni lo subas al repositorio. Asegúrate de incluir `.env` en tu archivo `.gitignore`.

---

## ▶️ Cómo ejecutar el script

Una vez configurada la clave de API y el entorno, ejecuta el script desde la raíz del proyecto:

```bash
python code/scrape_comments.py


