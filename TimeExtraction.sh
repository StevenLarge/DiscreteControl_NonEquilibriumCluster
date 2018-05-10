#!/usr/bin/env python

import os

Param = ["9_15","12_15","15_15"]
NumDirs = 10
TimeScales = [10,50,200,400,600,800,1000,1200,1400,1600,1800,2000,2200,2400,2600,2800,3000]

if(os.path.exists("TimeAggregated")==False):
	os.mkdir(TimeAggregated)


for index1 in range(len(Param)):

	for index2 in range(10):

		for index3 in range(len(TimeScales)):

			DistNaive = "TimeOpt/Param_" + Param[index1] + "_" + str(index2+1) + "/WorkDistributions/WorkDist_" + Param[index1] + "_Naive_CP25_T" + str(TimeScales[index3]) + ".dat"	
			DistTimeOpt = "TimeOpt/Param_" + Param[index1] + "_" + str(index2+1) + "/WorkDistributions/WorkDist_" + Param[index1] + "_TimeOpt_CP25_T" + str(TimeScales[index3]) + ".dat"
			DistFullOpt = "TimeOpt/Param_" + Param[index1] + "_" + str(index2+1) + "/WorkDistributions/WorkDist_" + Param[index1] + "_FullOpt_CP25_T" + str(TimeScales[index3]) + ".dat"	
			CopyNaive = "cp " + DistNaive + " TimeAggregated"
			CopyTimeOpt = "cp " + DistTimeOpt + " TimeAggregated"
			CopyFullOpt = "cp " + DistFullOpt + " TimeAggregated"

			RenameNaive = "mv TimeAggregated/WorkDist_" + Param[index1] + "_Naive_CP25_T" + str(TimeScales[index3]) + ".dat TimeAggregated/WorkDist_N_T" + str(TimeScales[index3]) + ".dat"
			RenameTimeOpt = "mv TimeAggregated/WorkDist_" + Param[index1] + "_TimeOpt_CP25_T" + str(TimeScales[index3]) + ".dat TimeAggregated/WorkDist_T_T" + str(TimeScales[index3]) + ".dat"
			RenameFullOpt = "mv TimeAggregated/WorkDist_" + Param[index1] + "_FullOpt_CP25_T" + str(TimeScales[index3]) + ".dat TimeAggregated/WorkDist_F_T" + str(TimeScales[index3]) + ".dat"

			os.system(CopyNaive)
			os.system(CopyTimeOpt)
			os.system(CoptFullOpt)

			os.system(RenameNaive)
			os.system(RenameTimeOpt)
			os.system(RenameFullOpt)






