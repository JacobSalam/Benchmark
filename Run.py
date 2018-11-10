import numpy as np
import csv
from numpy import genfromtxt
from Fibonacci import Fibonacci as Fib
from Trade import Trade as T


#with open("EURUSD_Candlestick_1_M_BID_01.10.2018-31.10.2018.csv", 'r') as csvfile:
 #   reader = np.array(csv.reader(csvfile))

my_data = genfromtxt("EURUSD_Candlestick_1_M_BID_01.10.2018-31.10.2018.csv", delimiter=',')

window = my_data[:240]
fibonacci = Fib(window)
trade = T(fibonacci, window[-1])

print(trade.lower, trade.upper)







