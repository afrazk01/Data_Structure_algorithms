class ATM:
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.pass_set = False
        self.menu = self.menu()

    def set_pin(self):

        user_input = input("Please Enter a Pin: ")

        if len(user_input) >= 1:

            self.pin = user_input
            balance = input("Please Deposit some balance: ")
            if type(balance) == str:
                try:
                    balance = int(balance)
                    self.balance = balance
                    self.pass_set = True
                except:
                    print("Enter Proper Balance and Pin")
                    self.pass_set = False
                    self.set_pin()
                    

        elif self.pass_set == False:
            print("Please Set a Password")
            self.set_pin()

    def check_balance(self):
        if self.balance <= 0:
            print(f"Your Balance is {self.balance}, Please Deposit some amount")

        if self.pin:
            check_pin = input("Please Enter The Pin: ")
            if self.pin == check_pin:
                print(f"Your Total Balance to withdraw is {self.balance}")
            else:
                print("Please Enter Correct Pin")
                self.check_balance()
        elif self.set_pin == False:
            print("Please set Pin and Balance First")
    
    def withdraw(self):
    
        if self.pass_set:
            pin = input("Please Enter Your Pin")
            if self.pin == pin:
                amount = int(input("Please Enter the amount to withdraw"))
                if self.balance > amount:
                    self.balance = self.balance - amount
                    print(f"{amount} Withdrawn Your new balance is {self.balance}")
                elif amount > self.balance:
                    print("Please Enter amount less or equal to balance")
                elif type(amount) != int:
                    print("Please Enter a valid amount")
    def change_pin(self):
        if self.pass_set:
            old_pin = input("Please Enter Old pin")
            if self.pin == old_pin:
                new_pin = input("Please enter new pin")
                self.pin = new_pin
            else:
                print("Wrong Password Retry")
        else:
            print("Please set a pin first")
            
    def menu(self):

        show = '''
        Welcome to CLI ATM
        1- : Press 1 to set Pin
        2- : Press 2 to check Balance
        3- : Press 3 to Withdraw Amont
        4- : Press 4 to Change Pin
        5- : Press 5 to Quit 
        '''
        show_menu = input("Press 1 to show Menu: ")
        if show_menu == '1':
            print(show)
        if show_menu != '1':
            print("Enter Proper Operation to show menu")
            self.menu()
        user_input = input("Enter Your Operation : ")
        if user_input == '1':
            self.set_pin()
            self.menu()
        elif user_input == '2':
            self.check_balance()
            self.menu()
        elif user_input == '3':
            self.withdraw()
            self.menu()
        elif user_input == '4':
            self.change_pin()
            self.main()
        elif user_input == '5':
            quit()
    

if __name__ == '__main__':
    obj = ATM()
    obj.set_pin()
        
        