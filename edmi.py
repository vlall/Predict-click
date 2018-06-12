#!/usr/bin/env python
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import pandas as pd  #imports the pandas library and aliasing as pd
import re

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import numpy as np
import json
import csv  #converting new_list to csv file

df = pd.read_json('test_edmi.json')
df = df[:10000]  #only the first 10k rows
df.to_csv('test_edmi_10k.csv')

# from the first 10k rows, only get these three columns
condensed_10k = df.loc[:, ['USERNAME', 'SOURCE_APP', 'SOURCE_APP_FUNCTION']]
condensed_10k.to_csv('condensed_10k.csv', index=False)

# filter out NaN items from column 'SOURCE_APP_FUNCTION'
df = df[pd.notnull(df['SOURCE_APP_FUNCTION'])]

# get items with non-alphanumeric pattern, r for raw string and the + for repeat
pattern = re.compile(r'\W+')

stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(df['SOURCE_APP_FUNCTIONS'])
item_filtered = [item for item in word_tokens if item not in stop_words]
for item in df['SOURCE_APP_FUNCTION']:

    # sub non-alphanumeric pattern with a space
    item_new = re.sub(pattern, ' ', item)

    if item_new not in stop_words:
        item_filtered.append(item_new)
        print(item_new)

# still working on this...


