class Trend:
    def __init__(self, F, L1, L2):
        self.F = F
        self.L1 = L1
        self.L2 = L2
        self.update_lower, self.update_upper = self.get_levels()
        self.under_thresh = False
        self.above_thresh = False
        self.threshold = 0.03

    def get_levels(self):
        if self.L1 == 0 and self.L2 == 23.6:
            return self.F.low.min(),  self.F.fib_23_6
        elif self.L1 == 23.6 and self.L2 == 38.2:
            return self.F.fib_23_6, self.F.fib_38_2
        elif self.L1 == 38.2 and self.L2 == 50:
            return self.F.fib_38_2 , self.F.fib_50_0
        elif self.L1 == 50 and self.L2 == 61.8:
            return self.F.fib_50_0, self.F.fib_61_8
        elif self.L1 == 61.8 and self.L2 == 76.4:
            return self.F.fib_61_8, self.F.fib_76_4
        else:
            return self.F.fib_76_4, self.F.high.max()

    def check_thresh(self, value):
        if value[4] - self.update_lower >= self.threshold or self.update_upper - value[4] >= self.threshold:
            return 2, 3
        if 0 <= value[4] - self.update_lower < self.threshold:
            return 1, 0
        elif 0 <= self.update_upper - value[4] < self.threshold:
            return 1, 1
        else:
            return 0, 3
