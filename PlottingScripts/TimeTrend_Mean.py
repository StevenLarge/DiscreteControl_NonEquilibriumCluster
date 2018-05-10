#This script plots the mean work and associated errors from the discrete control simulations
#
#Steven Large
#May 1st 2018

import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def ImportData(Path,Filename):
	
	Work = []
	WorkErr = []
	Time = []

	CompleteName = os.path.join(Path,Filename)

	file1 = open(CompleteName,'r')
	TempData = file1.readlines()
	file1.close()

	for index in range(len(TempData)):
		Parsed = TempData[index].split()
		Time.append(eval(Parsed[0]))
		Work.append(eval(Parsed[1]))
		WorkErr.append(eval(Parsed[2]))

	return Time,Work,WorkErr


ReadPath = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/NonEquilibrium_Local/WorkAnalysisFiles/"

ReadName_N_9 = "MeanWorkTrend_N_Time_9.dat"
ReadName_N_12 = "MeanWorkTrend_N_Time_12.dat"
ReadName_N_15 = "MeanWorkTrend_N_Time_15.dat"

ReadName_T_9 = "MeanWorkTrend_T_Time_9.dat"
ReadName_T_12 = "MeanWorkTrend_T_Time_12.dat"
ReadName_T_15 = "MeanWorkTrend_T_Time_15.dat"

ReadName_F_9 = "MeanWorkTrend_F_Time_9.dat"
ReadName_F_12 = "MeanWorkTrend_F_Time_12.dat"
ReadName_F_15 = "MeanWorkTrend_F_Time_15.dat"

Time_N_9,Work_N_9,WorkErr_N_9 = ImportData(ReadPath,ReadName_N_9)
Time_N_12,Work_N_12,WorkErr_N_12 = ImportData(ReadPath,ReadName_N_12)
Time_N_15,Work_N_15,WorkErr_N_15 = ImportData(ReadPath,ReadName_N_15)

Time_T_9,Work_T_9,WorkErr_T_9 = ImportData(ReadPath,ReadName_T_9)
Time_T_12,Work_T_12,WorkErr_T_12 = ImportData(ReadPath,ReadName_T_12)
Time_T_15,Work_T_15,WorkErr_T_15 = ImportData(ReadPath,ReadName_T_15)

Time_F_9,Work_F_9,WorkErr_F_9 = ImportData(ReadPath,ReadName_F_9)
Time_F_12,Work_F_12,WorkErr_F_12 = ImportData(ReadPath,ReadName_F_12)
Time_F_15,Work_F_15,WorkErr_F_15 = ImportData(ReadPath,ReadName_F_15)

WorkDiff_N_9 = []
WorkDiff_T_9 = []
WorkDiff_F_9 = []

WorkDiff_N_12 = []
WorkDiff_T_12 = []
WorkDiff_F_12 = []

WorkDiff_N_15 = []
WorkDiff_T_15 = []
WorkDiff_F_15 = []

for index in range(len(Work_N_9)):
	WorkDiff_N_9.append(Work_N_9[index] - Work_N_9[index])
	WorkDiff_T_9.append(Work_T_9[index] - Work_N_9[index])
	WorkDiff_F_9.append(Work_F_9[index] - Work_N_9[index])

	WorkDiff_N_12.append(Work_N_12[index] - Work_N_12[index])
	WorkDiff_T_12.append(Work_T_12[index] - Work_N_12[index])
	WorkDiff_F_12.append(Work_F_12[index] - Work_N_12[index])

	WorkDiff_N_15.append(Work_N_15[index] - Work_N_15[index])
	WorkDiff_T_15.append(Work_T_15[index] - Work_N_15[index])
	WorkDiff_F_15.append(Work_F_15[index] - Work_N_15[index])

WorkRatio_N_9 = []
WorkRatio_T_9 = []
WorkRatio_F_9 = []

WorkRatio_N_12 = []
WorkRatio_T_12 = []
WorkRatio_F_12 = []

WorkRatio_N_15 = []
WorkRatio_T_15 = []
WorkRatio_F_15 = []

for index in range(len(Work_N_9)):
	WorkRatio_N_9.append(Work_N_9[index]/Work_N_9[index])
	WorkRatio_T_9.append(Work_T_9[index]/Work_N_9[index])
	WorkRatio_F_9.append(Work_F_9[index]/Work_N_9[index])

	WorkRatio_N_12.append(Work_N_12[index]/Work_N_12[index])
	WorkRatio_T_12.append(Work_T_12[index]/Work_N_12[index])
	WorkRatio_F_12.append(Work_F_12[index]/Work_N_12[index])

	WorkRatio_N_15.append(Work_N_15[index]/Work_N_15[index])
	WorkRatio_T_15.append(Work_T_15[index]/Work_N_15[index])
	WorkRatio_F_15.append(Work_F_15[index]/Work_N_15[index])


sns.set(style='darkgrid',palette='muted',color_codes=True)

fig,ax = plt.subplots(3,3)

ax[0,0].plot(Time_N_9,Work_N_9,'r--',linewidth=2.5,alpha=0.5)
ax[0,1].plot(Time_N_12,Work_N_12,'r--',linewidth=2.5,alpha=0.5)
ax[0,2].plot(Time_N_15,Work_N_15,'r--',linewidth=2.5,alpha=0.5)

ax[0,0].plot(Time_T_9,Work_T_9,'b--',linewidth=2.5,alpha=0.5)
ax[0,1].plot(Time_T_12,Work_T_12,'b--',linewidth=2.5,alpha=0.5)
ax[0,2].plot(Time_T_15,Work_T_15,'b--',linewidth=2.5,alpha=0.5)

