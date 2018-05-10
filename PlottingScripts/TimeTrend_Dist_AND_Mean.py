#This python script generates the work histogram time-trend analysis plot for the discrete control project
#
#Steven Large
#April 17th 2018

import os
import matplotlib.pyplot as plt
import seaborn as sns
from math import *
import numpy as np

Xm = 1
kL = 12
kR = 12
beta = 1
kTrap = 1.5

def GenerateThreePanel(Path="/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/NonEquilibrium_Local/WorkDistributions_FromCluster/",CPNum = 25,option=1):

	FilenameNaive_Base = "WorkDist_" + Param + "_Naive_CP" + str(CPNum) + "_T"
	FilenameTimeOpt_Base = "WorkDist_" + Param + "_TimeOpt_CP" + str(CPNum) + "_T"
	FilenameFullOpt_Base = "WorkDist_" + Param + "_FullOpt_CP" + str(CPNum) + "_T"



def GeneratePlot(Path="/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/NonEquilibrium_Local/WorkDistributions_FromCluster/",Param="12_15",CPNum = 25,option=1):

	FilenameNaive_Base = "WorkDist_" + Param + "_Naive_CP" + str(CPNum) + "_T"
	FilenameTimeOpt_Base = "WorkDist_" + Param + "_TimeOpt_CP" + str(CPNum) + "_T"
	FilenameFullOpt_Base = "WorkDist_" + Param + "_FullOpt_CP" + str(CPNum) + "_T"

	TimeRange = [50,600,1400,2200,3000]
	TimeRange_Full = [10,50,200,400,600,800,1000,1200,1400,1600,1800,2000,2200,2400,2600,2800,3000]

	WorkDist_Naive = []
	WorkDist_TimeOpt = []
	WorkDist_FullOpt = []

	WorkDist_Naive_Full = []
	WorkDist_TimeOpt_Full = []
	WorkDist_FullOpt_Full = []

	for index in range(len(TimeRange)):

		FilenameNaive = FilenameNaive_Base + str(TimeRange[index]) + ".dat"
		FilenameTimeOpt = FilenameTimeOpt_Base + str(TimeRange[index]) + ".dat"
		FilenameFullOpt = FilenameFullOpt_Base + str(TimeRange[index]) + ".dat"

		WorkDist_Naive.append(ReadWorkData(Path,FilenameNaive))
		WorkDist_TimeOpt.append(ReadWorkData(Path,FilenameTimeOpt))
		WorkDist_FullOpt.append(ReadWorkData(Path,FilenameFullOpt))

	for index in range(len(TimeRange_Full)):

		FilenameNaive = FilenameNaive_Base + str(TimeRange_Full[index]) + ".dat"
		FilenameTimeOpt = FilenameTimeOpt_Base + str(TimeRange_Full[index]) + ".dat"
		FilenameFullOpt = FilenameFullOpt_Base + str(TimeRange_Full[index]) + ".dat"

		WorkDist_Naive_Full.append(ReadWorkData(Path,FilenameNaive))
		WorkDist_TimeOpt_Full.append(ReadWorkData(Path,FilenameTimeOpt))
		WorkDist_FullOpt_Full.append(ReadWorkData(Path,FilenameFullOpt))

	if(option==1):
		TwoHistoPlot(TimeRange,TimeRange_Full,WorkDist_Naive,WorkDist_TimeOpt,WorkDist_Naive_Full,WorkDist_TimeOpt_Full,CPNum,"Naive","Time-Optimized")

	elif(option==2):
		TwoHistoPlot(TimeRange,TimeRange_Full,WorkDist_TimeOpt,WorkDist_FullOpt,WorkDist_Naive_Full,WorkDist_TimeOpt_Full,CPNum,"Time-Optimized","Fully-Optimized")

	elif(option==3):
		ThreeHistoPlot(TimeRange,TimeRange_Full,WorkDist_Naive,WorkDist_TimeOpt,WorkDist_FullOpt,WorkDist_Naive_Full,WorkDist_TimeOpt_Full,WorkDist_FullOpt_Full,CPNum)

	else:
		print "\n\n\t\t----- Option Flag not valid -----\n\n"


