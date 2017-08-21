import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'A':[1,4,4,2,5,6], 'B':[1,1,1,2,5,8], 'C':[1,1,1,3,6,9]})


x2 = df.loc[:,'A']

x3 = x2.values
print '\n', type(x3)

print '\n', x3
plt.figure()
plt.boxplot(x3)
plt.show()







