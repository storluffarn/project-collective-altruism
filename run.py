from multiprocessing import Pool
import models 
import numpy as np
import random
import matplotlib.pyplot as plt
#from networkx.drawing.nx_agraph import graphviz_layout, to_agraph
from copy import deepcopy
import seaborn as sns
#import pygraphviz as pgv
from statistics import stdev, mean
import imageio
import networkx as nx
from scipy.stats import truncnorm
from itertools import repeat
import time
import multiprocessing
import os
from pathlib import Path

#Constants and Variables
plt.rcParams["svg.fonttype"] = "none"
#plt.rcParams["font.size"] = 16
plt.rcParams["savefig.directory"] = "Master/Comp/New"
#plt.rcParams["savefig.format"] = "svg"

s =100 #10^3 
if __name__ ==  '__main__': 
    num_processors = 8
    start = time.time()
    p=Pool( processes = num_processors)
    variables = [  0.6 ]
    
    for v in variables:
        fg= plt.figure(figsize=(16, 16))
        fn = Path(f'~/Documents/Prosjek/Master/Comp/New/144-k10-wi{v}-50s-skew-0.1-PU0.05-new.svg').expanduser()
        #fn = Path(f'~/Documents/Prosjek/Master/Comp/New/144-k10-wi{v}-50s-skew0.05-comparewi.svg').expanduser()        
        args1 = {"continuous": True, "type" : "rand", "d": 5, 'selfWeight': v}
        args2 = {"continuous": True, "type" : "cl", "d": 5, 'selfWeight':v}
        args3 = {"continuous": False, "type" : "rand",  "d": 5, 'selfWeight':v}
        args4 = {"continuous": False, "type" : "cl",  "d": 5, 'selfWeight':v}
        #args5 = {"continuous": True, "type" : "sf",  "d": 5, 'selfWeight':v}
        #args6 = {"continuous": False, "type" : "sf",  "d": 5, 'selfWeight':v}        
        sim1 = p.starmap(models.simulate, zip(range(s), repeat(args1)))
        sim2 = p.starmap(models.simulate, zip(range(s), repeat(args2)))
        sim3 = p.starmap(models.simulate, zip(range(s), repeat(args3)))
        sim4 = p.starmap(models.simulate, zip(range(s), repeat(args4)))
        #sim5 = p.starmap(models.simulate, zip(range(s), repeat(args5)))
        #sim6 = p.starmap(models.simulate, zip(range(s), repeat(args6)))
        
        simtime= time.time()
        print(f'Time to simulate: {simtime-start}s\n')
        fg= plt.figure()
        fg.subplots(nrows=1, ncols=2 )
        #print(nx.info(sim1[1].graph))  
        models.drawAvgState(sim1, avg=True, pltNr=1, title="rand cont", clusterSD=True)
        models.drawAvgState(sim2, avg=True, pltNr=2, title="cl cont",clusterSD=True )
        models.drawAvgState(sim3, avg=True, pltNr=3, title="rand dis",clusterSD=True)
        models.drawAvgState(sim4, avg=True, pltNr=4, title="cl disc",clusterSD=True )
        #models.drawAvgState(sim5, avg=True, pltNr=5, title="sf cont",clusterSD=True)
        #models.drawAvgState(sim6, avg=True, pltNr=6, title="sf disc",clusterSD=True )
        plt.legend()
        models.drawCrossSection(sim1)
        models.drawCrossSection(sim2, pltNr=2)
        models.drawCrossSection(sim3, pltNr=3)
        models.drawCrossSection(sim4, pltNr=4)
        #models.drawCrossSection(sim5, pltNr=5)
        #models.drawCrossSection(sim6, pltNr=6)
        #models.drawClustersizes(sim1)
        #models.drawClustersizes(sim2, pltNr=2)
        #models.drawClustersizes(sim3, pltNr=3)
        #models.drawClustersizes(sim4, pltNr=4)
        

        plt.draw()
        fg.savefig(fn, bbox_inches='tight')
        plt.close
    end = time.time()
    mins = (end - start) / 60
    sec = (end - start) % 60
    print(f'Time to complete: {mins:5.0f} mins {sec}s\n')
    
    #fn = Path('~/Documents/Prosjek/Master/Comp/rdtest.svg').expanduser()

    #fg.savefig(fn, bbox_inches='tight')
    """plt.xlabel("timesteps")
    plt.ylabel("fraction of cooperators")
    plt.ylim((0, 1))
    

    for i in range(s):
        plt.plot(mods[i].ratio)
        
    #models.avgRadialDist(mods, 6, False)
    plt.show()"""
    