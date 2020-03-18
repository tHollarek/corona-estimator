import datetime
import numpy as np


def get_date_list(start_date, num_days):
    base = start_date
    return [base + datetime.timedelta(days=x) for x in range(num_days)]


def get_int_list(num):
    return np.arange(num).reshape(-1, 1)
