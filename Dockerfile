# syntax=docker/dockerfile:1
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# (nije nužno, ali dobro je imati locales)
RUN apt-get update && apt-get install -y --no-install-recommends \
    locales && rm -rf /var/lib/apt/lists/* && \
    sed -i 's/# hr_HR.UTF-8 UTF-8/hr_HR.UTF-8 UTF-8/' /etc/locale.gen && locale-gen
ENV LANG=hr_HR.UTF-8 LC_ALL=hr_HR.UTF-8

WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]