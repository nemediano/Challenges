# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 18:15:02 2014

@author: cdhagmann
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16

def spring(x):
    k = 1.0
    return -k*x

def verlet(F, m, x0, v0, Dt=.01, t_max=5):
    '''
    Apply Verlet Integration
    '''
    nsteps = int(t_max / Dt)
    
    x = np.zeros( (nsteps + 1) )
    v = np.zeros( (nsteps + 1) )
    t = np.zeros( (nsteps + 1) )
    
    x[0] = x0
    v[0] = v0
    t[0] = 0.0
    
    x[1] = x[0] + v[0] * Dt
    t[1] = Dt
    for i in xrange(2, nsteps):
            x[i+1] = 2 * x[i] - x[i-1] + F(x[i]) * Dt ** 2.0 / float(m)
            t[i+1] = t[i] + Dt
        
    return t, x

if __name__ == "__main__":
    
    t, x = verlet(spring, 1.0, 1.0, 0.0, Dt=.01, t_max=5)

    plt.plot(t,x)
    plt.xlabel(r"$t$", size=18)
    plt.ylabel(r"$x$", size=18)
    plt.show()
