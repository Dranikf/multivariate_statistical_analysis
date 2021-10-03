import pandas as pd
import numpy as np
from math import sqrt

import sys
sys.path[0] = sys.path[0][:-5]


from lab2.main_comp import main_componets

df1 = pd.read_csv("lab2/data.csv", sep = ";", decimal = ",")
data = pd.concat([df1["x1"], df1["x2"], df1["x3"], df1["x4"]], axis = 1).to_numpy()


print("covariation matrix before")
print(np.corrcoef(data, rowvar = False))

F = main_componets(data)

print("covariation matrix after")
print(np.corrcoef(F, rowvar = False))