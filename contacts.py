contact = ''
delimiter = '-' * 30


def add():
    global contact
    print('\n----- Create new contact ----- ')
    contact = enter_contact_info()
    print(f'\nCongrats! Your new contact is:\n{contact}')
    print(delimiter)


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
    print('\n----- Search contact ----- ')

    keep_searching = True
    while keep_searching:
        search_substring = input('Start typing a name or a phone number: ')
        search_substring.lower() \
            .strip()

        prepared_contact = contact.lower()
        is_exist = prepared_contact.startswith(search_substring)

        if is_exist:
            print(contact)
        else:
            print("No results")

        keep_searching = input(f"\nWanna find anything else? "
                               f"Type 'y' for yes or press any key for 'no' ") == 'y'

    print(delimiter)


add()
search()
