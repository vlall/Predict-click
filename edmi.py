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
from urllib.parse import urlparse

df = pd.read_json('test_edmi.json')
df = df[:10000]  #only the first 10k rows
df.to_csv('test_edmi_10k.csv')

# from the first 10k rows, only get these four columns
condensed_10k = df[['USERNAME', 'SOURCE_APP', 'URI',
                   'SOURCE_APP_FUNCTION']]
condensed_10k.to_csv('condensed_10k.csv', index=False)

# Parse a URL into six components, returning a 6-tuple, keep only the path
df2 = df['URI'].apply(lambda x: urlparse(x)[2].split('/')[1:])

df2.to_csv('uri.csv', index=False)
