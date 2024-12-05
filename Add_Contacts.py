from Save_File import save_all_contact
from Duplicate_Numbers import duplicate_numbers

def add_contact(contact_list):
    while True:
        try:
            name = str(input("Enter your name: "))
            if not name.isalpha():
                raise ValueError("Use alphabets")
            break
        except ValueError as e:
            print(f"Invalid name: {e}")

    email = str(input("Enter your email: "))

    while True:
        try:
            phone_number = int(input("Enter your phone number: "))
            break  
        except ValueError:
            print("Invalid phone number. Please enter a valid number.")
    address = str(input("Enter your address: "))
    
    if duplicate_numbers(contact_list, phone_number):
        print("Use Different. This phone number already exists.")
        print()
        return contact_list

    contact = {
        "Name": name,
        "Email": email,
        "Phone Number": phone_number,
        "Address": address
    }
    contact_list.append(contact)
    save_all_contact(contact_list)
    print("COntact Added Successfully")
    print()
    
    return contact_list