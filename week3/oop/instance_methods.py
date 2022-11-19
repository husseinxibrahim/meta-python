class Payslips():
    def __init__(self,name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = "yes"

    def status(self):
        if self.payment == "yes":
            return self.name + " is Paid: " + str(self.amount)
        else:
            return self.name + " is not paid"

nathan = Payslips("Nathan", "No", 1000)
roger = Payslips("Roger", "No", 3000)

print(nathan.status(),"\n", roger.status())

print("After Payment:")
nathan.pay()

print(nathan.status(),"\n", roger.status())
