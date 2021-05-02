

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import glob
from scipy import stats
from scipy.interpolate import griddata
import matplotlib.ticker as ticker
import matplotlib.pylab as pylab

params = {'legend.fontsize': 'x-large',
          'axes.labelsize': 'x-large',
          'axes.titlesize':'x-large',
          'xtick.labelsize':'x-large',
          'ytick.labelsize':'x-large',
          'figure.autolayout':True}
pylab.rcParams.update(params)

systemsize = 33**2

# from separated data

rawdata = np.array([])
files = sorted(glob.glob('./para*'))
it = 0

rawdata = []
for f in files : 
    rawdata.append(np.loadtxt(f,delimiter=',',usecols=(0,)))

rawdata = np.array(rawdata)
dataclust = rawdata[0:5,:]
datainit = rawdata[5:10,:]
datainitmu = rawdata[10:15,:]
dataphi = rawdata[15:20,:]
datar = rawdata[20:25,:]
datawi = rawdata[25:30,:]
datawij = rawdata[30:35,:]
datawmu = rawdata[35:40,:]

xaxis50k = np.array(list(range(len(dataclust[0])))) / systemsize

figclust, ax = plt.subplots()

p1, = ax.plot(xaxis50k,dataclust[0], label = '0.2')
p2, = ax.plot(xaxis50k,dataclust[1], label = '0.35')
p3, = ax.plot(xaxis50k,dataclust[2], label = '0.5')
p4, = ax.plot(xaxis50k,dataclust[3], label = '0.65')
p5, = ax.plot(xaxis50k,dataclust[4], label = '0.8')
ax.set(xlabel='time [timestep / systemsize]',ylabel='cooperativity')
#ax.set(xlabel='time [timestep / systemsize]',ylabel='cooperativity', title='clustering')
ax.set_ylim(-1,1)
ax.legend(loc='upper left')


figinit, ax = plt.subplots()

p1, = ax.plot(xaxis50k,datainit[4], label = '0.0')
p2, = ax.plot(xaxis50k,datainit[0], label = '-0.1')
p3, = ax.plot(xaxis50k,datainit[1], label = '-0.25')
p4, = ax.plot(xaxis50k,datainit[2], label = '-0.5')
p5, = ax.plot(xaxis50k,datainit[3], label = '-0.75')
ax.set(xlabel='time [timestep / systemsize]',ylabel='cooperativity')
#ax.set(xlabel='time [timestep / systemsize]',ylabel='cooperativity', title='initial state')
ax.set_ylim(-1,1)
ax.legend(loc='upper left')


figinitmu, ax = plt.subplots()

p1, = ax.plot(xaxis50k,datainitmu[0], label = '0.025')
p2, = ax.plot(xaxis50k,datainitmu[1], label = '0.075')
p3, = ax.plot(xaxis50k,datainitmu[2], label = '0.15')
p4, = ax.plot(xaxis50k,datainitmu[3], label = '0.25')
p5, = ax.plot(xaxis50k,datainitmu[4], label = '0.45')
ax.set(xlabel='time [timestep / systemsize]',ylabel='cooperativity')
#ax.set(xlabel='time [timestep / systemsize]',ylabel='cooperativity', title='std initial state')
ax.set_ylim(-1,1)
ax.legend(loc='upper left')


figphi, ax = plt.subplots()

p1, = ax.plot(xaxis50k,dataphi[0], label = '0.01')
p2, = ax.plot(xaxis50k,dataphi[1], label = '0.025')
p3, = ax.plot(xaxis50k,dataphi[2], label = '0.05')
p4, = ax.plot(xaxis50k,dataphi[3], label = '0.1')
p5, = ax.plot(xaxis50k,dataphi[4], label = '0.25')
ax.set(xlabel='time [timestep / systemsize]',ylabel='cooperativity')
#ax.set(xlabel='time [timestep / systemsize]',ylabel='cooperativity', title='external field')
ax.set_ylim(-1,1)
ax.legend(loc='upper left')


figr, ax = plt.subplots()

p1, = ax.plot(xaxis50k,datar[0], label = '0.025')
p2, = ax.plot(xaxis50k,datar[1], label = '0.05')
p3, = ax.plot(xaxis50k,datar[2], label = '0.1')
p4, = ax.plot(xaxis50k,datar[3], label = '0.2')
p5, = ax.plot(xaxis50k,datar[4], label = '0.4')
ax.set(xlabel='time [timestep / systemsize]',ylabel='cooperativity')
#ax.set(xlabel='time [timestep / systemsize]',ylabel='cooperativity', title='randomness')
ax.set_ylim(-1,1)
ax.legend(loc='upper left')


figwi, ax = plt.subplots()

p1, = ax.plot(xaxis50k,datawi[0], label = '0.2')
p2, = ax.plot(xaxis50k,datawi[1], label = '0.4')
p3, = ax.plot(xaxis50k,datawi[2], label = '0.6')
p4, = ax.plot(xaxis50k,datawi[3], label = '0.75')
p5, = ax.plot(xaxis50k,datawi[4], label = '0.9')
ax.set(xlabel='time [timestep / systemsize]',ylabel='cooperativity')
#ax.set(xlabel='time [timestep / systemsize]',ylabel='cooperativity', title='stubbornness')
ax.set_ylim(-1,1)
ax.legend(loc='upper left')


figwij, ax = plt.subplots()

p1, = ax.plot(xaxis50k,datawij[0], label = '0.2')
p2, = ax.plot(xaxis50k,datawij[1], label = '0.35')
p3, = ax.plot(xaxis50k,datawij[2], label = '0.5')
p4, = ax.plot(xaxis50k,datawij[3], label = '0.65')
p5, = ax.plot(xaxis50k,datawij[4], label = '0.8')
ax.set(xlabel='time [timestep / systemsize]',ylabel='cooperativity')
#ax.set(xlabel='time [timestep / systemsize]',ylabel='cooperativity', title='friendship')
ax.set_ylim(-1,1)
ax.legend(loc='upper left')


figwmu, ax = plt.subplots()

p1, = ax.plot(xaxis50k,datawmu[0], label = '0.025')
p2, = ax.plot(xaxis50k,datawmu[1], label = '0.075')
p3, = ax.plot(xaxis50k,datawmu[2], label = '0.15')
p4, = ax.plot(xaxis50k,datawmu[3], label = '0.25')
p5, = ax.plot(xaxis50k,datawmu[4], label = '0.45')
ax.set(xlabel='time [timestep / systemsize]',ylabel='cooperativity')
#ax.set(xlabel='time [timestep / systemsize]',ylabel='cooperativity', title='std friendship')
ax.set_ylim(-1,1)
ax.legend(loc='upper left')


figclust.savefig("clustering.png")
figinit.savefig("initialstate.png")
figinitmu.savefig("initialstatestd.png")
figphi.savefig("field.png")
figr.savefig("randomness.png")
figwi.savefig("stubbornness.png")
figwij.savefig("friendship.png")
figwmu.savefig("friendshipstd.png")

