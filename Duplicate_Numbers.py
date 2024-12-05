import csv

def duplicate_numbers(contact_list, phone_number):
    for contact in contact_list:
        if contact['Phone Number'] == phone_number:
            return True  

    try:
        with open("Contact_List.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for contact in reader:
                if int(contact['Phone Number']) == phone_number:  
                    return True  
    except FileNotFoundError:
        pass  

    return False 