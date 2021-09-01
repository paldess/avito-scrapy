from pymongo import MongoClient
from pprint import pprint
import pandas as pd

pd.options.display.max_columns = 6

db = MongoClient('localhost', 27017)
data_m = db.avito['мужские часы']


data = pd.DataFrame(data_m.find({}))




pprint(data)