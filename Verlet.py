# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 18:15:02 2014

@author: cdhagmann
"""

import numpy as np

def verlet(F, m, x0, v0, Dt=.01, t_max=5):
    '''
    Apply Verlet Integration
    '''
    nsteps = tmax / Dt
    
    x = np.zeros( (nsteps + 1) )
    v = np.zeros( (nsteps + 1) )
    t = np.zeros( (nsteps + 1) )
    
    x[0] = x0
    v[0] = v0
    t[0] = 0.0
    
    x[1] = x[0] + v[0] * Dt + 0.5 * Dt ** 2 * F(x[0]) / m
    for i in xrange(1, nsteps):
        x[i+1] = 2 * x[i] - x[i-1] + F(x[i]) * Dt ** 2.0 / float(m)
        
    return x
    