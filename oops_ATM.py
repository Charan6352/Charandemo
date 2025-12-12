class atm():
    def __init__(self):
       self.balance = 0

    def atm_menu(self):
        print("\nATM Menu:")
        print("1. Credit")
        print("2. Debit")
        print("3. Balance")
        print("4. Exit")
    
    def credit(self):
        amount = float(input("Enter amount to credit: "))
        if amount <= 0:
            print("Please enter a positive amount.")
        else:
            self.balance += amount
            print(f"${amount} credited to your account.")

    def debit(self):
        amount = float(input("Enter amount to debit: "))
        if amount <= 0:
            print("Please enter a positive amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"${amount} debited from your account.")
    def atm_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def exit1(self):
        print("Thank you for using the ATM. Goodbye!")
        return {
             "status":"successfull"
        }
    def run(self):
     
     while True:
        self.atm_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            self.credit()
        elif choice == "2":
            self.debit()
        elif choice == "3":
           self.atm_balance()
        elif choice == "4":
           self.exit1()
           break

atm1 = atm()
atm1.run()