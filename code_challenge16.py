def denomination(amount):
    print("\nDenomination Breakdown:")
    a = amount // 1000
    amount %= 1000

    b = amount // 500
    amount %= 500

    c = amount // 200
    amount %= 200

    d = amount // 100
    amount %= 100

    e = amount // 50
    amount %= 50

    f = amount // 20
    amount %= 20

    g = amount // 10
    amount %= 10

    h = amount // 5
    amount %= 5

    i = amount // 1

    print(f"1000--- {a}")
    print(f"500---- {b}")
    print(f"200---- {c}")
    print(f"100---- {d}")
    print(f"50----- {e}")
    print(f"20----- {f}")
    print(f"10----- {g}")
    print(f"5------ {h}")
    print(f"1------ {i}")


accounts = {}

def create_account():
    username = input("Enter a username: ")
    if username in accounts:
        print("Account already exists!")
    else:
        accounts[username] = 0
        print(f"Account created successfully for {username}.")


def deposit():
    username = input("Enter your username: ")
    if username in accounts:
        try:
            amount = int(input("Enter amount to deposit: "))
            if amount > 0:
                accounts[username] += amount
                print(f"Deposited {amount} successfully. New balance: {accounts[username]}")
                denomination(amount)
            else:
                print("Amount must be positive!")
        except ValueError:
            print("Invalid input! Please enter a whole number.")
    else:
        print("Account not found!")


def withdrawal():
    username = input("Enter your username: ")
    if username in accounts:
        try:
            amount = int(input("Enter amount to withdraw (whole numbers only): "))
            if 0 < amount <= accounts[username]:
                accounts[username] -= amount
                print(f"Withdrawn {amount} successfully. Remaining balance: {accounts[username]}")
                denomination(amount)
            else:
                print("Insufficient funds or invalid amount!")
        except ValueError:
            print("Invalid input! Please enter a whole number.")
    else:
        print("Account not found!")


def check_balance():
    username = input("Enter your username: ")
    if username in accounts:
        print(f"Your balance: {accounts[username]}")
    else:
        print("Account not found!")


def options():
    while True:
        print("\nBanking System")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            create_account()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdrawal()
        elif choice == '4':
            check_balance()
        elif choice == '5':
            print("Thank you for using the Banking System!")
            break
        else:
            print("Invalid option. Please try again.")

options()