#ax[0].plot(Time_F_9,Work_F_9,'g--',linewidth=2.5,alpha=0.5)
#ax[1].plot(Time_F_12,Work_F_12,'g--',linewidth=2.5,alpha=0.5)
#ax[2].plot(Time_F_15,Work_F_15,'g--',linewidth=2.5,alpha=0.5)

ax[0,0].errorbar(Time_N_9,Work_N_9,yerr=WorkErr_N_9,fmt='ro',alpha=0.9,label="Naive")
ax[0,1].errorbar(Time_N_12,Work_N_12,yerr=WorkErr_N_12,fmt='ro',alpha=0.9,label="Naive")
ax[0,2].errorbar(Time_N_15,Work_N_15,yerr=WorkErr_N_15,fmt='ro',alpha=0.9,label="Naive")

ax[0,0].errorbar(Time_T_9,Work_T_9,yerr=WorkErr_T_9,fmt='bo',alpha=0.9,label="Time-Optimized")
ax[0,1].errorbar(Time_T_12,Work_T_12,yerr=WorkErr_T_12,fmt='bo',alpha=0.9,label="Time-Optimized")
ax[0,2].errorbar(Time_T_15,Work_T_15,yerr=WorkErr_T_15,fmt='bo',alpha=0.9,label="Time-Optimized")

#ax[0].errorbar(Time_F_9,Work_F_9,yerr=WorkErr_F_9,fmt='go',alpha=0.5,label="Fully-Optimal")
#ax[1].errorbar(Time_F_12,Work_F_12,yerr=WorkErr_F_12,fmt='go',alpha=0.5,label="Fully-Optimal")
#ax[2].errorbar(Time_F_15,Work_F_15,yerr=WorkErr_F_15,fmt='go',alpha=0.5,label="Fully-Optimal")

ax[1,0].plot(Time_N_9,WorkDiff_N_9,'r--',linewidth=2.5)
ax[1,0].plot(Time_N_9,WorkDiff_N_9,'ro')
ax[1,0].plot(Time_T_9,WorkDiff_T_9,'b--',linewidth=2.5)
ax[1,0].plot(Time_T_9,WorkDiff_T_9,'bo')
#ax[1,0].plot(Time_F_9,WorkDiff_F_9,'g--',linewidth=2.5)
#ax[1,0].plot(Time_F_9,WorkDiff_F_9,'go')

ax[1,1].plot(Time_N_12,WorkDiff_N_12,'r--',linewidth=2.5)
ax[1,1].plot(Time_N_12,WorkDiff_N_12,'ro')
ax[1,1].plot(Time_T_12,WorkDiff_T_12,'b--',linewidth=2.5)
ax[1,1].plot(Time_T_12,WorkDiff_T_12,'bo')
#ax[1,1].plot(Time_F_12,WorkDiff_F_12,'g--',linewidth=2.5)
#ax[1,1].plot(Time_F_12,WorkDiff_F_12,'go')

ax[1,2].plot(Time_N_15,WorkDiff_N_15,'r--',linewidth=2.5)
ax[1,2].plot(Time_N_15,WorkDiff_N_15,'ro')
ax[1,2].plot(Time_T_15,WorkDiff_T_15,'b--',linewidth=2.5)
ax[1,2].plot(Time_T_15,WorkDiff_T_15,'bo')
#ax[1,2].plot(Time_F_15,WorkDiff_F_15,'g--',linewidth=2.5)
#ax[1,2].plot(Time_F_15,WorkDiff_F_15,'go')


ax[2,0].plot(Time_N_9,WorkRatio_N_9,'r--',linewidth=2.5)
ax[2,0].plot(Time_N_9,WorkRatio_N_9,'ro')
ax[2,0].plot(Time_T_9,WorkRatio_T_9,'b--',linewidth=2.5)
ax[2,0].plot(Time_T_9,WorkRatio_T_9,'bo')
#ax[2,0].plot(Time_F_9,WorkRatio_F_9,'g--',linewidth=2.5)
#ax[2,0].plot(Time_F_9,WorkRatio_F_9,'go')

ax[2,1].plot(Time_N_12,WorkRatio_N_12,'r--',linewidth=2.5)
ax[2,1].plot(Time_N_12,WorkRatio_N_12,'ro')
ax[2,1].plot(Time_T_12,WorkRatio_T_12,'b--',linewidth=2.5)
ax[2,1].plot(Time_T_12,WorkRatio_T_12,'bo')
#ax[2,1].plot(Time_F_12,WorkRatio_F_12,'g--',linewidth=2.5)
#ax[2,1].plot(Time_F_12,WorkRatio_F_12,'go')

ax[2,2].plot(Time_N_15,WorkRatio_N_15,'r--',linewidth=2.5)
ax[2,2].plot(Time_N_15,WorkRatio_N_15,'ro')
ax[2,2].plot(Time_T_15,WorkRatio_T_15,'b--',linewidth=2.5)
ax[2,2].plot(Time_T_15,WorkRatio_T_15,'bo')
#ax[2,2].plot(Time_F_15,WorkRatio_F_15,'g--',linewidth=2.5)
#ax[2,2].plot(Time_F_15,WorkRatio_F_15,'go')


ax[0,0].legend(loc='upper right')

ax[0,0].set_yscale('log')
ax[0,1].set_yscale('log')
ax[0,2].set_yscale('log')

plt.plot()
plt.show()


