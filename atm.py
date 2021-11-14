class ATM(object):
    def __init__(self, card_number, pin_number, money):
        self.card = card_number
        self.pin = pin_number
        self.money = money

    def CashWithdrawl(self):
        print(f"You have withdrawed {self.money} dollars.")

    def BalanceInquiry(self):
        balance = (self.card + self.pin)/500000+100
        balance = round(balance, 2)

        print(f"You currently have {balance} dollars.")

card = input("Enter your ATM card number: ")
pin = input("Enter your PIN number: ")
card = int(card)
pin = int(pin)

which = input('To withdraw cash, type "1", To check your balance inquiry, type "2": ')
which = int(which)

if (which == 1):
    money = input("Enter the amount of dollars to withdraw: ")
    money = int(money)

    atm = ATM(card, pin, money)
    atm.CashWithdrawl()

elif (which == 2):
    atm = ATM(card, pin, "")
    atm.BalanceInquiry()