import numpy as np
import csv
import queue
from numpy import genfromtxt
from Fibonacci import Fibonacci as Fib
from Trade import Trade as T
from Levels import Levels as L
from Trend import Trend as TR


#with open("EURUSD_Candlestick_1_M_BID_01.10.2018-31.10.2018.csv", 'r') as csvfile:
 #   reader = np.array(csv.reader(csvfile))

my_data = genfromtxt("EURUSD_Candlestick_1_M_BID_01.10.2018-31.10.2018.csv", delimiter=',')
trend = [0] * 3
trend = []
level = None


for i in range(1):
    window = my_data[i:240+i]
    fibonacci = Fib(window)
    if i > 0:
        trend = TR(fibonacci, level.L1, level.L2)
        level.lower = trend.update_lower
        level.upper = trend.update_upper
        check = trend.check_thresh(window[-1])
        if check == 2:
            trend = []
        else:
            trend.append(check)

    if i is 0:
        level = L(fibonacci, window[-1])

    if len(trend) >= 3:
        if sum(trend[:3]) > 1:
            T.trade()
            trend = []
        else:
            level = L(fibonacci, window[-1])
            trend = []

    print(level.L1, "--", level.L2)









