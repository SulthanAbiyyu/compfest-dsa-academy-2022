import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

def adfuller_test(df):
    result = adfuller(df)
    print("ADF Statistic: %f" % result[0])
    print("p-value: %f" % result[1])
    if result[1] < 0.05:
        print("stationary")
    else:
        print("not stationary")

def sarima_acf_pacf(data):
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    plot_acf(data, ax=ax1)
    plot_pacf(data, ax=ax2)
    fig.set_size_inches(12, 9)
