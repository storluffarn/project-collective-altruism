
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import glob
import math
from scipy import stats
from scipy.interpolate import griddata
import matplotlib.ticker as ticker

systemsize = 33**2

def linreg(x, y): ## snippet stolen from geeksforkeeks
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
statescllong = np.loadtxt('./statescllong.csv',delimiter=',')

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
statescllong = statescllong[:,0]

xaxis50k = np.array(list(range(len(statescl)))) / systemsize
xaxis150k = np.array(list(range(len(statescllong)))) / systemsize


figtype, ax =  plt.subplots()
ax.plot(xaxis50k,statescl,label="CSF")
ax.plot(xaxis50k,statesgr,label="Grid")
ax.set(xlabel='time [timestep / system size]',ylabel='$cooperativity')
ax.legend(loc = 'lower right')
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.25))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(2.5))
ax.xaxis.grid(True, linestyle='dotted')
ax.yaxis.grid(True, linestyle='dotted')
ax.set_ylim([-1,1])

figtype.savefig('networktype.png')

figdeg, ax =  plt.subplots()
ax.plot(xaxis50k,statesdeg2,label="$\\langle k \\rangle = 2$")
ax.plot(xaxis50k,statesdeg4,label="$\\langle k \\rangle = 4$")
ax.plot(xaxis50k,statescl,label="$\\langle k \\rangle = 8$")
ax.plot(xaxis50k,statesdeg16,label="$\\langle k \\rangle = 16$")
ax.plot(xaxis50k,statesdeg32,label="$\\langle k \\rangle = 32$")

ax.set(xlabel='time [timestep / system size]',ylabel='cooperativity')
ax.legend(loc = 'lower right')
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.25))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(2.5))
#ax.xaxis.set_major_locator(ticker.MultipleLocator(10000))
#ax.xaxis.set_minor_locator(ticker.MultipleLocator(2500))
ax.xaxis.grid(True, linestyle='dotted')
ax.yaxis.grid(True, linestyle='dotted')
ax.set_ylim([-1,1])

figdeg.savefig('avgdeg.png')

figfield, ax =  plt.subplots()
ax.plot(xaxis50k,statesnewpol025, label = "$\\phi = 0.0250$")
ax.plot(xaxis50k,statesnewpol0375, label = "$\\phi = 0.0375$")
ax.plot(xaxis50k,statescl, label = "$\\phi = 0.05$")
ax.plot(xaxis50k,statesnewpol075, label = "$\\phi = 0.0750$")
ax.plot(xaxis50k,statesnewpol1, label = "$\\phi = 0.1000$")

ax.set(xlabel='time [timestep / system size]',ylabel='cooperativity')
ax.legend(loc = 'lower right')
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.25))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(2.5))
ax.xaxis.grid(True, linestyle='dotted')
ax.yaxis.grid(True, linestyle='dotted')
ax.set_ylim([-1,1])

figfield.savefig('fields.png')

figinf, ax =  plt.subplots()
ax.plot(xaxis50k,statescl,label="CSF")
ax.plot(xaxis50k,statesgr,label="Grid")
ax.plot(xaxis50k,statesinfcl,label="CSF + Influencer")
ax.plot(xaxis50k,statesinfgr,label="Grid + Influencer")

ax.set(xlabel='time [timestep / system size]',ylabel='cooperativity')
ax.legend(loc = 'lower right')
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.25))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(2.5))
ax.xaxis.grid(True, linestyle='dotted')
ax.yaxis.grid(True, linestyle='dotted')
ax.set_ylim([-1,1])

figinf.savefig('influencer.png')

figcomp, ax =  plt.subplots()
ax.plot(xaxis50k,statescl,label="CSF")
ax.plot(xaxis50k,statesdeg32,label="$\\langle k \\rangle$ = 32")
ax.plot(xaxis50k,statesnewpol1, label = "$\\phi = 0.100$")
ax.plot(xaxis50k,statesinfcl,label="CSF + Influencer")

ax.set(xlabel='time [timestep / system size]',ylabel='cooperativity')
ax.legend(loc = 'lower right')
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.25))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(2.5))
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
statescllongl = 1 - statescllong


