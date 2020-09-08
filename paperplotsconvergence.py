
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import glob
from scipy import stats
from scipy.interpolate import griddata
import matplotlib.ticker as ticker

def linreg(x, y): ## code stolen from geeksforkeeks
    x = np.array(x)
    y = np.array(y)
    
    n = np.size(x) 
     
    mx, my = np.mean(x), np.mean(y) 
  
    ssxy = np.sum(y*x) - n*my*mx 
    ssxx = np.sum(x*x) - n*mx*mx 
  
    b1 = ssxy / ssxx 
    b0 = my - b1*mx 
  
    return(b0, b1) 

statescl = np.loadtxt('./statestypecl.csv',delimiter=',')
statesgr = np.loadtxt('./statestypegrid.csv',delimiter=',')
statesinfcl = np.loadtxt('./statesinftypecllate.csv',delimiter=',')
statesinfgr = np.loadtxt('./statesinftypegrid.csv',delimiter=',')
statesdeg2 = np.loadtxt('./statesdegree2.csv',delimiter=',')
statesdeg4 = np.loadtxt('./statesdegree4.csv',delimiter=',')
statesdeg16 = np.loadtxt('./statesdegree16.csv',delimiter=',')
statesdeg32 = np.loadtxt('./statesdegree32.csv',delimiter=',')
statesnewpol025 = np.loadtxt('./statesnewPoliticalClimate0.025.csv',delimiter=',')
statesnewpol0375 = np.loadtxt('./statesnewPoliticalClimate0.0375.csv',delimiter=',')
statesnewpol075 = np.loadtxt('./statesnewPoliticalClimate0.075.csv',delimiter=',')
statesnewpol1 = np.loadtxt('./statesnewPoliticalClimate0.1.csv',delimiter=',')

statescl = statescl[:,0]
statesgr = statesgr[:,0]
statesinfcl = statesinfcl[:,0]
statesinfgr = statesinfgr[:,0]
statesdeg2 = statesdeg2[:,0]
statesdeg4 = statesdeg4[:,0]
statesdeg16 = statesdeg16[:,0]
statesdeg32 = statesdeg32[:,0]
statesnewpol025 = statesnewpol025[:,0]
statesnewpol0375 = statesnewpol0375[:,0]
statesnewpol075 = statesnewpol075[:,0]
statesnewpol1 = statesnewpol1[:,0]

allthestates = [statescl, statesgr, statesinfcl, statesinfgr, statesdeg2, statesdeg4, statesdeg16, statesdeg32, statesnewpol025, statesnewpol0375, statesnewpol075, statesnewpol1]

figtype, ax =  plt.subplots()
ax.plot(statescl,label="CSF")
ax.plot(statesgr,label="Grid")

ax.set(xlabel='timestep',ylabel='$\\langle$ state $\\rangle$')
ax.legend(loc = 'lower right')
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.25))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))
ax.xaxis.set_major_locator(ticker.MultipleLocator(10000))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(2500))
ax.xaxis.grid(True, linestyle='dotted')
ax.yaxis.grid(True, linestyle='dotted')
ax.set_ylim([-1,1])

figtype.savefig('networktype.png')

figdeg, ax =  plt.subplots()
ax.plot(statesdeg2,label="$\\langle k \\rangle = 2$")
ax.plot(statesdeg4,label="$\\langle k \\rangle = 4$")
ax.plot(statescl,label="$\\langle k \\rangle = 8$")
ax.plot(statesdeg16,label="$\\langle k \\rangle = 16$")
ax.plot(statesdeg32,label="$\\langle k \\rangle = 32$")

ax.set(xlabel='timestep',ylabel='$\\langle$ state $\\rangle$')
ax.legend(loc = 'lower right')
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.25))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))
ax.xaxis.set_major_locator(ticker.MultipleLocator(10000))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(2500))
ax.xaxis.grid(True, linestyle='dotted')
ax.yaxis.grid(True, linestyle='dotted')
ax.set_ylim([-1,1])

figdeg.savefig('avgdeg.png')

figfield, ax =  plt.subplots()
ax.plot(statesnewpol025, label = "$\\phi = 0.0250$")
ax.plot(statesnewpol0375, label = "$\\phi = 0.0375$")
ax.plot(statescl, label = "$\\phi = 0.05$")
ax.plot(statesnewpol075, label = "$\\phi = 0.0750$")
ax.plot(statesnewpol1, label = "$\\phi = 0.1000$")

