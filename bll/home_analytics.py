from db.home_analytics import *
import pandas as pd


def get_mortality_stats():
    data = mortality_data()
    data_dict = {"data": []}
    for row in data:
        data_dict["data"].append(dict(zip(row.keys(), row.values())))
    return data_dict
