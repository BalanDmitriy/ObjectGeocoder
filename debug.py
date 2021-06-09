from object_geocoder import data_processor
from object_geocoder.csv_reader import CSVreader
from object_geocoder.data_processor import DataProcessor


cr = CSVreader()
a = cr.read_csv(r"D:\Repositories\ObjectGeocoder\resourses\test_data.csv")

dp = DataProcessor(a)
dp.deduplicate()
# print(type(dp.data))