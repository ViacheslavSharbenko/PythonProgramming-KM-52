import csv
songs = [
    {"Song": "In the End", "Year": 2000},
    {"Song": "Numb", "Year": 2003},
    {"Song": "Crawling", "Year": 2000},
    {"Song": "Faint", "Year": 2003},
    {"Song": "What I've Done", "Year": 2007},
    {"Song": "One More Light", "Year": 2017},
]
filename = "LinkingPark.csv"
with open(filename, "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Song", "Year"])
    writer.writeheader()  
    for i in songs:
        writer.writerow(i)

print("Файл:", filename)
with open(filename, "r", newline='', encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
