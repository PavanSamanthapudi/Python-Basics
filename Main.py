
"""
Assignment : 

Create a Payment Processing System for a store and follow OOP.

- The system should enable store to add cash(online) in their system using CreditCard or UPI

- The system should also have functionality to refund to customers

- The system should have functionality to show balance

- The system should have functionality to check history

Terminal : uv run python main.py
Welcome to Payment system:
Press 1 for Add cash to the system
Press 2 to refund the money
Press 3 check balance
Press 4 to check the transcation
Press 5 to exit the system

if user press 1 : Want to use credit card or UPI : 1 of C, 2 UPI
if user press 2 : enter amount to refund : subtract the amount from system credit
if user press 3 :
if user press 4 : show the history but with good format in terminal

The code should be robust, running in while loop, should handle user input and type casting, should have exception handling + All OOPS concept + modules & package creation is (optional)
"""

from abc import ABC, abstractmethod

class abstractPaymentProcessor(ABC):
    
    @abstractmethod
    def add_cash(self):
        pass

    @abstractmethod
    def refund_cash(self):
        pass

    @abstractmethod
    def show_balance(self):
        pass
    
    @abstractmethod
    def show_history(self):
        pass

class PaymentProcessor(abstractPaymentProcessor):

    def __init__(self):
       pass
    
    def add_cash(self):
        print("Add Cash")
     
    def refund_cash(self):
        print("Refund Cash")

    def show_balance(self):
        print("Show Balance")

    def show_history(self):
        print("Show History")

    def payment_system(self):
        self.welcome_msg = "Welcome to Payment system:\nPress 1 for Add cash to the system\nPress 2 to refund the money\nPress 3 check balance\nPress 4 to check the transcation\nPress 5 to exit the system"
        #print(f"Welcome to Payment system:\nPress 1 for Add cash to the system\nPress 2 to refund the money\nPress 3 check balance\nPress 4 to check the transcation\nPress 5 to exit the system":>20)
        print(f"{self.welcome_msg:>40}")
        
        #user_input = int(input("Wecome "))

p = PaymentProcessor()
p.payment_system()
