import pandas as pd


class DataProcessor(object):
    """
    """
    def __init__(self, data):
        self.data = data

    def deduplicate(self):
        data_dedup = self.data.drop_duplicates(subset="shop_name")
        return print(data_dedup)


