import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("mmsa ysrs1 /input_data.csv", sep = ';', decimal = ',')

fig = plt.figure(figsize = [10,20])
ax = fig.add_subplot(111, projection='3d')

np_cluster1 = df.iloc[[0,3,8]].to_numpy()
np_cluster2 = df.iloc[[4,10,11]].to_numpy()
np_cluster3 = df.iloc[[5,6,7]].to_numpy()
np_cluster4 = df.iloc[[1,2,9]].to_numpy()

ax.scatter(np_cluster1[:,0],np_cluster1[:,1],np_cluster1[:,2], s = 100, marker = "o", alpha = 1)
ax.scatter(np_cluster2[:,0],np_cluster2[:,1],np_cluster2[:,2], s = 100, marker = ">", alpha = 1)
ax.scatter(np_cluster3[:,0],np_cluster3[:,1],np_cluster3[:,2], s = 100, marker = "s", alpha = 1)
ax.scatter(np_cluster4[:,0],np_cluster4[:,1],np_cluster4[:,2], s = 100, marker = "*", alpha = 1)

plt.show()