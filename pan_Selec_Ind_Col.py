import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'A':[1,4,7], 'B':[2,5,8], 'C':[3,6,9]})


print df

print '\n', df.iloc[0][0]

print '\n', df.loc[0]['A']

print '\n', df.iat[0,0]

print '\n', df.get_value(0, 'A')

x1 = df.iloc[0]
print type(x1)

print '\n', x1

x2 = df.loc[:,'A']
print type(x2)

print '\n', x2

x3 = x2.values
print '\n', type(x3)

print '\n', x3
plt.figure()
plt.boxplot(x3)
plt.show()







