#!/usr/bin/env python

import os

Ext = [1,2,3,4,5,6,7,8,9,10]
Param = ["9_15","12_15","15_15"]

os.chdir("TimeOpt")

for index1 in range(len(Param)):

	for index2 in range(len(Ext)):

		CopyCommand = "cp NonEquilibrium_Protocol_Time.cpp Para_" + Param[index1] + "_" + str(Ext[index2]) + "/src"
		os.system(CopyCommand)

os.chdir("..")

os.chdir("SpaceOpt")

for index1 in range(len(Param)):

	for index2 in range(len(Ext)):

		CopyCommand = "cp NonEquilibrium_Protocol_Space.cpp Para_" + Param[index1] + "_" + str(Ext[index2]) + "/src"
		os.system(CopyCommand)

os.chdir("..")

os.system("./SubmissionScript_April12.sh")

