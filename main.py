import csv


Intro = (
    'Welcome to Training! \n'
    '1. New Training \n'
    '2. View Training \n'
    '3. Exit'
)
print(Intro)
def main():
    if input == "1":
       return new_training()
    if input == "2":
       return view_training()
    if input == "3":
       return exit_program()
    else:
       print("Invalid input. Please try again.")

      
def new_training():
    date = input("Date (DD-MM-YYYYgit remote): ")
    distance = input("Distance (e.g. 100m): ")
    time = input("Time in seconds: ")

    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, distance, time])

    print("Sprint data saved!")

def view_training():
    pass
def exit_program():
    print("Exiting the program. Goodbye!")
    exit()
