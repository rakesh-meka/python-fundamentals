#Question :  Why do we use Abstraction in Python? Explain with one scenario ?

from abc import ABC, abstractmethod

#Payment system where each payment type must implement its own logic.
# Abstraction ensures a common contract while allowing different implementations.

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UpiPayment(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


# -------- Usage --------
payment1 = CreditCardPayment()
payment2 = UpiPayment()

payment1.pay(1000)
payment2.pay(500)
