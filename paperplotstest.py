
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

systemsize = 33**2
#systemsize = 1
systemsizegr = 12**2

statescl = np.loadtxt('./avgstatecl/states.csv',delimiter=',')
#statescl = np.loadtxt('./states0.csv',delimiter=',')
statesgr = np.loadtxt('./avgstategrid/states.csv',delimiter=',')

statescl1 = statescl[:,0]
statescl2 = statescl[:,1]
statescl3 = statescl[:,2]
statesgr1 = statesgr[:,0]
statesgr2 = statesgr[:,1]
statesclx = np.array(list(range(len(statescl1)))) / systemsize
statesgrx = np.array(list(range(len(statesgr1)))) / systemsizegr

fig, ax =  plt.subplots()
ax.set(xlabel='time [timestep / systems size]', ylabel='cooperativity')
ax.plot(statesclx,statescl1, color='#ff7f0e', label="AVG cooperativity")
ax.plot(statesclx,statescl2, color='#ff7f0e', alpha=0.5, label="SD cooperativity")
#ax.plot(statesclx,statescl3, color='#ff7f0e', linestyle=":", label="SD cluster cooperativity")
ax.legend(loc = 'lower right')
ax.xaxis.grid(True, linestyle='dotted')
ax.yaxis.grid(True, linestyle='dotted')
ax.set_ylim([-1,1])

fig.savefig('example.png')

fig, ax =  plt.subplots()
ax.set(xlabel='time [timestep / system size]', ylabel='cooperativity')
ax.plot(statesgrx,statesgr1, color='#ff7f0e', label="AVG cooperativity")
ax.plot(statesgrx,statesgr2, color='#ff7f0e', alpha=0.5, label="SD cooperativity")
ax.legend(loc = 'lower right')
ax.xaxis.grid(True, linestyle='dotted')
ax.yaxis.grid(True, linestyle='dotted')
ax.set_ylim([-1,1])

lines = np.array([0,100,250,500,750,1000,2000,4000]) / systemsizegr

for line in lines : 
    ax.axvline(x = line, color = 'gray', linestyle = 'dotted')

fig.savefig('examplegr.png')
