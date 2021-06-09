import pandas as pd


class CSVreader(object):
    """
    """
    def __init__(self):
        pass

    def read_csv(self, path: str):
        data = pd.read_csv(path)
        return data