import numpy as np 
import matplotlib.pyplot as plt 

np.random.seed(10)
datos = np.random.normal(100, 10, 200)

plt.figure(1, figsize=(9, 6))

plt.boxplot(datos)
plt.ylim([50,150])

plt.show()

