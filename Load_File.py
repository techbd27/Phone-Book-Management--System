import csv
def load_file():
    try:
        with open("Contact_List.csv", mode="r") as file:
            reader = csv.DictReader(file)
            return [contact for contact in reader]
    except FileNotFoundError:
        return []