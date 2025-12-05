print('My cli project using python to push in github')

while True:
    print()
    print('1. Check Balance')
    print('2. Deposit Amount')
    print('3. Withdrawal Amount')
    print('4. Quit')
    print()

    ops = input('Enter number to do operation: ').strip()

    if ops.isalpha():
        print("Alphabets are denied!")
        break

    if ops.isnumeric():
        if ops == '1':
            print("Checking available balance...")

        elif ops == '2':
            print("Depositing the amount is in progress...")

        elif ops == '3':
            print('Withdrawing the amount is in progess...')

        elif ops == '4':
            print('Quitting the program...')
            break 

        else:
            print("Invalid credentials are passed...")
            break

    else:
        print("Non-numerics are denied!")
        break