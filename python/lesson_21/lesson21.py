import numpy as np
import matplotlib.pyplot as plt

name = np.array(["Akshita","Rudraksh","Prashant","Avni","Kaavya","Ritika","Navya"])
marks = np.array([100,10,50,70,80,55,45])

x = []
for i in marks:
    result = (i//100)*100
    x.append(result)

print(x)

plt.plot(name,marks)

plt.show()

plt.bar(name,marks)

plt.show()


