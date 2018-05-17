#!/usr/bin/env python

import os

if(os.path.exists("SpaceAggregate")==False):
	os.mkdir("SpaceAggregate")


Para_Array = ["9_15","12_15","15_15"]
CPVals = ["4","8","16","32","64","128","256","512"]

if(os.path.exists("SpaceAggregate")==False):
	os.mkdir("SpaceAggregate")

for index1 in range(len(Para_Array)):

	for index2 in range(10):

		for index3 in range(len(CVals)):

			TargetDir = "SpaceOpt/Para_" + Para_Array[index1] + "/WorkDistributions/"
			NaiveName = "WorkDist_" + Para_Array[index1] + "_Naive_CP" + CPVals[index3] + "_T2000.dat"
			SpaceOptName = "WorkDist_" + Para_Array[index1] + "_SpaceOpt_CP" + CPVals[index3] + "_T2000.dat"
			FullOptName = "WorkDist_" + Para_Array[index1] + "_FullOpt_CP" + CPVals[index3] + "_T2000.dat"

			CopyCommand1 = "cp " TargetDir + NaiveName " SpaceAggregate"
			CopyCommand2 = "cp " TargetDir + SpaceOptName " SpaceAggregate"
			CopyCommand3 = "cp " TargetDir + FullOptName " SpaceAggregate"
			
			os.system(CopyCommand1)
			os.system(CopyCommand2)
			os.system(CopyCommand3)


