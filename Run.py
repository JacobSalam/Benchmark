from numpy import genfromtxt
from Fibonacci import Fibonacci as Fib
from Trade import Trade as T
from Levels import Levels as L
from Trend import Trend as TR
from Buy_And_Sell import Buy_And_Sell as BAS

my_data = genfromtxt("EURUSD_Candlestick_1_M_BID_01.10.2018-31.10.2018.csv", delimiter=',')
trend_array = []
level = None
balance_EUR = 10000
balance_USD = 0
trade_values = None
count = 0
buy_sell = None


for i in range(len(my_data)-420):
    window = my_data[i:420+i]
    fibonacci = Fib(window)

    if count == 5:
        #print(trade_values.limit, window[-1][4], "efssssss")
        trade_values.limit = 0
        level = L(fibonacci, window[-1])
        count = 0

    if trade_values is not None and trade_values.limit == 0 and buy_sell is not None and buy_sell.stop_loss[0] != 0:
        balance_EUR, balance_USD, activated = buy_sell.activate_stop_loss(window[-1][4])
        #print("gets herrrreeeeee", activated)
        if activated:
            print("Balance at iteration --> ", i, " Euro -> ", balance_EUR, " USD -> ", balance_USD)
            #print(balance_EUR, balance_USD)

            buy_sell.stop_loss = [0] * 2

    if trade_values and trade_values.limit != 0:
        #print(trade_values.limit, window[-1][4], "bhjf sfjf")
        buy_sell = BAS(window[-1], trade_values.limit, balance_EUR, balance_USD)

        if balance_EUR == buy_sell.balance_EUR:
            count = count + 1
            trend_array = []
        else:
            balance_EUR = buy_sell.balance_EUR
            balance_USD = buy_sell.balance_USD

            print("Balance at iteration --> ", i, " Euro -> ", balance_EUR, " USD -> ", balance_USD)

            count = 0
            trade_values.limit = 0
            level = L(fibonacci, window[-1])
            #print(level.L1, level.L2)
            trend_array = []

    if i > 0:
        trend = TR(fibonacci, level.L1, level.L2)
        level.lower = trend.update_lower
        level.upper = trend.update_upper
        check, bound = trend.check_thresh(window[-1])
        #print(balance_USD)
        if check == 2:
            trend_array = []
        else:
            trend_array.append(check)

    if i is 0:
        level = L(fibonacci, window[-1])

    #print(trend_array)
    if len(trend_array) >= 5:
        if sum(trend_array[:5]) >= 2:
            #print(bound, balance_EUR, balance_USD)
            #print(window[-1][4])
            trade_values = T(window[-1], balance_EUR, balance_USD, bound)
            #print(trade_values.limit)
            trend_array = []
        elif sum(trend_array[:5]) < 2:
            level = L(fibonacci, window[-1])
            trend_array = []
            #print(level.L1, level.L2)
            #print(window[-1][4])

print(i)
