import datetime

# --- Abstraction & Inheritance ---
class PaymentMethod:
    """Base class for payment methods"""
    def __init__(self, name):
        self.name = name

    def process(self, amount):
        # In a real system, this would connect to an API
        return True

class CreditCard(PaymentMethod):
    def __init__(self):
        super().__init__("Credit Card")

class UPI(PaymentMethod):
    def __init__(self):
        super().__init__("UPI")

# --- Transaction Model ---
class Transaction:
    """Represents a single transaction record"""
    def __init__(self, tx_type, amount, method="N/A"):
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.tx_type = tx_type  # 'ADD' or 'REFUND'
        self.amount = amount
        self.method = method

    def __str__(self):
        return f"{self.timestamp} | {self.tx_type:<7} | {self.method:<12} | ${self.amount:>8.2f}"

# --- Core System (Encapsulation) ---
class PaymentSystem:
    def __init__(self):
        self.__balance = 0.0  # Private attribute
        self.__history = []   # Private list

    def add_funds(self, amount, method_choice):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        
        method = CreditCard() if method_choice == '1' else UPI()
        
        if method.process(amount):
            self.__balance += amount
            tx = Transaction("ADD", amount, method.name)
            self.__history.append(tx)
            print(f"\nSuccessfully added ${amount:.2f} via {method.name}.")

    def refund(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient balance for this refund.")

        self.__balance -= amount
        tx = Transaction("REFUND", amount)
        self.__history.append(tx)
        print(f"\nRefund of ${amount:.2f} processed successfully.")

    def get_balance(self):
        return self.__balance

    def show_history(self):
        print("\n" + "="*55)
        print(f"{'Date & Time':<19} | {'Type':<7} | {'Method':<12} | {'Amount'}")
        print("-" * 55)
        if not self.__history:
            print("No transactions found.")
        else:
            for tx in self.__history:
                print(tx)
        print("="*55)

# --- CLI Application ---
def main():
    system = PaymentSystem()
    
    while True:
        print("\n--- Welcome to Payment System ---")
        print("1. Add cash to the system")
        print("2. Refund money")
        print("3. Check balance")
        print("4. Check transaction history")
        print("5. Exit")
        
        choice = input("\nSelect an option (1-5): ").strip()

        try:
            if choice == '1':
                print("\nPayment Methods: [1] Credit Card, [2] UPI")
                m_choice = input("Select method: ").strip()
                if m_choice not in ['1', '2']:
                    print("Error: Invalid payment method.")
                    continue
                
                amt = float(input("Enter amount to add: "))
                system.add_funds(amt, m_choice)

            elif choice == '2':
                amt = float(input("Enter amount to refund: "))
                system.refund(amt)

            elif choice == '3':
                print(f"\n>>> Current System Balance: ${system.get_balance():.2f}")

            elif choice == '4':
                system.show_history()

            elif choice == '5':
                print("Exiting system. Goodbye!")
                break
            
            else:
                print("Invalid choice! Please select between 1-5.")

        except ValueError as e:
            print(f"\nInput Error: {e}. Please enter a valid number.")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()