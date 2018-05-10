#This is a python script that checks whether or not the required protocols are contained in the local folders for 
#Discrete control simulations
#
#Steven Large
#April 14th 2018

import os

def NaiveProtocolGenerator(WriteName,CPVals,TotalTime):

	CPDist = 2
	CurrCP = -1

	CPStep = float(CPDist)/float(CPVals-1)

	Protocol_CP = []
	Protocol_Time = []

	for index in range(CPVals):
		Protocol_CP.append(CurrCP)
		CurrCP += CPStep

	TimeStep = TotalTime/float(CPVals - 2)

	for index in range(CPVals-2):
		Protocol_Time.append(TimeStep)

	Protocol_Time.append(100)
	Protocol_Time.insert(0,100)

	file1 = open(WriteName,'w')
	for index in range(len(Protocol_Time)):
		file1.write("%lf\t%lf\n" % (Protocol_CP[index],Protocol_Time[index]))
	file1.close()


TimeTrend = [10,50,200,400,800,1000,1200,1400,1600,1800,2000,2200,2400,2600,2800,3000]
CPTrend = [4,8,16,32,64,128,256,512]

CPFixed = 25
TimeFixed = 200

Para_Ex = ["9_15","12_15","15_15"]

MissingArray = []
TimeArray = []
CPArray = []

for index1 in range(len(Para_Ex)):

	ReadPath = "Protocols_" + Para_Ex[index1] + "/"

	for index2 in range(len(CPTrend)):

		NaiveName = "Naive_CP" + str(CPTrend[index2]) + "_T200.dat"
		SpaceName = "SpaceOpt_CP" + str(CPTrend[index2]) + "_T200.dat"

		FullNameNaive = ReadPath + NaiveName
		FullNameSpace = ReadPath + SpaceName

		if(os.path.exists(FullNameSpace)==False):
			MissingArray.append(FullNameSpace)
			TimeArray.append(200)
			CPArray.append(CPTrend[index2])

		if(os.path.exists(FullNameNaive)==False):
			MissingArray.append(FullNameNaive)
			TimeArray.append(200)
			CPArray.append(CPTrend[index2])

	for index3 in range(len(TimeTrend)):

		NaiveName = "Naive_CP25_T" + str(TimeTrend[index3]) + ".dat"
		TimeName = "TimeOpt_CP25_T" + str(TimeTrend[index3]) + ".dat" 

		FullNameNaive = ReadPath + NaiveName
		FullNameTime = ReadPath + TimeName

		if(os.path.exists(FullNameNaive)==False):
			MissingArray.append(FullNameNaive)
			TimeArray.append(TimeTrend[index3])
			CPArray.append(25)

		if(os.path.exists(FullNameTime)==False):
			MissingArray.append(FullNameTime)
			TimeArray.append(TimeTrend[index3])
			CPArray.append(25)


print "\n\n\t\t----- Checks Done -----\n\n"

print "Missing Files --> \n"
for index in range(len(MissingArray)):
	print MissingArray[index]

print "\n\n"

for index in range(len(MissingArray)):
	if "Naive" in MissingArray[index]:
		NaiveProtocolGenerator(MissingArray[index],CPArray[index],TimeArray[index])
	
