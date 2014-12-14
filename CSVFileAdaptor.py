#!/usr/bin/env python

import csv;

def csvReadSeriesData(filename) :
	series = [];
	rdr = csv.reader( open(filename, "r") );
	for row in rdr :
		series.append(float(row[0]));

	return series;


def csvWriteSeriesData(filename, series = []) :
	target = open(filename, "w");
	lenght = len(series);
	for i in range(lenght) :
		target.write(str(series[i]));
		target.write('\n');
	target.close();

