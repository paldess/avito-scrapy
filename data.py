from pymongo import MongoClient
from pprint import pprint
import pandas as pd
import xlsxwriter
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

pd.options.display.max_columns = 6

db = MongoClient('localhost', 27017)
data_m = db.avito['мужские часы']


data = pd.DataFrame(data_m.find({}))
data['views'] = data['views'][data['views']>=0].astype(np.int64)
data['last'] = data['last'].astype(np.int64)


print()

views_in_day = data['views'][data['views']>=0]/data['last'][data['last']>0]
data['views_in_day'] = views_in_day
data['price'][data['price']== ' Бесплатно  '] = -2
data['price'][data['price']== ' Цена не указана  '] = -1



plt.bar(data['last'], data['views_in_day'])
sns.barplot(data['price'], data['views_in_day'])




data.to_excel('мужские часы авито 1_09_21.xlsx')