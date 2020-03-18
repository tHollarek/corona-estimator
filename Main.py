from DataFile import *
from Forecasting import calculate_forecast, calculate_forecast_with_lockdown

days_to_forecast = 50
lockdown_date = date(2020, 3, 22)

# calculate_forecast(days_to_forecast, southkorea)
# calculate_forecast(days_to_forecast, germany)
# calculate_forecast(days_to_forecast, italy)
# calculate_forecast(days_to_forecast, Country.USA)
calculate_forecast_with_lockdown(days_to_forecast, lockdown_date, Country.GERMANY)
