import pandas as pd
import glob
import re
from functools import reduce
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import  Counter
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS, WordCloud

nltk.download()

all_files = glob.glob('./textAnalysis/baseResources/myCabinetExcelData*.xls')
print(all_files)

all_files_data = []
for file in all_files:
    data_frame = pd.read_excel(file)
    all_files_data.append(data_frame)
all_files_data[0]

all_files_data_concat = pd.concat(all_files_data, axis=0, lgnore_index=True)
print(all_files_data_concat)

