
Import numpy as np 
	data=np.loadtxt (
		fname='data/inflammation.csv, delimiter ',')
	done


import matplotlib as plt
fig = matplotlib.pyplot.figure(figsize=(3.0, 8.0)

ave_inflammation = np.mean (data, axis=0)
plt.plot(ave_inflammation)
