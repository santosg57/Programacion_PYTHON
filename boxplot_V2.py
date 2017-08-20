## numpy is used for creating fake data
import numpy as np 
import matplotlib.pyplot as plt 

## Create data
np.random.seed(10)
data_to_plot = np.random.normal(100, 10, 200)

# Create a figure instance
fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(data_to_plot)
ax.set_ylim([0,200])

fig.show()

