
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import glob
from scipy import stats
from scipy.interpolate import griddata
import matplotlib.ticker as ticker

states = np.loadtxt('./statestypecl.csv',delimiter=',')
states1 = np.loadtxt('./statesnewPoliticalClimate0.025.csv',delimiter=',')
states2 = np.loadtxt('./statesnewPoliticalClimate0.075.csv',delimiter=',')
states3 = np.loadtxt('./statesnewPoliticalClimate0.1.csv',delimiter=',')
states4 = np.loadtxt('./states0.csv',delimiter=',')
#statesdeg1 = np.loadtxt('./states.csv',delimiter=',')
#statesdeg2 = np.loadtxt('./statesdeg12.csv',delimiter=',')
#statesdeg3 = np.loadtxt('./statesdeg50.csv',delimiter=',')
#statesinf3 = np.loadtxt('./statesinf1.csv',delimiter=',')
#statesinf1 = np.loadtxt('./statesgridphi01.csv',delimiter=',')
#statesinfgr1 = np.loadtxt('./statesinfgr1.csv',delimiter=',')

#statesavgcl2 = statescl2.mean(0)
#statesdeg1 = statesdeg1[:,0]
#statesdeg2 = statesdeg2[:,0]
#statesdeg3 = statesdeg3[:,0]
#statesinf1 = statesinf1[:,0]
#statesinf3 = statesinf3[:,0]
#statesinfgr1 = statesinfgr1[:,0]
states = states[:,0]
states1 = states1[:,0]
states2 = states2[:,0]
states3 = states3[:,0]
states4 = states4[:,0]

print (np.argmin(states1))

figstates, ax =  plt.subplots()
ax.plot(states,'g',label="k = 4")
ax.plot(states1,'r',label="k = 4")
ax.plot(states2,'r',label="k = 4")
ax.plot(states3,'r',label="k = 4")
ax.plot(states4,'b',label="k = 4")
#f7 = ax.plot(statesavgcl2,'r',label="k = 4")
#f8 = ax.plot(statesdeg1,'g',label="k = 12")
#f9 = ax.plot(statesdeg3,'g',label="k = 50")
#f9 = ax.plot(statesinf3,'b',label="inf = 3")
#f9 = ax.plot(statesinf1,'r',label="inf = 1")
#f9 = ax.plot(statesinfgr1,'r',label="infgr = 1")
ax.set(xlabel='timestep',ylabel='$\\langle$ state $\\rangle$')
ax.legend(loc = 'lower right')
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.25))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))
ax.xaxis.set_major_locator(ticker.MultipleLocator(10000))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(2500))
ax.xaxis.grid(True, linestyle='dotted')
ax.yaxis.grid(True, linestyle='dotted')
ax.set_ylim([-1,1])

figstates.savefig('convlin.png')

