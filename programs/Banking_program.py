def showbalance(balance):
    print("******************************")
    print(f"Your balance is ${balance:.2f}")
    

def deposit():
    print("******************************")
    amount = float(input("Enter the amount you want to deposit: $"))
    print("******************************")
    if amount < 0:
        print("That's not a valid amount")
        return 0
    else:
        return amount
    
def withdraw(balance):
    amount = float(input("Enter amount to withdraw: $"))

    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount
        
def main():
    balance = 0
    is_running = True

    while is_running:
        print("******************************")
        print("       Banking program        ")
        print("******************************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("******************************")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            showbalance(balance)

        elif choice == '2':
            amount = deposit()
            balance += amount     

        elif choice == '3':
            amount = withdraw(balance)
            balance -= amount     

        elif choice == '4':
            is_running = False

        else:
            print("Invalid input")

main()
