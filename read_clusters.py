import pandas as pd
import matplotlib.pyplot as plt
import json
def get_usernames(x):
    if "USERNAME_" in x:
        clean = x.lstrip("USERNAME_")
        return clean

df = pd.read_pickle("df_dummy.pkl")
print(len(df))
print(df.groupby('clusters').size())
clusters = len(df.groupby('clusters').size())

cluster_list = []
cluster_users = {}
"""
    0:"Cognizant Engineer",
    1:"Flight Software Systems Engineer",
    2:"Instrument Manager and Deputy",
    3:"Payload System Engineer",
    4:"Cognizant Delivery Lead",
    5:"Outlier_1",
    6:"Outlier_2",
    7:"Outlier_3",
"""
roleDict = {
    0:"Flight Software Systems Engineer",
    1:"Outlier_1",
    2:"Outlier_2",
    3:"Payload System Engineer",
    4:"Cognizant Engineer",
    5:"Instrument Manager and Deput",
    6:"Outlier_3",
    7:"Outlier_4",
}
for cluster in range(0, clusters):
    df2 = df.loc[df['clusters'] == cluster]
    x = df2.any(0)
    y = pd.DataFrame({'Index':x.index, 'Bool':x.values})
    usernames = y[y.Bool].Index
    usernames = usernames.apply(lambda x: get_usernames(x)).dropna()
    list_for_json = []
    for user in usernames:
        list_for_json.append({"name": user, "size": 10})
    cluster_list.append({"name": cluster, "children":list_for_json})
    print(list(usernames))
    print(cluster, len(usernames))
#print(json.dumps(cluster_list, indent=4))
with open('data.json', 'w') as outfile:
    json.dump(cluster_list, outfile)
# Plot based on the two dimensions, and shade by cluster label
#plt.scatter(x=plot_columns[:,1], y=plot_columns[:,0], c=df_dummy["clusters"], s=10)
#plt.show()
with open('clustered-users.json', 'w') as the_file:
    json.dump(cluster_users, the_file)