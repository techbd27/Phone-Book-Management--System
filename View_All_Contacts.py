def view_all_contacts(contact_list):
    print(f"Loaded {len(contact_list)} contacts from file.\n")
    if contact_list != [] :
            for index, contact in enumerate(contact_list, start=1):
                print(f"Contact Details {index}: Name: {contact['Name']} | Email: {contact['Email']} | Phone Number: {contact['Phone Number']} | Address: {contact['Address']}")
            #print(f"Name: {contact['Name']} | Email: {contact['Email']} | Phone Number: {contact['Phone Number']} | Address: {contact['Address']}")     
    else:
        print("No contacts in the list.")
        return contact_list