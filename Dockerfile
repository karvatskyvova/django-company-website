# Dockerfile

# Базовий образ
FROM python:3.9-slim

# Встановлення робочої директорії
WORKDIR /app

# Копіювання файлу вимог
COPY requirements.txt requirements.txt

# Встановлення залежностей
RUN pip install --no-cache-dir -r requirements.txt

# Копіювання всіх файлів проекту
COPY . .

# Встановлення змінної середовища для налаштувань Django
ENV DJANGO_SETTINGS_MODULE=company_website.settings

# Запуск серверу
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "company_website.wsgi:application"]
