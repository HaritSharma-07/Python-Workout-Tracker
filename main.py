import requests
from datetime import datetime
import os

today_date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

GENDER = "male"
WEIGHT_KG = 72
HEIGHT_CM = 177.8
AGE = 21
MY_TOKEN = os.environ.get("MY_TOKEN")

bearer_headers = {
"Authorization": f"Bearer {MY_TOKEN}"
}

API_ID = os.environ.get("API_ID")
API_KEY = os.environ.get("API_KEY")

SHEETY_URL = "https://api.sheety.co/0bb072fb6ec406f244240cef0e00a51e/workoutSheetySheet/workouts"

URL = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

exercise_text = input("Tell me what exercise you did : ")

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query" : exercise_text,
    "gender" : GENDER,
    "weight_kg" : WEIGHT_KG,
    "height_cm" : HEIGHT_CM,
    "age" : AGE,
}

class Nutrition:
    def __init__(self, header):
        self.header = header

    def send_post_request(self, parameter, POST_URL):
        response = requests.post(url = URL, headers = self.header, json = parameters)
        req = response.json()
        return req

    def post_today_progress(self, Sheety_url, bearer_headers,inputs_for_sheet):
        try:
            response = requests.post(url = Sheety_url, headers = bearer_headers, json = inputs_for_sheet)
            print("Entry submitted successfully")

        except Exception as e:
            print(f"Something went wrong. {e}")


nutri= Nutrition(headers)
response_from_api = nutri.send_post_request(parameters, URL)
print(response_from_api)

for exercise in response_from_api["exercises"]:
    inputs_for_sheet = {
        "workout":{
            "date" : today_date,
            "time" : time,
            "exercise" : exercise["name"],
            "duration" : exercise["duration_min"],
            "calories" : exercise["nf_calories"],
        }
    }

response_of_posting = nutri.post_today_progress(SHEETY_URL, bearer_headers, inputs_for_sheet)