def ThreeHistoPlot(Time,TimeLong,Work1,Work2,Work3,Work1Long,Work2Long,Work3Long,CPNum):

	sns.set(style='darkgrid', palette='muted', color_codes=True)

	fig,axes = plt.subplots(4,1,figsize=(5,10))

	pal = sns.cubehelix_palette(2*len(Work1))
	for index in range(len(Work1)):
		handle = r'$\tau = $' + str(Time[index])
		sns.distplot(Work1[index], color=pal[index],ax=axes[0],label=handle)

	pal = sns.cubehelix_palette(2*len(Work2), start=0.25, rot=-0.25)
	for index in range(len(Work2)):
		handle = r'$\tau = $' + str(Time[index])
		sns.distplot(Work2[index], color=pal[index],ax=axes[1],label=handle)

	pal = sns.cubehelix_palette(2*len(Work3), start=-0.5, rot=-0.25)
	for index in range(len(Work3)):
		handle = r'$\tau = $' + str(Time[index])
		sns.distplot(Work3[index], color=pal[index],ax=axes[2],label=handle)

	axes[0].legend(loc='upper left')
	axes[1].legend(loc='upper left')
	axes[2].legend(loc='upper left')

	MeanWork1,StdErr1 = WorkAnalysis(Work1Long,CPNum)
	MeanWork2,StdErr2 = WorkAnalysis(Work2Long,CPNum)
	MeanWork3,StdErr3 = WorkAnalysis(Work3Long,CPNum)

	axes[3].plot(TimeLong,MeanWork1,'r--',linewidth=3.0,alpha=0.75)
	axes[3].plot(TimeLong,MeanWork2,'b--',linewidth=3.0,alpha=0.75)
	axes[3].plot(TimeLong,MeanWork3,'g--',linewidth=3.0,alpha=0.75)

	axes[3].errorbar(TimeLong,MeanWork1,yerr=StdErr1,fmt='ro',label="Naive")
	axes[3].errorbar(TimeLong,MeanWork2,yerr=StdErr2,fmt='bo',label="Time-Optimized")
	axes[3].errorbar(TimeLong,MeanWork3,yerr=StdErr3,fmt='go',label="Fully-Optimized")

	axes[3].set_yscale('log')
	axes[3].legend(loc='upper right')

	axes[2].set_xlabel(r'Average exess work $\langle\beta W_{\rm ex}\rangle$',fontsize=15)
	axes[2].set_ylabel(r'$P(W)$',fontsize=15)

	axes[3].set_xlabel(r'Protocol duration $\tau$', fontsize=15)
	axes[3].set_ylabel(r'$\frac{\langle W_{\rm ex}\rangle}{\langle W_{\rm ex}^{\infty}\rangle} - 1$',fontsize=15)

	plt.show()
	plt.close()


