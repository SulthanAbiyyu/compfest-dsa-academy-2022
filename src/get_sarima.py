import statsmodels.api as sm

def get_sarima(data, p, d, q, s):
    return sm.tsa.SARIMAX(data, order=(p, d, q), seasonal_order=(p, d, q, s))