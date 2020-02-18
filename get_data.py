import json
import requests
import statistics

print("REQUESTING SOME DATA FROM THE INTERNET...")
request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/1.json"
response = requests.get(request_url)
print(response.status_code)
print(response.text)
response_data = json.loads(response.text)

print(type(response_data)) #> <class 'list'> or <class 'dict'>





#request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json"
#response = requests.get(request_url)
#print(response.status_code)
#print(response.text)
#response_data = json.loads(response.text)
#print (type(response_data))
#
#for d in response_data:
#    print("name: " + d["name"] + " id: " + str(d["id"]))


#request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json"
#response = requests.get(request_url)
#print(response.status_code)
#print(response.text)
#response_data = json.loads(response.text)
#
#print(type(response_data))
#
#grades = [d["finalGrade"] for d in response_data["students"]]
#
#print("Grade: ",(grades))
#avg_grade = statistics.mean(grades)
#print("Avg Grade: ", avg_grade)
#
#print("Min Grade: ", min(grades))
#
#print("Avg Grade: ", max(grades))
##{
##  "downloadDate": "2018-06-05",
##  "professorId": 123,
##  "students":[
##    {"studentId": 1, "finalGrade": 76.7},
##    {"studentId": 2, "finalGrade": 85.1},
##    {"studentId": 3, "finalGrade": 50.3},
##    {"studentId": 4, "finalGrade": 89.8},
##    {"studentId": 5, "finalGrade": 97.4},
##    {"studentId": 6, "finalGrade": 75.5},
##    {"studentId": 7, "finalGrade": 87.2},
##    {"studentId": 8, "finalGrade": 88.0},
##    {"studentId": 9, "finalGrade": 93.9},
##    {"studentId": 10, "finalGrade": 92.5}
##  ]
##}
##