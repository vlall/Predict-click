import numpy as np
import pandas as pd
from kmodes import kmodes
import ipaddress
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


def is_valid_ip(ip):
	try:
		ipaddress.ip_address(ip)
		return True
	except ValueError:
		return False

df = pd.read_json("test-edmi.json")
df = df[["USERNAME", 'SOURCE_APP']]
# filter by IP Address
mask = df['USERNAME'].apply(lambda x: is_valid_ip(x))
df = df[['USERNAME','SOURCE_APP']][~mask]

df_dummy = pd.get_dummies(df)

#transform into numpy array
x = df_dummy.reset_index().values

km = kmodes.KModes(n_clusters=7, init='random', n_init=5, verbose=1)
clusters = km.fit_predict(x)
df_dummy['clusters'] = clusters

pca = PCA(2)

# Turn the dummified df into two columns with PCA
plot_columns = pca.fit_transform(df_dummy.ix[:,0:12])

# Plot based on the two dimensions, and shade by cluster label
plt.scatter(x=plot_columns[:,1], y=plot_columns[:,0], c=df_dummy["clusters"], s=30)
plt.show()
