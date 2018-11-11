class Trade:
    def __init__(self, value, balance_EUR, balance_USD, bound):
        self.value = value[4]
        self.limit = 0
        self.balance_EUR = balance_EUR
        self.balance_USD = balance_USD
        self.bound = bound
        self.limit, self.stop_loss = self.buy_or_sell()
        # print(self.balance_USD, self.balance_EUR)
        # print("self.value", self.value)
        # print("self.limit", self.limit)
        # print("self.bound", self.bound)

    def buy_or_sell(self):
        if self.bound == 0 and self.balance_USD > 0:
            return self.value - 0.00001, self.value - 0.0003
        elif self.bound == 1 and self.balance_EUR > 0:
            print("gets here")
            return self.value + 0.00001, self.value + 0.0003
        else:
            return 0, 0
