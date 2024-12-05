import csv

def save_all_contact(contact_list):
    with open("Contact_List.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Email", "Phone Number", "Address"])
        for contact in contact_list:
            writer.writerow([contact["Name"], contact["Email"], contact["Phone Number"], contact["Address"]])
            