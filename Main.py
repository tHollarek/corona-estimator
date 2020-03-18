
import matplotlib.pyplot as plt

from DataFile import *
from DateUtils import get_date_list
from LogisticGrowth import calculate_logistic_function_params, \
    total_cases_from_params, calculate_logistic_function_params_constrained

days_to_forecast = 50
start_date = germany_start_date
lockdown_date = date(2020, 3, 19)
cases = germany_cases

days_with_cases = get_date_list(start_date, len(cases))
days_until_lockdown = (lockdown_date - start_date).days
days_until_turning_point = days_until_lockdown + 7
num_days_with_model_values = len(cases) + days_to_forecast
days_with_model_values = get_date_list(start_date, num_days_with_model_values)

logistic_function_params = calculate_logistic_function_params(cases)
logistic_function_params_constrained = calculate_logistic_function_params_constrained(cases, days_until_turning_point)

# model_values = total_cases_from_params(
#     logistic_function_params[0],
#     logistic_function_params[1],
#     logistic_function_params[2],
#     num_days_with_model_values)
model_values_lockdown_fast = total_cases_from_params(
    logistic_function_params_constrained[0],
    logistic_function_params_constrained[1],
    days_until_turning_point,
    num_days_with_model_values)

plt.scatter(days_with_cases, cases)
# plt.plot(days_with_model_values, model_values, label="simple model")
plt.plot(days_with_model_values, model_values_lockdown_fast, label="Lockdown on 19.03")
# plt.plot(germany_forecast_days, germany_model_values_lockdown_medium, label="Germany - Lockdown on 26.04")
# plt.plot(germany_forecast_days, germany_model_values_lockdown_slow, label="Germany - Lockdown on 02.04")
plt.legend()
plt.show()

print("successfully created forecast")
