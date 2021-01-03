from datetime import date, datetime

import dateutil

from Country import Country
from DataLoader import get_cases_world, get_cases_for, start_date
from Forecasting import show_forecast, show_forecast_with_lockdown
from LogisticGrowth import calculate_logistic_function_params

days_to_forecast = 50
lockdown_date = date(2020, 3, 19)
country = Country.NETHERLANDS


corona_world_data = get_cases_world()
corona_cases_country = get_cases_for(country, corona_world_data)


show_forecast(country, start_date, days_to_forecast, corona_cases_country)
# show_forecast_with_lockdown(country, start_date, days_to_forecast, corona_cases_country, lockdown_date)