figstateslog, ax =  plt.subplots()

ax.plot(xaxis50k,statescll,label="CSF")
ax.plot(xaxis50k,statesgrl,'-',label="Grid")
#ax.plot(xaxis50k,statesdeg16l,label="$\\langle k \\rangle$ = 16")
ax.plot(xaxis50k,statesdeg4l,'-',label="$\\langle k \\rangle$ = 4")
ax.plot(xaxis50k,statesnewpol1l, label = "$\\phi = 0.100$")
ax.plot(xaxis50k,statesnewpol025l,'-', label = "$\\phi = 0.025$")
ax.plot(xaxis50k,statesinfcll,label="CSF + Influencer")
#ax.plot(xaxis50k,statesinfgrl,'-',label="Gid + Influencer")
ax.legend(loc = 'lower left')
ax.set(xlabel='time [timestep / system size]',ylabel='1 - cooperativity')
#ax.yaxis.set_major_locator(ticker.MultipleLocator(0.25))
#ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))
ax.xaxis.grid(True, linestyle='dotted')
ax.yaxis.grid(True, linestyle='dotted')
#ax.set_ylim([-1,1])
plt.yscale('log')

figstateslog.savefig('convlog.png')

figstatesloglong, ax =  plt.subplots()

ax.plot(xaxis150k,statescllongl,label="CSF")
ax.legend(loc = 'lower left')
ax.set(xlabel='time [timestep / system size]',ylabel='1 - cooperativity')
#ax.yaxis.set_major_locator(ticker.MultipleLocator(0.25))
#ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))
ax.xaxis.grid(True, linestyle='dotted')
ax.yaxis.grid(True, linestyle='dotted')
#ax.set_ylim([-1,1])
plt.yscale('log')

figstatesloglong.savefig('convloglong.png')

allthestates = [statescl, statesgr, statesinfcl, statesinfgr, statesdeg2, statesdeg4, statesdeg16, statesdeg32, statesnewpol025, statesnewpol0375, statesnewpol075, statesnewpol1]

masterrootlist = []

for states in allthestates : 
    root = 0
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
    nstates = len(states)
    regwin = 10
    dx = list(range(root-regwin , root+regwin +1))
    dy = states[root-regwin : root+regwin +1]
    coef = linreg(dx,dy)
    slope = coef[1]
    print (index,root,slope)
    rates.append(-slope/(states[root]-1))
    #rates.append(slope)
    index = index + 1

ratesstd = rates[0:2]
ratesinf = rates[2:4]
ratesdeg = rates[4:8]
ratespol = rates[8:12]
ratesdeg.insert(math.floor(len(ratesdeg)*0.5),ratesstd[0])
ratespol.insert(math.floor(len(ratespol)*0.5),ratesstd[0])

rscale = 1000;
ratespol = np.array(ratespol) * rscale
ratesdeg = np.array(ratesdeg) * rscale
ratesinf = np.array(ratesinf) * rscale

print (ratespol)
print (ratesdeg)
print (ratesinf)

xvals = [2,4,8,16,32]

figrates1, ax =  plt.subplots()
ax.plot(xvals,ratesdeg,'b*',label="cl")
ax.set(xlabel='$\\langle k \\rangle$',ylabel='rate ($\\times${})'.format(rscale))
ax.xaxis.grid(True, linestyle='dotted')
ax.yaxis.grid(True, linestyle='dotted')
ax.set_xlim([0,35])
ax.set_ylim([0,0.00014*rscale])

figrates1.savefig("ratesdeg.png")

xvals = [0.025,0.0375,0.05,0.075,0.1]

figrates2, ax =  plt.subplots()
ax.plot(xvals,ratespol,'b*',label="cl")
ax.set(xlabel='$\\phi$',ylabel='rate ($\\times${})'.format(rscale))
ax.xaxis.grid(True, linestyle='dotted')
ax.yaxis.grid(True, linestyle='dotted')
ax.set_xlim([0,0.11])
ax.set_ylim([0,0.00018 * rscale])

figrates2.savefig("ratespol.png")




