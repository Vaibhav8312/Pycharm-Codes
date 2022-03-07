import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 62
HEIGHT_CM = 167.64
AGE = 19

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
BEARER_TOKEN = os.environ["BEARER_TOKEN"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["SHEET_ENDPOINT"]


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_text = input("Tell me which exercises you did: ")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
response.raise_for_status()
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

for exercise in result["exercises"]:
    # "Sheet expects your record to be nested in a singular root property named after your sheet."
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers,
    )

    print(sheet_response.text)

# # No Authentication
# sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
#
# # Basic Authentication
# sheet_response = requests.post(
#     sheet_endpoint,
#     json=sheet_inputs,
#     auth=(
#         YOUR USERNAME,
#     YOUR PASSWORD,
#     )
# )
#
# # Bearer Token Authentication
# bearer_headers = {
#     "Authorization": f"Bearer {YOUR TOKEN}"
# }
# sheet_response = requests.post(
#     sheet_endpoint,
#     json=sheet_inputs,
#     headers=bearer_headers
# )