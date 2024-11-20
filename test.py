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
