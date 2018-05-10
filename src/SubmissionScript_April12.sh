#!/usr/bin/env python

import os

ClassDir = ["TimeOpt","SpaceOpt"]

ParaDir = ["9_15_1","9_15_2","9_15_3","9_15_4","9_15_5","12_15_1","12_15_2","12_15_3","12_15_4","12_15_5","15_15_1","15_15_2","15_15_3","15_15_4","15_15_5"]

for index1 in range(len(ClassDir)):

	os.chdir(ClassDir[index1])

	os.system("echo ProtClass")

	for index2 in range(len(ParaDir)):

		os.system("echo \"     ParaDir\"")

		DirName = "Para_" + ParaDir[index2]

		os.chdir(DirName)
		os.mkdir("WorkDistributions")
		os.system("make clean")
		os.system("make")
		os.system("sbatch SlurmSubmission.sh")
		os.chdir("..")

	os.chdir("..")


