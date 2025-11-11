import simple_banking_app

if __name__ == "__main__":

    bank1 = simple_banking_app.Bank()
    print(bank1.check_balance())


    while True:
        print("\n 1 . check balance  \n 2. Diposite \n 3. Withdrow  \n Exit")
        choice = input("Enter choice 1,2,3,4:").strip()
        if choice == "1":
            print("Balance:", bank1.check_balance())
        elif choice == "2":
            try:
                amt = float(input("Amount to deposit: ").strip())
                print("Balance:", bank1.deposit(amt))
            except ValueError:
                print("Enter a number")
        elif choice == "3":
            try:
                amt = float(input("Amount to withdraw: ").strip())
                print("Result:", bank1.withdraw(amt))
            except ValueError:
                print("Enter a number")
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice")
