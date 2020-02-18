
import json
import requests
import statistics

print("REQUESTING SOME DATA FROM THE INTERNET...")
request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json"
response = requests.get(request_url)
print(response.status_code)
print(response.text)
response_data = json.loads(response.text)

print(type(response_data))

grades = [d["finalGrade"] for d in response_data["students"]]

print("Grade: ",(grades))
avg_grade = statistics.mean(grades)
print("Avg Grade: ", avg_grade)

print("Min Grade: ", min(grades))

print("Avg Grade: ", max(grades))