
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import glob
from scipy import stats
from scipy.interpolate import griddata
import matplotlib.ticker as ticker

systemsize = 33**2

### Standard plot

statesraw = np.array([])
statesfiles = sorted(glob.glob('./states*'))
it = 0
for f in statesfiles : 
    if (it == 0) :
        statesraw = np.loadtxt(open(f,"rb"),delimiter=',',skiprows=0)
    else :
        statesraw = np.append(statesraw,np.loadtxt(f,delimiter=','),axis=1)
    it = it + 1

#statesraw = np.loadtxt('./archive/tragic/states0.csv',delimiter=',')

statesavg = statesraw[:,0::3]
statesstd = statesraw[:,1::3]
clustrstd = statesraw[:,2::3]
xaxisvals = np.array(list(range(len(statesavg)))) / systemsize

print (np.shape(xaxisvals))

statesavg = statesavg.mean(axis=1)
statesstd = statesstd.mean(axis=1)  
clustrstd = clustrstd.mean(axis=1)

#size = 150000
#statesavg = statesavg[0:size]
#statesstd = statesstd[0:size]
#clustrstd = clustrstd[0:size]
#xaxisvals = xaxisvals[0:size]

## comment out for non tipping
#statesraw = np.loadtxt(open('./archive/standard/states0.csv',"rb"),delimiter=',',skiprows=0)

#statesavg = statesraw[:,0]
#statesstd = statesraw[:,1]
#clustrstd = statesraw[:,2]

print(np.shape(statesavg))

figstates, ax =  plt.subplots()
ax.plot(xaxisvals, statesavg, color='#ff7f0e', label="AVG cooperativity")
ax.plot(xaxisvals, statesstd, color='#ff7f0e', alpha=0.5, label="SD cooperativity")
#ax.plot(xaxisvals, clustrstd, color='#ff7f0e', linestyle=":", label="SD cluster cooperativity")
#ax.axhline(y=0.0, color='r', linestyle='-')
ax.set(xlabel='time [timestep / system size]',ylabel='cooperativity')
ax.legend(loc = 'lower right')
ax.xaxis.grid(True, linestyle='dotted')
ax.yaxis.grid(True, linestyle='dotted')
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.25))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))
ax.xaxis.set_major_locator(ticker.MultipleLocator(50))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.set_ylim([-1,1])
#plt.xscale('log')
#plt.yscale('log')
#
figstates.savefig('tipping.png')

