import numpy as np
data_type = [('name', 'S15'),('class', int),('height', float)]
studs = [('Akshita', 12, 160.02),('Prashant', 12, 165),('Rudraksh',100,125)]
studs2 = np.array(studs, dtype= data_type)
print(np.sort(studs2, order='height'))