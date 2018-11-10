class Trade:
    def __init__(self, F, value):
        self.F = F
        self.value = value
        self.lower, self.upper = self.detect_levels()


    def detect_levels(self):
        v = self.value[4]
        print(v)

        if v > self.F.low.min() and v <= self.F.fib_23_6:
            return  self.F.low.min(), self.F.fib_23_6
        elif v > self.F.fib_23_6 and v <= self.F.fib_38_2:
            return self.F.fib_23_6, self.F.fib_38_2
        elif v > self.F.fib_38_2 and v <= self.F.fib_50:
            return self.F.fib_38_2, self.F.fib_50
        elif v > self.F.fib_50 and v <= self.F.fib_61_8:
            return self.F.fib_50, self.F.fib_61_8
        elif v > self.F.fib_61_8 and v <= self.F.fib_76_4:
            return self.F.fib_61_8, self.F.fib_76_4
        else:
            return self.F.fib_76_4, self.F.high.max()
