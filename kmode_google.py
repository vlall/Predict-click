import numpy as np
import pandas as pd
from kmodes import kmodes
import ipaddress
from urllib.parse import urlparse
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np
from scipy import spatial
import gensim
from nltk.cluster import KMeansClusterer
import nltk


def avg_feature_vector(words, num_features=300):
	model = gensim.models.Word2Vec.load_word2vec_format('./model/GoogleNews-vectors-negative300.bin', binary=True)
	index2word_set = set(model.wv.index2word)
	feature_vec = np.zeros((num_features, ), dtype='float32')
	n_words = 0
	for word in words:
		if word in index2word_set:
			n_words += 1
			feature_vec = np.add(feature_vec, model[word])
	if (n_words > 0):
		feature_vec = np.divide(feature_vec, n_words)
	return feature_vec


def is_valid_ip(ip):
	try:
		ipaddress.ip_address(ip)
		return True
	except ValueError:
		return False


df = pd.read_json("test-edmi.json")
df = df[["USERNAME", 'SOURCE_APP', 'URI']]
df = df.loc[df['SOURCE_APP'] == "BAT"]
# Filter the IP Addresses. Only 1,029,890 rows have usernames
mask = df['USERNAME'].apply(lambda x: is_valid_ip(x))
df = df[['USERNAME','URI']][~mask]
df['URI'] = df['URI'].apply(lambda x: urlparse(x)[2].split('/')[1:])
print(df.groupby(['USERNAME']).count())
print("Finished preprossessing... %d rows ready." % (len(df)))
print(df)

df_dummy = pd.get_dummies(df)
print(len(df_dummy))

#transform into numpy array
x = df_dummy.reset_index().values
clusters_incorrect = True

km = kmodes.KModes(n_clusters=3, init="Huang", n_init=3, verbose=1)
clusters = km.fit_predict(x)
df_dummy['clusters'] = clusters
print(df_dummy)
pca = PCA(2)

# Turn the dummified df into two columns with PCA
plot_columns = pca.fit_transform(df_dummy)
print(len(plot_columns))
df_dummy.to_pickle("df_dummy.pkl")
np.save("pca-transform.pkl", plot_columns)

# Plot based on the two dimensions, and shade by cluster label
plt.scatter(x=plot_columns[:,1], y=plot_columns[:,0], c=df_dummy["clusters"], s=10)
#plt.show()
print("Done.")

#df.groupby('clusters').size()
#df2 = df.loc[df['clusters'] == 1]]
#df2.any(0)
#df.any

