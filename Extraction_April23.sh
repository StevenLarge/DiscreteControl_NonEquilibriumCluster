#!/usr/bin/env python

#Extraction script for April discrete control data


BaseDir = ["SpaceOpt","TimeOpt"]

Param = ["9_15","12_15","15_15"]

NumDirs = 10

TimeScales = [10,50,200,400,600,800,1000,1200,1400,1600,1800,2000,2200,2400,2600,2800,3000]
TimeTrandCP = 25

SpaceScale = [4,8,16,32,64,128,256,512]
SpaceTrendTime = 2000

ProtClassTime = ["Naive","TimeOpt","FullOpt"]
ProtClassSpace = ["Naive","SpaceOpt","FullOpt"]

ReadNameBase = "WorkDist_12_15_"

for index1 in range(len(Param)):

	for index2 in range(10):

		for index3 in range(len(TimeScales)):

			CopyPath = "TimeOpt/Para_" + Param[index1] + "_" + str(index2+1) + "/" + "WorkDistributions/"
			Filename1 = "WorkDist_12_15_TimeOpt_CP25_T" + str(TimeScales[index3]) + ".dat"
			Filename2 = "WorkDist_12_15_Naive_CP25_T" + str(TimeScales[index3]) + ".dat"
			Filename3 = "WorkDist_12_15_FullOpt_CP25_T" + str(TimeScales[index3]) + ".dat" 
			#Filename1 = "WorkDist_" + Param[index1] + "TimeOpt_CP25_T" + str(TimeScales[index3]) + ".dat"
			#Filename2 = "WorkDist_" + Param[index1] + "Naive_CP25_T" + str(TimeScales[index3]) + ".dat"
			#Filename3 = "WorkDist_" + Param[index1] + "FullOpt_CP25_T" + str(TimeScales[index3]) + ".dat"

			CopyCommand1 = "cp " + CopyPath + Filename1 + " AggregateData"
			CopyCommand2 = "cp " + CopyPath + Filename2 + " AggregateData"
			CopyCommand3 = "cp " + CopyPath + Filename3 + " AggregateData"
			NameCommand1 = "mv AggregateData/" + Filename1 + " AggregateData/WorkDist_" + Param[index1] + "TimeOpt_CP25_T" + str(TimeScales[index3]) + "_" + str(index2+1) + ".dat"
			NameCommand2 = "mv AggregateData/" + Filename2 + " AggregateData/WorkDist_" + Param[index1] + "Naive_CP25_T" + str(TimeScales[index3]) + "_" + str(index2+1) + ".dat"
			NameCommand3 = "mv AggregateData/" + Filename3 + " AggregateData/WorkDist_" + Param[index1] + "FullOpt_CP25_T" + str(TimeScales[index3]) + "_" + str(index2+1) + ".dat"

			os.system(CopyCommand1)
			os.system(CopyCommand2)
			os.system(CopyCommand3)
			os.system(NameCommand1)
			os.system(NameCommand2)
			os.system(NameCommand3)


for index1 in range(len(Param)):

	for index2 in range(10):

		for index3 in range(len(SpaceScale)):

			CopyPath = "SpaceOpt/Para_" + Param[index1] + "_" + str(index2+1) + "/" + "WorkDistributions/"
			Filename1 = "WorkDist_12_15_SpaceOpt_CP" + str(SpaceScale[index3]) + "_T2000.dat"
			Filename2 = "WorkDist_12_15_Naive_CP" + str(SpaceScale[index3]) + "_T2000.dat"
			Filename3 = "WorkDist_12_15_FullOpt_CP" + str(SpaceScale[index3]) + "_T2000.dat"
			
			CopyCommand1 = "cp " + CopyPath + Filename1 + " AggregateData"
			CopyCommand2 = "cp " + CopyPath + Filename2 + " AggregateData"
			CopyCommand3 = "cp " + CopyPath + Filename3 + " AggregateData"
			NameCommand1 = "mv AggregateData/" + Filename1 + " AggregateData/WorkDist_" + Param[index1] + "SpaceOpt_CP" + str(SpaceScale[index3]) + "_T2000_" + str(index2+1) + ".dat"
			NameCommand2 = "mv AggregateData/" + Filename2 + " AggregateData/WorkDist_" + Param[index1] + "Naive_CP" + str(SpaceScale[index3]) + "_T2000_" + str(index2+1) + ".dat"
			NameCommand3 = "mv AggregateData/" + Filename3 + " AggregateData/WorkDist_" + Param[index1] + "FullOpt_CP" + str(SpaceScale[index3]) + "_T2000_" + str(index2+1) + ".dat"
				
			os.system(CopyCommand1)
			os.system(CopyCommand2)
			os.system(CopyCommand3)
			os.system(NameCommand1)
			os.system(NameCommand2)
			os.system(NameCommand3)
			

os.chdir('AggregateData')
TarCommand = "tar -cvf DistData_April23.tar *.dat"
CopyCommand = "cp *.tar .."
os.system(TarCommand)
os.system(CopyCommand)
os.chdir("..")

os.system("echo")
os.system("echo")
os.system("echo----- Finished -----")
os.system("echo")
os.system("echo")





