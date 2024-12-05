from Add_Contacts import add_contact
from Save_File import save_all_contact
from View_All_Contacts import view_all_contacts
from Load_File import load_file
from Update_Contact import update_contact
from Remove_Contacts import remove_contact
from Search_Contacts import search_contact
from Duplicate_Numbers import duplicate_numbers


print("***** Welcome To Contact Management System *****")
contact_list = load_file()
print(f"Loaded {len(contact_list)} contacts from file.\n")

while True:
    print("@ Select any Option")
    print("1.Add contact")
    print("2.Remove contact")
    print("3.Search contact")
    print("4.Update contact")
    print("5.View All contact")
    print("6.Exit")

    option = int(input("- Enter any Option: "))
    print()
    if option==1:
        contact_list= add_contact(contact_list)
    elif option==2:
        contact_list=remove_contact(contact_list)
    elif option==3:
        contact_list=search_contact(contact_list)
    elif option==4:
        contact_list=update_contact(contact_list)
    elif option==5:
        view_all_contacts(contact_list)
    elif option==6:
        print("Thanks for using Contact Management System")
        print()
        break
    else:
        print("Invalid input")