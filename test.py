
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

rawdata = np.loadtxt('paraclustering0.2xl.csv',delimiter=',')
#rawdata = np.loadtxt('.paraclustering0.2.csv',delimiter=',')

print(np.shape(rawdata))

fig, ax = plt.subplots()

p1, = ax.plot(rawdata[0])

fig.savefig('test.png')

