from object_geocoder import data_processor
from object_geocoder.csv_reader import CSVreader
from object_geocoder.data_processor import DataProcessor
from object_geocoder.geocoder import ForwardGeocoder

cr = CSVreader()
a = cr.read_csv(r"D:\Repositories\ObjectGeocoder\resourses\test_data.csv")

dp = DataProcessor(a)
data = dp.deduplicate("shop_name")
fg = ForwardGeocoder("af1ReeiC0Gu_R2q00q0S8czaWAhqGiNHuhX4SME45lE")

for i, v in data.iterrows():
    fg.geocode(v["address_line"])