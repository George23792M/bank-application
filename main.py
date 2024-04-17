from Address import Address
from Utils import is_blank
from BusinessTransactions import deposit, draw_money, check_balance


def welcome():
    print(f'Welcome to MY BANK\n')
    try:
        validate_name()
        local_address = validate_address()

        if local_address is not None:
            options_select = {1: "Deposit Cash", 2: "With Draw money", 3: "Check balance"}

            for key, value in options_select.items():
                print(f'{key} : {value}')

            user_input = int(input(f'What would like to do today? '))

            if user_input in options_select.keys():
                deposit()

            elif user_input in options_select.keys():
                draw_money()

            elif user_input in options_select.keys():
                check_balance()

    except Exception as exception:
        print(f'oops an exception occurred : ', exception)


def validate_name():
    print(f'First Name:')
    first_name = str(input()).lower()
    if is_blank(first_name):
        raise Exception("First Name is emtpy")

    print(f'Last Name:')
    last_name = str(input()).lower()
    if is_blank(last_name):
        raise Exception("Last Name is empty")

    print(f'Hi, {first_name} {last_name}!!!\n')


def validate_address():
    print(f'Street:')
    street = input(str())

    if is_blank(street):
        raise Exception("Street is empty")

    print(f'City:')
    city = input(str())

    if is_blank(city):
        raise Exception("City is empty")

    print(f'State:')
    state = input(str())

    if is_blank(state):
        raise Exception("State is empty")

    print(f'Zip Code:')
    postalCode = input(str())

    if is_blank(postalCode):
        raise Exception("Zip code is empty")

    address = Address(street, city, state, postalCode)

    return address


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    welcome()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
