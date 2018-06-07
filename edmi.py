import pandas as pd  #imports the pandas library and aliasing as pd
import re
import numpy as np
import json
import csv  #converting new_list to csv file

df = pd.read_json('test_edmi.json')
df = df[:10000]  #only the first 10k rows
df.to_csv('test_edmi_10k.csv')

# from the first 10k rows, only get these three columns
condensed_10k = df.loc[:, ['USERNAME', 'SOURCE_APP', 'SOURCE_APP_FUNCTION']]
condensed_10k.to_csv('condensed_10k.csv', index=False)

# filter out NaN items from column 'SOURCE_APP_FUNCTION' and call it app_func
df = df[pd.notnull(df['SOURCE_APP_FUNCTION'])]

# get items with non-alphanumeric pattern, r for raw string and the + for repeat
pattern = re.compile(r'\W+')

for item in df['SOURCE_APP_FUNCTION']:
    item_new = re.sub(pattern, ' ', item)
    print(item_new)

