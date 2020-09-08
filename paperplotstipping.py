
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import glob
from scipy import stats
from scipy.interpolate import griddata
import matplotlib.ticker as ticker


### Standard plot

statesraw = np.loadtxt(open('./states0.csv',"rb"),delimiter=',',skiprows=1)

statesavg = statesraw[:,0]
statesstd = statesraw[:,1]
clustrstd = statesraw[:,2]

figstates, ax =  plt.subplots()
f1 = ax.plot(statesavg, color='#ff7f0e', label="AVG state")
f2 = ax.plot(statesstd, color='#ff7f0e', alpha=0.5, label="SD states")
f3 = ax.plot(clustrstd, color='#ff7f0e', linestyle=":", label="SD clusters")
#ax.axhline(y=0.0, color='r', linestyle='-')
ax.set(xlabel='timestep',ylabel='1 - $\\langle$ state $\\rangle$')
ax.legend(loc = 'lower right')
ax.xaxis.grid(True, linestyle='dotted')
ax.yaxis.grid(True, linestyle='dotted')
#ax.set_ylim([-1,1])
#plt.xscale('log')
#plt.yscale('log')
#
figstates.savefig('states.png')

