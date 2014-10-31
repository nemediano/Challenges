# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 18:15:02 2014

@author: cdhagmann
"""

import numpy as np

def verlet(F, m, x0, v0, delta_t=.01, t_max=5):
    x = {0: x0}    
    x[1] = x[0] + v0 * delta_1
    for i in xrange(2, int(t_max / delta_T)):
        x[i] = 2 * x[i] - x[i-1] + F(delta_t * i) / float(m) * 
    