
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import glob
from scipy import stats
from scipy.interpolate import griddata
import matplotlib.ticker as ticker

systemsize = 33**2

# from separated data

heatdataraw = np.array([])
heatfiles = sorted(glob.glob('./runs*'))
it = 0
for f in heatfiles : 
    if (it == 0) :
        heatdataraw = np.loadtxt(open(f,"rb"),delimiter=',',skiprows=0)
    else :
        heatdataraw = np.append(heatdataraw,np.loadtxt(f,delimiter=','),axis=0)
    it = it + 1

#heatdataraw = np.array([])
#heatfiles = sorted(glob.glob('./runs*'))
#for f in heatfiles : 
#    heatdataraw = np.append(heatdataraw,np.loadtxt(f,delimiter=','),axis=0)
    
#heatdataraw = np.loadtxt('./runs1.csv',delimiter=',')
#heatdataraw = np.append(heatdataraw,np.loadtxt('./runs2.csv',delimiter=','),axis=0)
#heatdataraw = np.append(heatdataraw,np.loadtxt('./runs3.csv',delimiter=','),axis=0)

#heatdataraw = np.loadtxt('./runs0.csv',delimiter=',')

#heatdataraw = heatdataraw[:,0:300000]

#print (heatdataraw.shape)
print (len(heatdataraw))
print (len(heatdataraw[0]))

#statesavg = heatdataraw.mean(0)
#
#figstates, ax =  plt.subplots()
#ax.plot(statesavg, color='#ff7f0e', label="AVG state")
#ax.set(xlabel='timestep',ylabel='$\\langle$ state $\\rangle$')
#ax.xaxis.grid(True, linestyle='dotted')
#ax.yaxis.grid(True, linestyle='dotted')
#ax.set_ylim([-1,1])
#plt.xscale('log')
#plt.yscale('log')
#
#figstates.savefig('states.png')

### heatmap

#heatdataraw = np.loadtxt('./data/runs.csv',delimiter=',')
#heatdataraw = heatdataraw[:,0:150000]

elsinrow = len(heatdataraw[0])
ts = range (elsinrow)
times = []

for x in range (len(heatdataraw)) :
    times.append(ts)

times = np.array(times)
#times = times / systemsize
times = times.flatten()
heatdata = heatdataraw.flatten()

binsize = 100
xbins = np.arange(0,elsinrow,binsize)
ybins = np.linspace(-1.0,1.0,elsinrow/binsize)

def isnan (n) :
    return n != n

heatdatabinned = stats.binned_statistic_2d(times,heatdata,heatdata,'count',bins=[xbins,ybins])

heatdatabinned = np.array(heatdatabinned.statistic)
heatdatabinned = heatdatabinned.T

#for el in np.nditer(heatdata,op_flags=['readwrite']) :
#    if isnan(el) :
#        el[...] = 0

xbins = xbins + (xbins[1]-xbins[0])/2
ybins = ybins + (ybins[1]-ybins[0])/2

xbins = xbins[:-1]
ybins = ybins[:-1]

heatmap, ax = plt.subplots()

#im = ax.pcolormesh(xbins,ybins,heatdatabinned,cmap='inferno',shading='gouraud',vmin=0,vmax=binsize*10)
#im = ax.pcolormesh(xbins,ybins,heatdatabinned,cmap='inferno',vmin=0,vmax=binsize*1,)
im = ax.imshow(heatdatabinned,cmap='inferno',vmin=0,vmax=binsize*1,extent=[0,275,-1,1],interpolation='nearest',origin='lower',aspect='auto')
ax.set(xlabel='time [timestep / system size]', ylabel='cooperativity')

cbar = heatmap.colorbar(im)
cbar.ax.set_ylabel('counts')

heatmap.savefig('heatmap.png')

