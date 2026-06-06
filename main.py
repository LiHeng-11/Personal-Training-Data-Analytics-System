import csv

date = input("Date (DD-MM-YYYY): ")
distance = input("Distance (e.g. 100m): ")
time = input("Time in seconds: ")

with open("data.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([date, distance, time])

print("Sprint data saved!")