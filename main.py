#!/usr/bin/env python

import CSVFileAdaptor;
import SampleAutoFunction;

series = [0.4, 0.7, 0.5, 0.75, 0.6, 0.8, 0.55, 0.79, 0.65];
length = len(series);

CSVFileAdaptor.csvWriteSeriesData("data.csv", series);
seriesdata = CSVFileAdaptor.csvReadSeriesData("data.csv");

series2 = [];
for i in range(length - 1) :
	series2.append(SampleAutoFunction.ACVF(i, series));
CSVFileAdaptor.csvWriteSeriesData("test1.csv", series2);

series3 = [];
for i in range(length - 1) :
	series3.append(SampleAutoFunction.ACVF(i, seriesdata));
CSVFileAdaptor.csvWriteSeriesData("test2.csv", series3);
