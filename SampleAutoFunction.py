#!/usr/bin/env python

import BasicMath;

def ACVF(h, series = []) :
	th = abs(h);
	ms = BasicMath.mean(series);
	length = len(series);
	ss = 0.0;
	for i in range(length - th) :
		ss += (series[i + th] - ms) * (series[i] - ms);

	return (ss / length);

def ACF(h, series = []) :
	acvf0 = ACVF(0, series);
	acvfh = ACVF(h, series);

	return (acvfh / acvf0);
