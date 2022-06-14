DELIMITER = '\n' + '-' * 30
all_contacts = ['abc 94587694576',
                'znxcvnx 127352',
                'abcrty 1234567',
                'test 09586709']


def add():
    print('\n----- Create new contact ----- ')
    contact = enter_contact_info()
    all_contacts.append(contact)

    print(f'\nCongrats! Your new contact is:\n{contact}')
    print(DELIMITER)
    return contact


def delete():
    print('\n----- Delete contact ----- ')

    if len(all_contacts) == 0:
        print('Contact list is empty')
        return

    show_contacts(all_contacts)

    index = int(input('Enter index number of the contact: '))
    while index < 1 or index > len(all_contacts):
        index = int(input('The index is incorrect. Try again: '))

    contact = all_contacts[index - 1]
    all_contacts.remove(contact)
    print(f"\nYou're right! {contact} doesn't deserve to be on your contact list.")
    print(DELIMITER)


def enter_contact_info():
    while True:
        name = input('Name: ').strip()
        phone_number = input('Phone number: ').strip()

        if name == '' or phone_number == '':
            print('\nThe name or the phone number is empty. Try again: ')
        elif not phone_number.isnumeric():
            print('\nPhone number must contain only digits. Try again: ')
        else:
            return name + ' ' + phone_number


def search():
    print('\n------- Search contact ------- ')

    search_substring = input('Start typing a name or a phone number: ')
    result = []
    for contact in all_contacts:
        if matches(contact, search_substring):
            result.append(contact)

    if len(result) == 0:
        print('No results')
    else:
        show_contacts(result)
    print(DELIMITER)


def matches(contact: str, substring):
    substring = substring.strip().lower()
    contact = contact.lower()
    name, number = contact.split(' ')
    return matches_by_name(name, substring) or \
           matches_by_number(number, substring)


def matches_by_name(name, substring):
    return name.startswith(substring)


def matches_by_number(num: str, substring):
    result = num.find(substring)
    return result != -1


def show_contacts(contacts: list):
    print('\n-------- All contacts -------- ')
    for i, contact in enumerate(contacts):
        print(f'{i + 1}.', contact)
    print(DELIMITER)


def ask_action():
    return input("\nWanna do anything else? Type 'y' for yes or press any key for 'no' ").lower() == 'y'


def manage_contacts():
    while True:
        action = input("""Choose your action:\n\n
                           Show contacts list (type l)\n
                           Search contact (type s)\n
                           Add new contact (type n)\n
                           Delete contact (type d)\n
                           Exit (type e)\n""").lower()
        match action:
            case 'l':
                show_contacts(all_contacts)
            case 's':
                search()
            case 'n':
                add()
            case 'd':
                delete()
            case 'e':
                break
            case _:
                print('Try again')
                continue
        if not ask_action():
            break


if __name__ == '__main__':
    manage_contacts()
