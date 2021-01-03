from datetime import date

import pandas as pd


covid_data_gho_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
start_date = date(22, 1, 20)


def get_cases_world():
    corona_cases = pd.read_csv(covid_data_gho_url, error_bad_lines=False)
    return corona_cases


def get_cases_for(country, corona_cases):
    country_data = corona_cases[corona_cases['Country/Region'] == country]
    country_cases_df = country_data.drop(columns=["Province/State", "Country/Region", "Lat", "Long"])
    country_cases_list = country_cases_df.to_numpy().tolist()[0]
    return country_cases_list
