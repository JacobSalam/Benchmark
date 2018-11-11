class Buy_And_Sell:
    def __init__(self, value, limit, stop, balance_EUR, balance_USD):
        self.value = value[4]
        self.limit = limit
        self.stop = stop
        self.balance_USD = balance_USD
        self.balance_EUR = balance_EUR
        self.balance_EUR, self.balance_USD, self.lower = self.calculate_new_balance()

    def calculate_new_balance(self):
        if self.balance_EUR != 0 and self.value <= self.limit:
            return 0, self.limit * self.balance_EUR, True
        elif self.balance_USD != 0 and self.value >= self.limit:
            return self.balance_USD * (1 / self.limit), 0, True
        else:
            return self.balance_EUR, self.balance_USD, False

    def activate_stop_loss(self, val):
        if self.lower and val < self.stop:
            return self.balance_USD * (1 / self.stop), 0, True
        elif not self.lower and val > self.stop:
            return 0, self.stop * self.balance_EUR, True
        else:
            return self.balance_EUR, self.balance_USD, False
