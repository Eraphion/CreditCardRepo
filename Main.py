class CreditCard:
    def __init__(self, current):
        self.balance = current

    def buy_stuff(self, prices):
        i = 0
        for i in prices:
            print("��������� �������: " + str(i))
            self.balance -= i
            print("�������� �� �����: " + str(self.balance))


if __name__ == "__main__":
    cd = CreditCard(500)
    cd.buy_stuff([50,30,120])