import csv
import json

with open("config.txt", "r") as config:
    min_score = int(config.read())

print(min_score)
students=[]
with open("students.csv", "r",encoding="utf-8") as file:
    reader = list(csv.DictReader(file))
    for s in reader:
        s["score"] = int(s["score"])
        students.append(s)

retest_list=[]
for s in students:
    if s["score"] <= min_score:
        retest_list.append(s)

with open("retest.csv", "w", encoding="utf-8", newline="") as file:
    f = ["id", "name", "surname", "score"]
    writer = csv.DictWriter(file, fieldnames=f)
    writer.writeheader()
    for s in retest_list:
        writer.writerow(s)

success_list = []
for s in students:
    if s["score"] >= min_score:
        success_list.append(s)

for s in success_list:
    s["passed"] = True

with open("top_students.json", "w", encoding="utf-8") as json_file:
    json.dump(success_list, json_file, indent=4, ensure_ascii=False)


