import pandas as pd


class DataProcessor(object):
    """
    """
    def __init__(self, data):
        self.data = data

    def deduplicate(self, field_name: str):
        data_dedup = self.data.drop_duplicates(subset=field_name)
        return data_dedup


