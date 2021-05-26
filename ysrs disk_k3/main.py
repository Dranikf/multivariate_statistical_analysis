import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


inp = pd.read_csv("input_data.csv", sep = ";")

one = inp.iloc[:,[0, 1]]
one = one.to_numpy()

two = inp.iloc[:,[2, 3]]
two = two.to_numpy()

three = inp.iloc[:,[4, 5]]
three = three.to_numpy()

M_points = np.array([[14, 6], [1, 1], [1, 14]])

plt.figure()

plt.scatter(one[:,0], one[:,1])
plt.scatter(two[:,0], two[:,1], color = "red")
plt.scatter(three[:,0], three[:,1], color = "green")
plt.scatter(M_points[:,0], M_points[:,1], color = 'orange', s = 200)

plt.show()

cov_1 = np.cov(one, bias = True, rowvar = False)
print(cov_1)