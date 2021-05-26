import numpy as np
import pandas as pd
from compute_functionals import functional5_8

data1 = pd.DataFrame(np.array([[1,2],[3,4]]))
data2 = pd.DataFrame(np.array([[3,4], [1, 2]]))

print(data1)
print(data2)


print(functional5_8([data1, data2]))