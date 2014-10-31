# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 18:15:02 2014

@author: nemediano
"""

import numpy as np
import math

def damper_spring(x, v, L):
	K_s = 0.5
    if x != L:
		f = K_s * math.fabs(L - x)
    else
		f = 0
    return f;