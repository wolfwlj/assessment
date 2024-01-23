import os
import sys
import json


'''
print all contacts in the following format:
======================================
Position: <position>
First name: <firstname>
Last name: <lastname>
Emails: <email_1>, <email_2>
Phone numbers: <number_1>, <number_2>
'''


def display(addressbook: list):

    return


'''
return list of contacts sorted by first_name or last_name [if blank then unsorted], direction [ASC (default)/DESC])
'''


def list_contacts(addresses, sortby, direction):
    addressbook = addresses

    def sort_key(contact):
        if sortby == 'first_name':
            return contact['first_name']
        elif sortby == 'last_name':
            return contact['last_name']
        else:
            return None

    addressbook.sort(key=sort_key, reverse=direction == 'DESC')

    for contact in addressbook:
        print("======================================")
        print(f"Position: {contact['id']}")
        print(f"First name: {contact['first_name']}")
        print(f"Last name: {contact['last_name']}")

        print("Emails: ", end="")
        for email in contact['emails']:
            if email != contact['emails'][0]:
                print(f", {email}", end="")
            else:
                print(f"{email}", end="")
        print("")

        print("Phone numbers: ", end="")
        for number in contact['phone_numbers']:
            if number != contact['phone_numbers'][0]:
                print(f", {number}", end="")
            else:
                print(f"{number}", end="")
        print("")

    return addressbook


'''
add new contact:
- first_name
- last_name
- emails = {}
- phone_numbers = {}
'''


def add_contact(hoogste_id):

    while True:
        firstname = input("First name: ")
        lastname = input("Last name: ")
        if firstname.isalpha() and lastname.isalpha():
            break
        else:
            print("voer een geldige naam in")

    emails = []
    phonenumbers = []
    emailset = set()

    while True:
        email = input("Email: ")
        if email != "" and '@' in email and email not in emailset:
            emailarr = email.split(', ')
            for email in emailarr:
                emailset.add(email)
            for email in emailset:
                emails.append(email)

            break
        elif email == "":
            break
        else:
            print("voer een geldige email in")

    while True:
        phonenumber = input("Phone number: ")
        if phonenumber != "":
            phonenumbers.append(phonenumber)
            break
        else:
            break

    contact = {
        "id": hoogste_id + 1,
        "first_name": firstname,
        "last_name": lastname,
        "emails": emails,
        "phone_numbers": phonenumbers
    }

    return contact


'''
remove contact by ID (integer)
'''


def remove_contact(contact_id, contacts):
    for contact in contacts:
        if contact['id'] == int(contact_id):
            contacts.remove(contact)
            print("contact verwijderd :)")
            break
    write_to_json('contacts.json', contacts)

    return contacts


'''
merge duplicates (automated > same fullname [firstname & lastname])
'''


def merge_contacts(contacts):
    merged_contact = {
        "id": 0,
        "first_name": "",
        "last_name": "",
        "emails": [],
        "phone_numbers": []
    }
    ids_merged = set()

    for contact in contacts:
        for inner_contact in contacts:
            if (contact['id'] != inner_contact['id'] and contact['id'] not in ids_merged
                    and inner_contact['id'] not in ids_merged):
                if (contact['first_name'] == inner_contact['first_name']
                        and contact['last_name'] == inner_contact['last_name']):

                    highest_id = min(contact['id'], inner_contact['id'])

                    merged_contact['id'] = highest_id
                    merged_contact['first_name'] = contact['first_name']
                    merged_contact['last_name'] = contact['last_name']
                    merged_contact['emails'] = contact['emails'] + inner_contact['emails']
                    merged_contact['phone_numbers'] = contact['phone_numbers'] + inner_contact['phone_numbers']

                    ids_merged.add(contact['id'])
                    ids_merged.add(inner_contact['id'])

    for identifier in ids_merged:
        for contact in contacts:
            if contact['id'] == identifier:
                contacts.remove(contact)

    contacts.append(merged_contact)

    return contacts


'''
read_from_json
Do NOT change this function
'''


def read_from_json(filename) -> list:
    addressbook = list()
    # read file
    with open(os.path.join(sys.path[0], filename)) as outfile:
        contact_data = json.load(outfile)
        # iterate over each line in contact_data and call the add function
        for contact in contact_data:
            addressbook.append(contact)

    return addressbook


'''
write_to_json
Do NOT change this function
'''


def write_to_json(filename, addressbook: list) -> None:

    json_object = json.dumps(addressbook, indent=4)

    with open(os.path.join(sys.path[0], filename), "w") as outfile:
        outfile.write(json_object)


'''
addressbook_program function:
# build menu structure as following
# the input can be case-insensitive (so E and e are valid inputs)
# [L] List contacts
# [A] Add contact
# [R] Remove contact
# [M] Merge contacts
# [Q] Quit program
Don't forget to put the contacts.json file in the same location as this file!
'''


def addressbook_program(json_file):
    addressbook = read_from_json(json_file)

    contacts = []
    for contact in addressbook:
        contacts.append(contact)

    while True:
        actie = input("""[L] List contacts
[A] Add contact
[R] Remove contact
[M] Merge contacts
[Q] Quit program""")

        if actie.lower() == 'l':
            sortby = 'first_name'
            direction = 'ASC'
            # sortbyoptie = input("""Sort by: [F]irst name, [L]ast name, [N]o sort""")

            # if sortbyoptie.lower() == 'l':
            #     sortby = 'last_name'

            # directionoptie = input("""Sort direction: [A]scending, [D]escending""")

            # if directionoptie.lower() == 'd':
            #     direction = 'DESC'

            list_contacts(contacts, sortby, direction)

        elif actie.lower() == 'a':

            hoogste_id = 0

            for contact in contacts:
                if contact['id'] > hoogste_id:
                    hoogste_id = contact['id']

            nieuwcontact = add_contact(hoogste_id)
            contacts.append(nieuwcontact)
            write_to_json('contacts.json', contacts)

            print("contact toegevoegd :)")

        elif actie.lower() == 'r':
            print('e')
            ingevoerde_id = input("ID: ")
            updated_contacts = remove_contact(ingevoerde_id, contacts)
            contacts = updated_contacts

        elif actie.lower() == 'm':
            merged_contacts = merge_contacts(contacts)
            contacts = merged_contacts
            write_to_json('contacts.json', contacts)
            print("contacten gemerged :)")

        elif actie.lower() == 'q':
            break
        else:
            print("verkeerde input")


'''
calling addressbook_program function:
Do NOT change it.
'''
if __name__ == "__main__":
    addressbook_program('contacts.json')