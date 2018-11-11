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


for i in range(len(my_data)-240):
    window = my_data[i:240+i]
    fibonacci = Fib(window)
    if count == 5:
        trade_values.limit = 0
        trade_values.stop_loss = 0

    if trade_values is not None and trade_values.stop_loss != 0 and trade_values.limit == 0 and buy_sell is not None:
        balance_EUR, balance_EUR, activated = buy_sell.activate_stop_loss(window[-1][4])
        if activated:
            trade_values.stop_loss = 0

    if trade_values and trade_values.limit != 0:
        buy_sell = BAS(window[-1], trade_values.limit, trade_values.stop_loss, balance_EUR, balance_USD)

        if balance_EUR == buy_sell.balance_EUR:
            count = count + 1
        else:
            balance_EUR = buy_sell.balance_EUR
            balance_USD = buy_sell.balance_USD
            print("Balance at iteration --> ", i, " Euro -> ", balance_EUR, " USD -> ", balance_USD)

            count = 0
            trade_values.limit = 0
            level = L(fibonacci, window[-1], )
            trend_array = []

    if i > 0:
        trend = TR(fibonacci, level.L1, level.L2)
        level.lower = trend.update_lower
        level.upper = trend.update_upper
        check, bound = trend.check_thresh(window[-1])
        if check == 2:
            trend_array = []
        else:
            trend_array.append(check)

    if i is 0:
        level = L(fibonacci, window[-1])

    if len(trend_array) >= 3:
        if sum(trend_array[:3]) > 1:
            trade_values = T(window[-1], balance_EUR, balance_USD, bound)
            trend_array = []
        else:
            level = L(fibonacci, window[-1], )
            trend_array = []
