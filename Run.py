import numpy as np
import csv
import queue
from numpy import genfromtxt
from Fibonacci import Fibonacci as Fib
from Trade import Trade as T
from Levels import Levels as L


#with open("EURUSD_Candlestick_1_M_BID_01.10.2018-31.10.2018.csv", 'r') as csvfile:
 #   reader = np.array(csv.reader(csvfile))

my_data = genfromtxt("EURUSD_Candlestick_1_M_BID_01.10.2018-31.10.2018.csv", delimiter=',')
trend = [0] * 3
trend_queue = queue.Queue()
level = None


for i in range(1):
    window = my_data[i:240+i]
    fibonacci = Fib(window)

    if level is not None:
        value = window[-1][4]

        f_L1 =


    if i == 0:
        level = L(fibonacci, window[-1])

    if i != 0 and trend_queue.qsize() == 3:
        level = L(fibonacci, window[-1])

    print(level.L1, "--", level.L2)









