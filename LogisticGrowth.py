from scipy.optimize import curve_fit
import numpy as np


def total_cases_from_params(L, k, x0, num_days_including_forecast):
    total_cases = [logistic_funct(x, L, k, x0) for x in range(num_days_including_forecast)]
    return total_cases


def calculate_logistic_function_params(values):
    days = np.array(np.arange(len(values)), dtype=float)
    fit_params, cov = curve_fit(logistic_funct, days, values, p0=[1000000, .20, 40], maxfev=2000)
    return fit_params


def calculate_params_constrained(values, x0):
    days = np.array(np.arange(len(values)), dtype=float)
    fit_params, cov = curve_fit(logistic_funct_constrained(x0), days, values, p0=[100000, .10], maxfev=2000)
    return fit_params


def logistic_funct(x, maximum, growth, midpoint):
    return maximum / (1 + np.exp(-growth * (x - midpoint)))


def logistic_funct_constrained(midpoint):
    def logistic_func(x, maximum, growth):
        return maximum / (1 + np.exp(-growth * (x - midpoint)))
    return logistic_func



