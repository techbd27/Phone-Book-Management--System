def update_contact(contact_list):
    if not contact_list:
        print("No Contact available to update.")
        return contact_list
    updatenumber = int(input("Enter your Phone Number you want to Update: "))
    for contact in contact_list:
        if int(contact['Phone Number']) == updatenumber:
            print("\nContact Found")
            print("Current Contact Details:")
            print(f"Name: {contact['Name']}")
            print(f"Email: {contact['Email']}")
            print(f"Phone Number: {contact['Phone Number']}")
            print(f"Address: {contact['Address']}")
 
            contact['Name'] = input("Enter New Name: ") or contact['Name']
            contact['Email'] = input("Enter New Email: ") or contact['Email']
            contact['Address'] = input("Enter New Address: ") or contact['Address']

            print("Contact LIst Updated")
            return contact_list

    print("No Contact found in List")
    return contact_list