name = ''


def add():
    global name
    name = input(f'New contact: ')
    name = name.strip()


def search():
    keep_searching = True

    while keep_searching:
        search_substring = input(f'\nStart typing a name: ')
        search_substring.lower() \
                        .strip()

        prepared_name = name.lower()
        is_exist = prepared_name.startswith(search_substring)

        if is_exist:
            print(name)
        else:
            print("No results")

        keep_searching = input(f"\nWanna find anything else? "
                               f"Type 'y' for yes or press any key for 'no'") == 'y'


add()
search()

