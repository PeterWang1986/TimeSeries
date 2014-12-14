# -*- coding: utf-8 -*-
"""
Created on Tue Dec 09 15:15:01 2014

@author: I067331
"""

#/usr/bin/env python

import math;
import numpy as np;

import CSVFileAdaptor;

len = 144;
arr = [];
f = math.pi / 6.0;

for i in range (len):
    arr.append(3.0 * math.sin(i * f) + np.random.normal());
    #arr.append(math.sin(i * f));
    
CSVFileAdaptor.csvWriteSeriesData("seasonal_series2.csv", arr);