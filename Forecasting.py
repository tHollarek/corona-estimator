import matplotlib.pyplot as plt

from DateUtils import get_date_list
from LogisticGrowth import calculate_logistic_function_params, \
    total_cases_from_params, calculate_params_constrained


def show_forecast(days_to_forecast, input_params):
    name = input_params[0]
    start_date = input_params[1]
    cases = input_params[2]
    days_with_cases = get_date_list(start_date, len(cases))
    num_days_with_model_values = len(cases) + days_to_forecast
    days_with_model_values = get_date_list(start_date, num_days_with_model_values)

    logistic_function_params = calculate_logistic_function_params(cases)

    model_values = total_cases_from_params(
        logistic_function_params[0],
        logistic_function_params[1],
        logistic_function_params[2],
        num_days_with_model_values)

    plot(name, cases, days_with_cases, days_with_model_values, model_values)

    print("successfully created forecast")


def show_forecast_with_lockdown(days_to_forecast, lockdown_date, input_params):
    name = input_params[0]
    start_date = input_params[1]
    cases = input_params[2]

    days_until_turning_point = (lockdown_date - start_date).days + 7
    num_days_with_model_values = len(cases) + days_to_forecast

    day_list_cases = get_date_list(start_date, len(cases))
    day_list_including_forecast = get_date_list(start_date, num_days_with_model_values)

    params_constrained = calculate_params_constrained(cases, days_until_turning_point)
    model_values = total_cases_from_params(
        params_constrained[0],
        params_constrained[1],
        days_until_turning_point,
        num_days_with_model_values)

    plot(name, cases, day_list_cases, day_list_including_forecast, model_values)
    print("successfully created forecast")


def plot(name, cases, days_with_cases, days_with_model_values, model_values):
    plt.scatter(days_with_cases, cases)
    plt.plot(days_with_model_values, model_values, label=name)
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()
