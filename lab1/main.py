import build_disc

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

#print(sys.path[0])

#data1 = pd.read_csv("df1_test.csv")
#data2 = pd.read_csv("df2_test.csv")

data1 = pd.read_csv("df1.csv")
data2 = pd.read_csv("df2.csv")

#print(build_disc(data1, data2))


#build_disc.plot_cirles(data1,data2)

ax = build_disc.circle_surface(data1,data2)



check_data = pd.read_csv("check.csv", sep = ';', decimal = ',')

ax.scatter(check_data.iloc[0]['x'], check_data.iloc[0]['y'], check_data.iloc[0]['z'], s = 500 , color = 'blue')
ax.scatter(check_data.iloc[1]['x'], check_data.iloc[1]['y'], check_data.iloc[1]['z'], s = 500 , color = 'orange', marker = '>')

plt.show()

#test = pd.read_csv("hello.csv", decimal = ",", sep = ";")
#print(test)