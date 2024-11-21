import requests

#
# BASE_URL = "http://localhost:8000/api"
#
#
# def test_upload_tariff():
#     url = f"{BASE_URL}/tariffs/"
#     payload = {
#         "cargo_type": "Glass",
#         "rate": 0.04,
#         "effective_date": "2020-06-01"
#     }
#     response = requests.post(url, json=payload)
#     print("Upload Tariff:", response.status_code, response.json())
#
#
# def test_calculate_insurance():
#     url = f"{BASE_URL}/calculate/"
#     params = {
#         "cargo_type": "Glass",
#         "declared_value": 1000,
#         "date": "2020-06-15"
#     }
#     response = requests.get(url, params=params)
#     print("Calculate Insurance:", response.status_code, response.json())
#
#
# if __name__ == "__main__":
#     print("Testing API...")
#     test_upload_tariff()
#     test_calculate_insurance()


base_url = "http://localhost:8000/api/tariffs/"

new_tariff = {
    "cargo_type": "Glass",
    "rate": 0.04,
    "effective_date": "2020-06-01"
}

response = requests.post(base_url, json=new_tariff)

if response.status_code == 200:
    print("Tariff created successfully:", response.json())
else:
    print(f"Error creating tariff: {response.status_code} - {response.text}")

tariff_id = response.json()["id"]
get_url = f"{base_url}{tariff_id}/"

response = requests.get(get_url)

if response.status_code == 200:
    print("Tariff fetched successfully:", response.json())
else:
    print(f"Error fetching tariff: {response.status_code} - {response.text}")

updated_tariff = {
    "cargo_type": "Glass",
    "rate": 0.05,
    "effective_date": "2020-07-01"
}

response = requests.put(get_url, json=updated_tariff)

if response.status_code == 200:
    print("Tariff updated successfully:", response.json())
else:
    print(f"Error updating tariff: {response.status_code} - {response.text}")

response = requests.delete(get_url)

if response.status_code == 200:
    print("Tariff deleted successfully:", response.json())
else:
    print(f"Error deleting tariff: {response.status_code} - {response.text}")
