# Insurance Cost API

## Описание проекта

Insurance Cost API — это REST API-сервис для расчета стоимости страхования в зависимости от типа груза, даты и
объявленной стоимости. Тарифы загружаются через JSON, сохраняются в базе данных и используются для вычислений.

### Технологии:

- **FastAPI** — для разработки API.
- **PostgreSQL** — база данных.
- **SQLAlchemy** — ORM.
- **Docker** и **Docker-compose** — для контейнеризации.
- **Uvicorn** — сервер для запуска приложения.

---

## Запуск проекта

### Шаг 1: Установка зависимостей

Убедитесь, что у вас установлены:

- **Docker** (версия 20.10+)
- **Docker Compose** (версия 1.29+)

### Шаг 2: Клонирование репозитория

Склонируйте проект:

```bash
git clone <URL_РЕПОЗИТОРИЯ>
cd <ДИРЕКТОРИЯ_ПРОЕКТА>
```

### Шаг 3: Запуск проекта через Docker Compose

```bash
docker-compose up --build
```

### Шаг 4: Проверка работоспособности
Создайте файл test_api.py и вставьте следующий код и выполните следующий скрипт 
python test_api.py

```bash
import requests

BASE_URL = "http://localhost:8000/api"

def test_upload_tariff():
    url = f"{BASE_URL}/tariffs/"
    payload = {
        "cargo_type": "Glass",
        "rate": 0.04,
        "effective_date": "2020-06-01"
    }
    response = requests.post(url, json=payload)
    print("Upload Tariff:", response.status_code, response.json())

def test_calculate_insurance():
    url = f"{BASE_URL}/calculate/"
    params = {
        "cargo_type": "Glass",
        "declared_value": 1000,
        "date": "2020-06-15"
    }
    response = requests.get(url, params=params)
    print("Calculate Insurance:", response.status_code, response.json())

if __name__ == "__main__":
    print("Testing API...")
    test_upload_tariff()
    test_calculate_insurance()

```