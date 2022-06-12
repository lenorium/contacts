DELIMITER = '\n' + '-' * 30
contacts = ['abc 94587694576',
            'znxcvnx 127352',
            'abcrty 1234567']


def add():
    print('\n----- Create new contact ----- ')
    contact = enter_contact_info()
    contacts.append(contact)

    print(f'\nCongrats! Your new contact is:\n{contact}{DELIMITER}')
    return contact


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


def search(contact: str):
    print('\n------- Search contact ------- ')

    keep_searching = True
    while keep_searching:
        search_substring = input('Start typing a name or a phone number: ')\
            .strip()\
            .lower()
        prepared_contact = contact.lower()
        contact_info = prepared_contact.split(' ')
        is_present = search_by_name(contact_info[0], search_substring)
        if not is_present:
            is_present = search_by_number(contact_info[1], search_substring)

        print(contact if is_present else 'No results')

        keep_searching = input(f"\nWanna find anything else? "
                               f"Type 'y' for yes or press any key for 'no' ") == 'y'

    print(DELIMITER)


def search_by_name(name, substring):
    return name.startswith(substring)


def search_by_number(num: str, substring):
    result = num.find(substring)
    return result != -1


def show_contacts():
    print('\n-------- All contacts -------- ')
    print(*contacts, sep='\n')
    print(DELIMITER)


def manage_contacts():
    contact = add()
    show_contacts()
    search(contact)


if __name__ == '__main__':
    manage_contacts()
