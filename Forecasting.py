# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 20:52:29 2014

"""

#!/usr/bin/env python

#test
import BasicMath;
#import CSVFileAdaptor;

import numpy as np;

def sACVF(series, h) :
    th = np.abs(h);
    length = series.size;
    ss = 0.0;
    for i in range(length - th) :
        ss += (series[i+th] * series[i]);
    
    return (ss / length);
    

def DurbinLevinson(series = []) :
    arr = np.array(series, dtype=float);
    average = arr.mean();
    length = arr.size;
    for i in range(length) :
        arr[i] = arr[i] - average;
        
    acvfArray = np.arange(length + 1, dtype=float);   #store ACVF(0 ... length)     
    for i in range(length) :
        acvfArray[i] = sACVF(arr, i);
    acvfArray[length] = 0.0;
    
    vArray = np.arange(length + 1, dtype=float);  #refer to Vn in Durbin-Levinson Algorithm
    phiArray = np.arange(length + 1, dtype=float); #refer to Phi(ii) in Durbin-Levinson Algorithm
    
    #init
    phiArray[1] = acvfArray[1] / acvfArray[0];  #here exclude the phiArray[0]
    vArray[0] = acvfArray[0];
    vArray[1] = vArray[0] * (1 - (phiArray[1] * phiArray[1]));
    
    oldPHIs = [];   #refer to phi(n-1, i)
    for i in range(2, length + 1) :
        oldPHIs.append(phiArray[i-1]);
        ss = 0.0;
        for j in range(1, i):
            ss += oldPHIs[j-1] * acvfArray[length - j]
        phiArray[i] = (acvfArray[i] - ss) / vArray[i-1];
        
        newPHIs = [];
        factor = phiArray[i];
        size = len(oldPHIs);
        for k in range(size) :
            newPHIs.append(oldPHIs[k] - factor * oldPHIs[size-k-1])
        oldPHIs = newPHIs;
    
    oldPHIs.append(phiArray[length]);
    
    result = 0.0;
    for i in range(length) :
        result += series[i] * oldPHIs[i];
        
    return result;

#test
test = [];
length = 20;
for i in range(length) :
    test.append(5 + np.random.normal());
#CSVFileAdaptor.csvWriteSeriesData("stationary_series1.csv", test);
    
print("orginal series data:");
print(test);
print("=======================================================================");
    
average = BasicMath.mean(test);
for i in range(length) :
    test[i] = test[i] - average;
    
tmpResult = DurbinLevinson(test);
print("result value= ", tmpResult + average);

























