def read_and_print_file(file_to_read):
    file = open(f'{file_to_read}', 'r')
    file_content = file.read()
    print(file_content)
    file.close()


def print_welcome():
    read_and_print_file('welcome_message.txt')


def check_string_in_file(string_to_check, file_to_read):
    print(f'\nChecking if {string_to_check} existing in the file {file_to_read}')
    print(f'Printing a content of {file_to_read}:')
    read_and_print_file(file_to_read)

    with open(f'{file_to_read}') as file:
        if f'{string_to_check}' in file.read():
            print(f'\n{string_to_check} is existing in {file_to_read}')
        else:
            print(f'\n{string_to_check} is not existing in {file_to_read}')


print_welcome()
check_string_in_file('Alex', 'file.txt')
check_string_in_file('NoName', 'file.txt')
