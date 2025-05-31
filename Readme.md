🧠 YouTube Comment Scraper – Veritasium
Este proyecto implementa un scraper en Python que utiliza la YouTube Data API v3 para recopilar información pública sobre los videos más recientes del canal Veritasium y sus comentarios.

El objetivo es generar una base de datos estructurada con metadatos de los videos (como título, URL y fecha de publicación) junto con los comentarios top-level de los usuarios. Esta información puede ser usada para análisis de contenido, minería de texto, visualizaciones o investigaciones sobre participación del público.
🛠 Características principales
🔍 Busca automáticamente el canal oficial de Veritasium

📥 Recupera hasta 50 videos más recientes

💬 Extrae hasta 50 comentarios por video

🗃 Genera una tabla con:

Título del video

URL

Fecha de publicación

Nombre del canal

Comentario

Autor del comentario

Fecha del comentario

Likes del comentario

📁 Guarda los resultados en un archivo CSV ubicado en data/Veritasium_comments.csv