def TwoHistoPlot(Time,TimeLong,Work1,Work2,Work1Long,Work2Long,CPNum,Tag1,Tag2):

	sns.set(style='darkgrid', palette='muted', color_codes=True)

	fig,axes = plt.subplots(3,1,figsize=(5,7))

	pal = sns.cubehelix_palette(2*len(Work1))
	for index in range(len(Work1)):
		handle = r'$\tau = $' + str(Time[index])
		sns.distplot(Work1[index], color=pal[index], ax=axes[0],label=handle)

	pal = sns.cubehelix_palette(2*len(Work2), start=0.25,rot=-0.25)
	for index in range(len(Work2)):
		handle = r'$\tau = $' + str(Time[index])
		sns.distplot(Work2[index], color=pal[index], ax=axes[1],label=handle)

	axes[0].legend(loc='upper left')
	axes[1].legend(loc='upper left')

	MeanWork1,StdErr1 = WorkAnalysis(Work1Long,CPNum)
	MeanWork2,StdErr2 = WorkAnalysis(Work2Long,CPNum)

	axes[2].plot(TimeLong,MeanWork1,'r--',linewidth=3.0,alpha=0.75)
	axes[2].plot(TimeLong,MeanWork2,'b--',linewidth=3.0,alpha=0.75)

	axes[2].errorbar(TimeLong,MeanWork1,yerr=StdErr1,fmt='ro',label=Tag1)
	axes[2].errorbar(TimeLong,MeanWork2,yerr=StdErr2,fmt='bo',label=Tag2)

	axes[2].set_yscale('log')
	axes[2].legend(loc='upper right')

	axes[1].set_xlabel(r'Work $\beta W$',fontsize=15)
	axes[1].set_ylabel(r'$P(\beta W)$',fontsize=15)

	axes[2].set_xlabel(r'Protocol duration $\tau$',fontsize=15)
	axes[2].set_ylabel(r'$\frac{\langle W_{\rm ex}\rangle}{\langle W_{\rm ex}^{\rm\infty}\rangle} - 1$',fontsize=15)

	plt.show()
	plt.close()


def WorkAnalysis(WorkArray,CPNum):

	CorrectedWork = []
	CorrectedErr = []

	for index in range(len(WorkArray)):

		MeanWork = np.mean(WorkArray[index])
		StdDev = np.std(WorkArray[index])
		StdErr = 2*StdDev/float(sqrt(len(WorkArray[index])-1))

		InfiniteWork = CalculateInfiniteWork(CPNum)

		CorrectedWork.append((MeanWork/float(InfiniteWork)) - 1)
		CorrectedErr.append(StdErr/float(InfiniteWork))

	return CorrectedWork,CorrectedErr


def CalculateInfiniteWork(CPNum):

	CPInit = -1
	CPStep = 2/float(CPNum-1)

	CPVals = []

	CurrCP = CPInit

	for index in range(CPNum):
		CPVals.append(CurrCP)
		CurrCP += CPStep

	WorkAcc = 0

	for index in range(len(CPVals)-1):
		WorkAcc += WorkStep(CPVals[index],CPVals[index+1])

	return WorkAcc


def WorkStep(CP1,CP2):

	XMin = -5
	XMax = 5
	dX = 0.01

	XRange = []
	XCurr = XMin

	while XCurr <= XMax:
		XRange.append(XCurr)
		XCurr += dX

	Dist1 = Boltzmann(CP1,XRange)
	Dist2 = Boltzmann(CP2,XRange)

	Work = (1/float(beta))*RelativeEntropy(Dist1,Dist2,dX)

	return Work


def Boltzmann(CPVal,XRange):

	Prob = []
	NormFactor = 0

	dX = XRange[1] - XRange[0]

	for index in range(len(XRange)):

		Energy = TotalEnergy(CPVal,XRange[index])
		Prob.append(exp(-beta*Energy))
		NormFactor += exp(-beta*Energy)*dX

	for index in range(len(Prob)):
		Prob[index] = Prob[index]/float(NormFactor)

	return Prob


def RelativeEntropy(Dist1,Dist2,dX):

	RelativeEntropy = 0

	for index in range(len(Dist1)):
		RelativeEntropy += log(Dist1[index]/Dist2[index])*Dist1[index]*dX

	return RelativeEntropy


def TotalEnergy(CP, position):

	EnergyTrap = 0.5*kTrap*((position - CP)**2)
	EnergyBistable = -(1/float(beta))*log(exp(-beta*0.5*kL*((position + Xm)**2)) + exp(-beta*0.5*kR*((position - Xm)**2)))

	TotalEnergy = EnergyTrap + EnergyBistable

	return TotalEnergy


def ReadWorkData(Path,Filename):

	CompleteName = os.path.join(Path,Filename)

	file1 = open(CompleteName,'r')
	TempData = file1.readlines()
	file1.close()

	WorkArray = []

	for index in range(len(TempData)):
		WorkArray.append(eval(TempData[index]))

	return WorkArray



GeneratePlot(option=3)