ax.set(xlabel='timestep',ylabel='$\\langle$ state $\\rangle$')
ax.legend(loc = 'lower right')
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.25))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))
ax.xaxis.set_major_locator(ticker.MultipleLocator(10000))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(2500))
ax.xaxis.grid(True, linestyle='dotted')
ax.yaxis.grid(True, linestyle='dotted')
ax.set_ylim([-1,1])

figfield.savefig('fields.png')

figinf, ax =  plt.subplots()
ax.plot(statescl,label="CSF")
ax.plot(statesgr,label="Grid")
ax.plot(statesinfcl,label="CSF + Influencer")
ax.plot(statesinfgr,label="Grid + Influencer")

ax.set(xlabel='timestep',ylabel='$\\langle$ state $\\rangle$')
ax.legend(loc = 'lower right')
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.25))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))
ax.xaxis.set_major_locator(ticker.MultipleLocator(10000))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(2500))
ax.xaxis.grid(True, linestyle='dotted')
ax.yaxis.grid(True, linestyle='dotted')
ax.set_ylim([-1,1])

figinf.savefig('influencer.png')

figcomp, ax =  plt.subplots()
ax.plot(statescl,label="CSF")
ax.plot(statesdeg32,label="$\\langle k \\rangle$ = 32")
ax.plot(statesnewpol1, label = "$\\phi = 0.100$")
ax.plot(statesinfcl,label="CSF + Influencer")

ax.set(xlabel='timestep',ylabel='$\\langle$ state $\\rangle$')
ax.legend(loc = 'lower right')
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.25))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))
ax.xaxis.set_major_locator(ticker.MultipleLocator(10000))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(2500))
ax.xaxis.grid(True, linestyle='dotted')
ax.yaxis.grid(True, linestyle='dotted')
ax.set_ylim([-1,1])

figcomp.savefig('comparison.png')

statescll = 1 - statescl
statesgrl = 1 - statesgr
statesinfcll = 1 - statesinfcl
statesinfgrl = 1 - statesinfgr
statesdeg2l = 1 - statesdeg2
statesdeg4l = 1 - statesdeg4
statesdeg16l = 1 - statesdeg16
statesdeg32l = 1 - statesdeg32
statesnewpol025l = 1 - statesnewpol025
statesnewpol0375l = 1 - statesnewpol0375
statesnewpol075l = 1 - statesnewpol075
statesnewpol1l = 1 - statesnewpol1


figstateslog, ax =  plt.subplots()

ax.plot(statescll,label="CSF")
ax.plot(statesgrl,'-',label="Grid")
ax.plot(statesdeg16l,label="$\\langle k \\rangle$ = 16")
ax.plot(statesdeg4l,'-',label="$\\langle k \\rangle$ = 4")
ax.plot(statesnewpol1l, label = "$\\phi = 0.100$")
ax.plot(statesnewpol025l,'-', label = "$\\phi = 0.025$")
ax.plot(statesinfcll,label="CSF + Influencer")
ax.plot(statesinfgrl,'-',label="Gid + Influencer")
#ax.yaxis.set_major_locator(ticker.MultipleLocator(0.25))
#ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))
ax.xaxis.set_major_locator(ticker.MultipleLocator(10000))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(2500))
ax.xaxis.grid(True, linestyle='dotted')
ax.yaxis.grid(True, linestyle='dotted')
#ax.set_ylim([-1,1])
plt.yscale('log')

figstateslog.savefig('convlog.png')

masterrootlist = []

for states in allthestates : 
    root = 1
    index = 0
    for state in states :
        if abs(state) < abs(states[root]) :
            root = index
        index = index + 1
    masterrootlist.append(root)

rates = []
index = 0

for root in masterrootlist :    
    states = allthestates[index]
    regwin = 100
    dx = list(range(root-regwin , root+regwin +1))
    dy = states[root-regwin : root+regwin +1]
    coef = linreg(dx,dy)
    slope = coef[1]
    print (slope)
    rates.append(-slope/(states[root]-1))

ratesstd = rates[0:2]
ratesinf = rates[2:4]
ratesdeg = rates[4:8]
ratespol = rates[8:12]
        
print (ratespol)

figrates1, ax =  plt.subplots()
ax.plot(ratesdeg,'b*',label="cl")
ax.set(xlabel='Rate',ylabel='degree')
ax.xaxis.grid(True, linestyle='dotted')
ax.yaxis.grid(True, linestyle='dotted')

figrates1.savefig("ratesdeg.png")

figrates2, ax =  plt.subplots()
ax.plot(ratespol,'b*',label="cl")
ax.set(xlabel='rate',ylabel='pol')
ax.xaxis.grid(True, linestyle='dotted')
ax.yaxis.grid(True, linestyle='dotted')

figrates2.savefig("ratespol.png")
