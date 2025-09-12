# Python bazaviy image
FROM python:3.11-slim

# Django loyihang uchun env sozlash
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Kerakli paketlarni o‘rnatish uchun ishchi katalog
WORKDIR /app

# Requirements faylni ko‘chirib o‘rnatamiz
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Loyihani konteynerga ko‘chiramiz
COPY . /app/

# Django serverni ishga tushirish (dev rejim uchun)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
