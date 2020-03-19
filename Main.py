from DataFile import *
from Forecasting import show_forecast, show_forecast_with_lockdown

days_to_forecast = 50
lockdown_date = date(2020, 3, 16)

show_forecast(days_to_forecast, Country.SPAIN)
# show_forecast_with_lockdown(days_to_forecast, lockdown_date, Country.SPAIN)
