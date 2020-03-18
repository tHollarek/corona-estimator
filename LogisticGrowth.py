from scipy.optimize import curve_fit
import numpy as np


def total_cases_from_params(L, k, x0, num_days_including_forecast):
    total_cases = [logistic_funct(x, L, k, x0) for x in range(num_days_including_forecast)]
    return total_cases


def calculate_logistic_function_params(values):
    days = np.array(np.arange(len(values)), dtype=float)
    fit_params, cov = curve_fit(logistic_funct, days, values)
    return fit_params


def calculate_params_constrained(values, x0):
    days = np.array(np.arange(len(values)), dtype=float)
    fit_params, cov = curve_fit(logistic_funct_constrained(x0), days, values)
    return fit_params


def logistic_funct(x, L, k, x0):
    return L / (1 + np.exp(-k * (x - x0)))


def logistic_funct_constrained(x0):
    def logistic_func(x, L, k):
        return L / (1 + np.exp(-k * (x - x0)))
    return logistic_func



