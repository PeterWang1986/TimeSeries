# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 14:58:39 2014

refer to chapter5 of 'Introduction Time Series and Forecasting'
"""

#!/usr/bin/env python

import numpy as np;
import scipy as sp;

import SampleAutoFunction as saf;

def YuleWalker(ArSeries, pOrder) :
    coefficients = [];
    length = len(ArSeries);
    
    if (pOrder<=0 or length<pOrder) :
        coefficients;

    gammas = np.arange(pOrder + 1, dtype = float);
    for i in range(pOrder + 1) :
        gammas[i] = saf.ACVF(i, ArSeries);
    
    temp = np.arange(pOrder * pOrder, dtype = float);
    for i in range(pOrder) :
        base = i * pOrder
        for j in range(pOrder) :
            temp[base + j] = gammas[np.abs(i-j)];

    A = temp.reshape((3, 3));
    b = gammas[1 : pOrder+1];  
    result = sp.linalg.lstsq(A, b);
    
    return result[0];