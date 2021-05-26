import pandas as pd
import numpy as np

data1 = pd.read_csv("df1.csv")
data2 = pd.read_csv("df2.csv")

data1_s = len(data1.index)
data2_s = len(data2.index)

data1_np = data1.to_numpy()
data2_np = data2.to_numpy()

cov1 = np.cov(data1_np, bias = True, rowvar = False)
cov2 = np.cov(data2_np, bias = True, rowvar = False)

unioun_cov = (cov1*data1_s + cov2*data2_s) * (1/(data1_s + data2_s - 2))
inv_union_cov = np.linalg.inv(unioun_cov)

mean1 = np.mean(cov1, axis = 0)
mean2 = np.mean(cov2, axis = 0)

A = np.dot(inv_union_cov,(mean1 - mean2).transpose())

temp_list = []

for i in range(data1_np.shape[0]):
    temp_list.append(0)
    for j in range(data1_np.shape[1]):
        temp_list[i] += A[j]*data1_np[i][j]

mean1 = temp_list.mean()