def deposit():
    print(f'Lets Deposit your cash\n')

    success_message = 'Your transaction is completed successfully'

    max_retries_reached = 'You have reached max retries'

    YES = 'YES'

    NO = 'NO'

    amount_verified = enter_amount()

    if amount_verified == YES:
        print(success_message)

    if amount_verified == NO:
        count = 0

        while count <= 3:
            message = enter_amount()

            if message == YES:
                print(success_message)
                break

            if message == NO:
                count = count + 1
                if count >= 3:
                    raise Exception(max_retries_reached)


def enter_amount():
    print(f'Enter amount that you would like to deposit: ')

    user_input = int(input())

    if user_input > 0:
        print(f'You have entered, {user_input}\n')

        confirm_transaction = ('YES', 'NO')

        for item in confirm_transaction:
            print(item)

        message = str(input(f'Please type above options to confirm your transaction: \n')).upper()

        return message
    else:
        raise Exception('Amount entered is incorrect')


def draw_money():
    print(f'Lets With Drawy some money to spend')


def check_balance():
    print(f'Lets check your current balance')
