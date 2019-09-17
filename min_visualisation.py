import numpy as np

data = np.loadtxt(fname='data/inflammation-01.csv', delimiter=',')

ave_inflammation = np.min (data, axis=0)
plt.plot(ave_inflammation)
