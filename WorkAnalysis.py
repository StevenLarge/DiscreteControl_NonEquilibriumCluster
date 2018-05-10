#This is the work analysis script for the Discrete protocol simulations
#
#Steven Large
#April 6th 2018

import os
import numpy as np
from math import *
import matplotlib.pyplot as plt
import seaborn as sns

from mpl_toolkits.axes_grid.inset_locator import inset_axes

kTrap = 1.5
kL = 12
kR = 12
Xm = 1
beta = 1

def ReadWorkDist(Path,Filename):

	CompleteName = os.path.join(Path,Filename)

	file1 = open(CompleteName,'r')
	TempData = file1.readlines()
	file1.close()

	WorkArray = []

	for index in range(len(TempData)):
		WorkArray.append(eval(TempData[index]))

	return WorkArray


def WorkHistogram(WorkArray):

	sns.set(style="darkgrid",palette="muted",color_codes=True)

	sns.distplot(WorkArray)
	
	plt.show()
	plt.close()


def EqDist(CPVal,XVals):

	Prob = []
	Partition = 0
	dX = XVals[1] - XVals[0]

	for index in range(len(XVals)):

		Energy = TotalEnergy(CPVal,XVals[index])
		Boltzmann = exp(-beta*Energy)
		Prob.append(Boltzmann)
		Partition = Partition + Boltzmann*dX

	for index in range(len(Prob)):

		Prob[index] = Prob[index]/float(Partition)

	return Prob


def KL_Divergence(Prob1,Prob2,dX):

	KL_Div = 0

	for index in range(len(Prob1)):

		KL_Div = KL_Div + Prob1[index]*log(Prob1[index]/Prob2[index])*dX

	return KL_Div


def TotalEnergy(CPVal,position):

	TrapEnergy = 0.5*float(kTrap)*(position - CPVal)*(position - CPVal)
	BistableEnergy = -(1/float(beta))*log(exp(-beta*0.5*float(kL)*(position + Xm)*(position + Xm)) + exp(-beta*0.5*float(kR)*(position - Xm)*(position - Xm)))

	TotalEnergy = TrapEnergy + BistableEnergy

	return TotalEnergy


def InfiniteWork(CPVals,XRange):

	dX = XRange[1] - XRange[0]

	ProtocolWork = 0

	for index in range(len(CPVals)-1):

		Prob1 = EqDist(CPVals[index],XRange)
		Prob2 = EqDist(CPVals[index+1],XRange)

		WorkStep = KL_Divergence(Prob1,Prob2,dX)

		ProtocolWork = ProtocolWork + WorkStep

	return ProtocolWork


def GenerateProtocol(NumCPVals):

	CPVals = []

	TotalDist = 2

	StepSize = float(TotalDist)/float(NumCPVals-1)

	CurrentCP = -1

	for index in range(NumCPVals):
		CPVals.append(CurrentCP)
		CurrentCP = CurrentCP + StepSize

	return CPVals	


def AnalyzeWorkTime(WorkArray):

	XRange = []

	XCurr = -5
	XMax = 5
	XDiff = 0.01

	while XCurr <= XMax:
		XRange.append(XCurr)
		XCurr += XDiff

	CPVals = GenerateProtocol(25)

	AsympWork = InfiniteWork(CPVals,XRange)

	Mean = np.mean(WorkArray)
	StdDev = np.std(WorkArray)

	StdErr = 2*StdDev/sqrt(len(WorkArray))

	CorrectedMean = (float(Mean)/float(AsympWork)) - 1
	CorrectedStdErr = float(StdErr)/float(AsympWork)

	return CorrectedMean, CorrectedStdErr


def AnalyzeWorkSpace(WorkArray):

	XRange = []

	XCurr = -5
	XMax = 5
	XDiff = 0.01

	while XCurr <= XMax:
		XRange.append(XCurr)
		XCurr += XDiff

	CPVals = [-1,1]

	InstantWork = InfiniteWork(CPVals,XRange)

	Mean = np.mean(WorkArray)
	StdDev = np.std(WorkArray)

	StdErr = 2*StdDev/sqrt(len(WorkArray))

	CorrectedMean = float(Mean)/float(InstantWork)
	CorrectedStdErr = float(StdErr)/float(InstantWork)

	return CorrectedMean, CorrectedStdErr


def AnalyzeWorkFull(WorkArray):
	
	XRange = []

	XCurr = -5
	XMax = 5
	XDiff = 0.01

	while XCurr <= XMax:
		XRange.append(XCurr)
		XCurr += XDiff

	CPVals = [-1,1]

	InstantWork = InfiniteWork(CPVals,XRange)

	Mean = np.mean(WorkArray)
	StdDev = np.std(WorkArray)

	StdErr = 2*StdDev/sqrt(len(WorkArray))

	CorrectedMean = float(Mean)/float(InstantWork)
	CorrectedStdErr = float(StdErr)/float(InstantWork)

	return CorrectedMean, CorrectedStdErr


def WorkPlotting_Trend(WorkArrayNaive_Time,WorkArrayTimeOpt_Time,WorkArrayFullOpt_Time,TimeArray,TimeArray_Full,WorkArrayNaive_Space,WorkArraySpaceOpt_Space,CPArray):#WorkArrayFullOpt_Space,CPArray):

	sns.set(style="darkgrid",palette="muted",color_codes=True)

	fig,axes = plt.subplots(1,2)

	MeanWorkNaive_Time = []
	MeanWorkTimeOpt_Time = []
	MeanWorkFullOpt_Time = []
	StdErr_Naive_Time = []
	StdErr_TimeOpt_Time = []
	StdErr_FullOpt_Time = []

	for index in range(len(WorkArrayNaive_Time)):
		MeanWorkNaive_Time.append([])
		StdErr_Naive_Time.append([])
		MeanWorkNaive_Time[index],StdErr_Naive_Time[index] = AnalyzeWorkTime(WorkArrayNaive_Time[index])
	
	for index in range(len(WorkArrayTimeOpt_Time)):
		MeanWorkTimeOpt_Time.append([])
		StdErr_TimeOpt_Time.append([])
		MeanWorkTimeOpt_Time[index],StdErr_TimeOpt_Time[index] = AnalyzeWorkTime(WorkArrayTimeOpt_Time[index])

	for index in range(len(WorkArrayFullOpt_Time)):
		MeanWorkFullOpt_Time.append([])
		StdErr_FullOpt_Time.append([])
		MeanWorkFullOpt_Time[index],StdErr_FullOpt_Time[index] = AnalyzeWorkTime(WorkArrayFullOpt_Time[index])

	MeanDiff_Time = []
	EmanDiff_TimeFull = []
	StdErr_Diff_Time = []
	StdErr_Diff_TimeFull = []

	for index in range(len(MeanWorkNaive_Time)):
		MeanDiff_Time.append((MeanWorkTimeOpt_Time[index]/MeanWorkNaive_Time[index]))
		StdErr_Diff_Time.append((MeanWorkTimeOpt_Time[index]/MeanWorkNaive_Time[index])*((StdErr_Naive_Time[index]/sqrt(MeanWorkNaive_Time[index])) + (StdErr_TimeOpt_Time[index])/sqrt(MeanWorkTimeOpt_Time[index])))

	for index in range(len(MeanWorkNaive_Time)):
		MeanDiff_Full.append(MeanWorkFullOpt_Time[index]/MeanWorkNaive_Time[index])
		StdErr_Diff_Full.append((MeanWorkFullOpt_Time[index]/MeanWorkNaive_Time[index])*((StdErr_Naive_Time[index]/sqrt(MeanWorkNaive_Time[index])) + (StdErr_FullOpt_Time[index])/sqrt(MeanWorkFullOpt_Time[index])))


	MeanWorkNaive_Space = []
	MeanWorkSpaceOpt_Space = []
	MeanWorkFullOpt_Space = []
	StdErr_Naive_Space = []
	StdErr_SpaceOpt_Space = []
	StdErr_FullOpt_Space = []

	for index in range(len(WorkArrayNaive_Space)):
		#MeanWorkNaive_Space.append([])
		#StdErr_Naive_Space.append([])
		#MeanWorkNaive_Space[index],StdErr_Naive_Space[index] = AnalyzeWorkTime(WorkArrayNaive_Space[index])
	
	for index in range(len(WorkArrayTimeOpt_Space)):
		MeanWorkSpaceOpt_Space.append([])
		StdErr_SpaceOpt_Space.append([])
		MeanWorkSpaceOpt_Space[index],StdErr_SpaceOpt_Space[index] = AnalyzeWorkTime(WorkArraySpaceOpt_Space[index])

	#for index in range(len(WorkArrayFullOpt_Space)):
		#MeanWorkFullOpt_Space.append([])
		#StdErr_FullOpt_Space.append([])
		#MeanWorkFullOpt_Space[index],StdErr_FullOpt_Space[index] = AnalyzeWorkTime(WorkArrayFullOpt_Space[index])

	MeanDiff_Space = []
	MeanDiff_SpaceFull
	StdErr_Diff_Space = []
	StdErr_Diff_SpaceFull = []

	for index in range(len(MeanWorkNaive_Space)):
		MeanDiff_Space.append((MeanWorkSpaceOpt_Space[index]/MeanWorkNaive_Space[index]))
		StdErr_Diff_Space.append((MeanWorkSpaceOpt_Space[index]/MeanWorkNaive_Space[index])*((StdErr_Naive_Space[index]/sqrt(MeanWorkNaive_Space[index])) + (StdErr_SpaceOpt_Space[index])/sqrt(MeanWorkSpaceOpt_Space[index])))

	#for index in range(len(MeanWorkNaive_Time)):
		#MeanDiff_SpaceFull.append(MeanWorkFullOpt_Space[index]/MeanWorkNaive_Space[index])
		#StdErr_Diff_SpaceFull.append((MeanWorkFullOpt_Space[index]/MeanWorkNaive_Space[index])*((StdErr_Naive_Space[index]/sqrt(MeanWorkNaive_Space[index])) + (StdErr_FullOpt_Space[index])/sqrt(MeanWorkFullOpt_Space[index])))


	axes[0].plot(TimeArray_Full,MeanDiff_Time,'b--',linewidth=3.0,alpha=0.5)
	axes[0].errorbar(TimeArray_Full,MeanDiff_Time,yerr=StdErr_Diff_Time,fmt='bo',label="Time Optimized")
	axes[0].plot(TimeArray_Full,MeanDiff_Full,'m--',linewidth=3.0,alpha=0.5)
	axes[0].errorbar(TimeArray_Full,MeanDiff_Full,yerr=StdErr_Diff_Full,fmt='mo',label="Fully Optimized")

	axes[1].plot(CPArray,MeanDiff_Space,'g--',linewidth=3.0,alpha=0.5)
	axes[1].errorbar(CPArray,MeanDiff_Space,yerr=StdErr_Diff_Space,fmt='go',label="Space Optimized")
	#axes[1].plot(CPArray,MeanDiff_SpaceFull,'m--',linewidth=3.0,alpha=0.5)
	#axes[1].errorbar(CPArray,MeanDiff_SpaceFull,yerr=StdErr_Diff_SpaceFull,fmt='mo',label="Fully Optimized")

	axes[0].set_xlabel(r'Protocol duration $\tau$',fontsize=15)
	axes[0].set_ylabel(r'$\frac{\langle W_{\rm ex}^{\rm neq}\rangle_{\rm opt}}{\langle W_{\rm ex}^{\rm neq}\rangle_{\rm naive}}$',fontsize=15)

	axes[1].set_xlabel(r'Number of $\lambda$ values',fontsize=15)
	axes[1].set_ylabel(r'$\frac{\langle W_{\rm ex}\rangle}{\langle W_{\rm ex}\rangle_{\lambda_{\rm i}\rightarrow\lambda_{\rm f}}}$',fontsize=15)

	plt.show()
	plt.close()


def WorkHistogram_TimeSeries(WorkArrayNaive,WorkArrayTime,TimeArray,WorkArrayNaive_Full,WorkArrayTime_Full,TimeArray_Full):

	sns.set(style="darkgrid",palette="muted",color_codes=True)

	fig,axes = plt.subplots(3,1)

	#pal = sns.light_palette("Red",len(WorkArrayNaive))
	pal = sns.cubehelix_palette(2*len(WorkArrayNaive))
	#pal = sns.color_palette("Reds")
	for index in range(len(WorkArrayNaive)):
		handle = r'$\tau =$ ' + str(TimeArray[index])
		sns.distplot(WorkArrayNaive[index],color=pal[index],ax=axes[0],label=handle)

	#pal = sns.light_palette("Blue",len(WorkArrayTime))
	#pal = sns.cubehelix_palette(2*len(WorkArrayTime), start=0.5,rot=-0.75)
	#pal = sns.color_palette("Blues")
	pal = sns.cubehelix_palette(2*len(WorkArrayTime), start=0.25,rot=-0.25)
	for index in range(len(WorkArrayTime)):
		handle = r'$\tau =$ ' + str(TimeArray[index])
		sns.distplot(WorkArrayTime[index],color=pal[index],ax=axes[1],label=handle)

	axes[0].legend(loc='upper left')
	axes[1].legend(loc='upper left')

	axes[1].set_xlabel(r"Protocol work $\langle W\rangle_{\Lambda}$",fontsize=14)
	axes[1].set_ylabel(r"$P(W)$",fontsize=14)

	MeanWork_Naive = []
	MeanWork_Time = []
	StdErr_Naive = []
	StdErr_Time = []

	for index in range(len(WorkArrayNaive_Full)):
		MeanWork_Naive.append([])
		StdErr_Naive.append([])
		MeanWork_Naive[index],StdErr_Naive[index] = AnalyzeWorkTime(WorkArrayNaive_Full[index])
	
	for index in range(len(WorkArrayTime_Full)):
		MeanWork_Time.append([])
		StdErr_Time.append([])
		MeanWork_Time[index],StdErr_Time[index] = AnalyzeWorkTime(WorkArrayTime_Full[index])

	MeanDiff = []
	StdErr_Diff = []

	for index in range(len(MeanWork_Naive)):
		MeanDiff.append((MeanWork_Time[index]/MeanWork_Naive[index]))
		StdErr_Diff.append((MeanWork_Time[index]/MeanWork_Naive[index])*((StdErr_Naive[index]/sqrt(MeanWork_Naive[index])) + (StdErr_Time[index])/sqrt(MeanWork_Time[index])))
		#StdErr_Diff.append((StdErr_Naive[index] + StdErr_Time[index]))
		#MeanDiff.append((MeanWork_Naive[index]-MeanWork_Time[index])/float(0.5*(MeanWork_Naive[index]+MeanWork_Time[index])))
		#StdErr_Diff.append(0.5*(StdErr_Naive[index] + StdErr_Time[index])/float(0.5*(MeanWork_Naive[index]+MeanWork_Time[index])))

	axes[2].plot(TimeArray_Full,MeanDiff,'k--',linewidth=3.0,alpha=0.5)
	axes[2].errorbar(TimeArray_Full,MeanDiff,yerr=StdErr_Diff,fmt='ko',label="Work Difference")

	axes[2].set_yscale('log')
	axes[2].set_xlabel(r'Protocol Duration $\tau$',fontsize=14)
	axes[2].set_ylabel(r'$\frac{\langle W_{\rm ex}^{\rm N}\rangle_{\rm N}}{\langle W_{\rm ex}^{\rm T}\rangle}$',fontsize=14)

	axes[2].legend(loc='upper right')

	#axes[2].plot(TimeArray_Full,MeanWork_Naive,'r--',linewidth=2.0,alpha=0.5)
	#axes[2].plot(TimeArray_Full,MeanWork_Time,'b--',linewidth=2.0,alpha=0.5)

	#axes[2].errorbar(TimeArray_Full,MeanWork_Naive,yerr=StdErr_Naive,fmt="ro",label="Naive")
	#axes[2].errorbar(TimeArray_Full,MeanWork_Time,yerr=StdErr_Time,fmt="bo",label="Time-Optimized")

	#axes[2].set_yscale('log')
	#axes[2].set_xlabel(r'Protocol Duration, $\tau$')
	#axes[2].set_ylabel(r'$\frac{\langle W\rangle_{\Lambda}}{\langle W\rangle_{\Lambda}^{\infty}} - 1$')
	#axes[2].legend(loc='upper right')

	plt.show()
	plt.close()


def WorkHistogram_SpaceSeries(WorkArrayNaive,WorkArraySpace,CPArray):

	sns.set(style="darkgrid",palette="muted",color_codes=True)

	fig,axes = plt.subplots(3,1)

	pal = sns.cubehelix_palette(2*len(WorkArrayNaive))
	for index in range(len(WorkArrayNaive)):
		sns.distplot(WorkArrayNaive[index],color=pal[index],ax=axes[0])


	pal = sns.cubehelix_palette(2*len(WorkArraySpace), start=0.25,rot=-0.25)
	for index in range(len(WorkArraySpace)):
		sns.distplot(WorkArraySpace[index],color=pal[index],ax=axes[1])

	MeanWork_Naive = []
	MeanWork_Space = []
	StdErr_Naive = []
	StdErr_Space = []

	for index in range(len(WorkArrayNaive)):
		MeanWork_Naive.append([])
		StdErr_Naive.append([])
		MeanWork_Naive[index],StdErr_Naive[index] = AnalyzeWorkSpace(WorkArrayNaive[index])
	
	for index in range(len(WorkArraySpace)):
		MeanWork_Space.append([])
		StdErr_Space.append([])
		MeanWork_Space[index],StdErr_Space[index] = AnalyzeWorkSpace(WorkArraySpace[index])

	axes[2].plot(CPArray,MeanWork_Naive,'r--',linewidth=2.0,alpha=0.5)
	axes[2].plot(CPArray,MeanWork_Space,'b--',linewidth=2.0,alpha=0.5)

	axes[2].errorbar(CPArray,MeanWork_Naive,yerr=StdErr_Naive,fmt="ro")
	axes[2].errorbar(CPArray,MeanWork_Space,yerr=StdErr_Space,fmt="bo")

	axes[2].set_yscale('log')
	axes[2].set_xscale('log')

	#Inset = inset_axes(axes[2],width="30%",height="40%",loc=1)

	MeanDiff = []
	StdErr_Diff = []

	for index in range(len(MeanWork_Naive)):
		MeanDiff.append((MeanWork_Naive[index]-MeanWork_Space[index])/float(0.5*(MeanWork_Naive[index]+MeanWork_Space[index])))
		StdErr_Diff.append(0.5*(StdErr_Naive[index] + StdErr_Space[index])/float(0.5*(MeanWork_Naive[index]+MeanWork_Space[index])))

	#Inset.plot(CPArray,MeanDiff,'k--',linewidth=1.5,alpha=0.5)
	#Inset.errorbar(CPArray,MeanDiff,yerr=StdErr_Diff,fmt='ko')

	#Inset.set_yscale('log')
	#Inset.set_xscale('log')

	plt.show()
	plt.close()


def WorkHistogram_SpaceSeries2(WorkArraySpace,CPArray):

	sns.set(style="darkgrid",palette="muted",color_codes=True)

	fig,axes = plt.subplots(2,1)

	pal = sns.cubehelix_palette(2*len(WorkArraySpace), start=0.25,rot=-0.25)
	for index in range(len(WorkArraySpace)):
		sns.distplot(WorkArraySpace[index],color=pal[index],ax=axes[0])

	MeanWork_Space = []
	StdErr_Space = []

	for index in range(len(WorkArraySpace)):
		MeanWork_Space.append([])
		StdErr_Space.append([])
		MeanWork_Space[index],StdErr_Space[index] = AnalyzeWorkSpace(WorkArraySpace[index])

	axes[1].plot(CPArray,MeanWork_Space,'b--',linewidth=2.0,alpha=0.5)

	axes[1].errorbar(CPArray,MeanWork_Space,yerr=StdErr_Space,fmt="bo")

	axes[1].set_yscale('log')
	axes[1].set_xscale('log')

	plt.show()
	plt.close()


def WorkHistogram_FullOpt(WorkArrayNaive,WorkArrayFull,TimeArray,WorkArrayNaive_Full,WorkArrayFull_Full,TimeArray_Full):

	sns.set(style="darkgrid",palette="muted",color_codes=True)

	fig,axes = plt.subplots(3,1)

	pal = sns.cubehelix_palette(2*len(WorkArrayNaive))
	for index in range(len(WorkArrayNaive)):
		handle = r'$\tau =$ ' + str(TimeArray[index])
		sns.distplot(WorkArrayNaive[index],color=pal[index],ax=axes[0],label=handle)

	pal = sns.cubehelix_palette(2*len(WorkArrayFull), start=0.25,rot=-0.25)
	for index in range(len(WorkArrayFull)):
		handle = r'$\tau =$ ' + str(TimeArray[index])
		sns.distplot(WorkArrayFull[index],color=pal[index],ax=axes[1],label=handle)

	axes[0].legend(loc='upper left')
	axes[1].legend(loc='upper left')

	axes[1].set_xlabel(r"Protocol work $\langle W\rangle_{\Lambda}$")
	axes[1].set_ylabel(r"$P(W)$")

	MeanWork_Naive = []
	MeanWork_Full = []
	StdErr_Naive = []
	StdErr_Full = []

	for index in range(len(WorkArrayNaive_Full)):
		MeanWork_Naive.append([])
		StdErr_Naive.append([])
		MeanWork_Naive[index],StdErr_Naive[index] = AnalyzeWorkFull(WorkArrayNaive_Full[index])
	
	for index in range(len(WorkArrayFull_Full)):
		MeanWork_Full.append([])
		StdErr_Full.append([])
		MeanWork_Full[index],StdErr_Full[index] = AnalyzeWorkFull(WorkArrayFull_Full[index])

	axes[2].plot(TimeArray_Full,MeanWork_Naive,'r--',linewidth=2.0,alpha=0.5)
	axes[2].plot(TimeArray_Full,MeanWork_Full,'b--',linewidth=2.0,alpha=0.5)

	axes[2].errorbar(TimeArray_Full,MeanWork_Naive,yerr=StdErr_Naive,fmt="ro",label="Naive")
	axes[2].errorbar(TimeArray_Full,MeanWork_Full,yerr=StdErr_Full,fmt="bo",label="Fully-Optimized")

	axes[2].set_yscale('log')
	axes[2].set_xlabel(r'Protocol Duration, $\tau$')
	axes[2].set_ylabel(r'$\frac{\langle W\rangle_{\Lambda}}{\langle W\rangle_{\lambda_0\rightarrow\lambda_N}}$')
	axes[2].legend(loc='upper right')

	#Inset = axes[2].add_axes([0.75,0.5,0.2,0.4])
	#Inset = inset_axes(axes[2],width="30%",height="40%",loc=1)

	#MeanDiff = []
	#StdErr_Diff = []

	#for index in range(len(MeanWork_Naive)):
	#	MeanDiff.append((MeanWork_Naive[index]-MeanWork_Time[index])/float(0.5*(MeanWork_Naive[index]+MeanWork_Time[index])))
	#	StdErr_Diff.append(0.5*(StdErr_Naive[index] + StdErr_Time[index])/float(0.5*(MeanWork_Naive[index]+MeanWork_Time[index])))

	#for index in range(len(MeanWork_Naive)):
		#MeanDiff.append(MeanWork_Naive[index]/MeanWork_Time[index])

	#Inset.plot(TimeArray,MeanDiff,fmt='ko')
	#Inset.errorbar(TimeArray,MeanDiff,yerr=StdErr_Diff,fmt='ko')

	plt.show()
	plt.close()


def PlotWorkHistograms_Time(ReadPath,FilenameNaive_Base,FilenameTimeOpt_Base,FilenameFullOpt_Base):

	WorkDist_Naive = []
	WorkDist_Time = []
	WorkDist_Full = []

	WorkDist_Naive_Long = []
	WorkDist_Time_Long = []
	WorkDist_Full_Long = []

	TimeRange = [50,600,1400,2200,3000]
	TimeRange_Full = [10,50,200,400,600,800,1000,1200,1400,1600,1800,2000,2200,2400,2600,2800,3000]	

	for index in range(len(TimeRange)):

		FilenameNaive = FilenameNaive_Base + str(TimeRange[index]) + ".dat"
		FilenameTime = FilenameTime_Base + str(TimeRange[index]) + ".dat"
		FilenameFull = FilenameFull_Base + str(TimeRange[index]) + ".dat"

		WorkDist_Naive.append(ReadWorkDist(Path,FilenameNaive))
		WorkDist_Time.append(ReadWorkDist(Path,FilenameTime))
		WorkDist_Full.append(ReadWorkDist(Path,FilenameFull))

	for index in range(len(TimeRange_Full)):

		FilenameNaive = FilenameNaive_Base + str(TimeRange_Full[index]) + ".dat"
		FilenameTime = FilenameTime_Base + str(TimeRange_Full[index]) + ".dat"
		FilenameFull = FilenameFull_Base + str(TimeRange_Full[index]) + ".dat"

		WorkDist_Naive_Long.append(ReadWorkDist(Path,FilenameNaive))
		WorkDist_Time_Long.append(ReadWorkDist(Path,FilenameTime))
		WorkDist_Full_Long.append(ReadWorkDist(Path,FilenameFull))

	sns.set(style="darkgrid",palette="muted",color_codes=True)

	fig, axes = plt.subplots(1,4)

	pal = sns.cubehelix_palette(2*len(WorkDist_Naive))
	for index in range(len(WorkDist_Naive)):
		handle = r'$\tau =$ ' + str(TimeRange[index])
		sns.distplot(WorkDist_Naive[index],color=pal[index],ax=axes[0],label=handle)

	pal = sns.cubehelix_palette(2*len(WorkDist_Time), start=0.25,rot=-0.25)
	for index in range(len(WorkDist_Time)):
		handle = r'$\tau =$ ' + str(TimeRange[index])
		sns.distplot(WorkDist_Time[index],color=pal[index],ax=axes[1],label=handle)

	pal = sns.cubehelix_palette(2*len(WorkDist_Full), start=-0.25,rot=-0.25)
	for index in range(len(WorkDist_Full)):
		handle = r'$\tau =$ ' + str(TimeRange[index])
		sns.distplot(WorkDist_Full[index],color=pal[index],ax=axes[2],label=handle)






Path = "WorkDistributions_FromCluster/"

FilenameNaive_Base = "WorkDist_12_15_Naive_CP25_T"
FilenameTime_Base = "WorkDist_12_15_TimeOpt_CP25_T"
FilenameFull_Base = "WorkDist_12_15_FullOpt_CP25_T"

FilenameSpace_Base = "WorkDist_12_15_SpaceOpt_CP"
FilenameNaiveSpace_Base = "WorkDist_12_15_Naive_CP"
#FilenameFull_Base = "WorkDist_3_12_15_FullOpt_CP"

TimeRange = [50,600,1400,2200,3000]
TimeRange_Full = [10,50,200,400,600,800,1000,1200,1400,1600,1800,2000,2200,2400,2600,2800,3000]
PlotSize = len(TimeRange)

CPRange = [4,8,16,32,64,128,256,512]

WorkDist_Naive = []
WorkDist_Time = []
WorkDist_Full = []

WorkDist_Naive_Full = []
WorkDist_Time_Full = []
WorkDist_Full_Full = []

for index in range(PlotSize):

	FilenameNaive = FilenameNaive_Base + str(TimeRange[index]) + ".dat"
	FilenameTime = FilenameTime_Base + str(TimeRange[index]) + ".dat"

	WorkDist_Naive.append(ReadWorkDist(Path,FilenameNaive))
	WorkDist_Time.append(ReadWorkDist(Path,FilenameTime))

for index in range(len(TimeRange_Full)):

	FilenameNaive = FilenameNaive_Base + str(TimeRange_Full[index]) + ".dat"
	FilenameTime = FilenameTime_Base + str(TimeRange_Full[index]) + ".dat"
	FilenameFull = FilenameFull_Base + str(TimeRange_Full[index]) + ".dat"

	WorkDist_Naive_Full.append(ReadWorkDist(Path,FilenameNaive))
	WorkDist_Time_Full.append(ReadWorkDist(Path,FilenameTime))
	WorkDist_Full_Full.append(ReadWorkDist(Path,FilenameFull))

#WorkHistogram_TimeSeries(WorkDist_Naive,WorkDist_Time,TimeRange,WorkDist_Naive_Full,WorkDist_Time_Full,TimeRange_Full)


#for index in range(PlotSize):

	#FilenameFull = FilenameFull_Base + str(TimeRange[index]) + ".dat"

	#WorkDist_Full.append(ReadWorkDist(Path,FilenameFull))

#for index in range(len(TimeRange_Full)):

	#FilenameFull= FilenameFull_Base + str(TimeRange_Full[index]) + ".dat"

	#WorkDist_Full_Full.append(ReadWorkDist(Path,FilenameFull))

#WorkHistogram_FullOpt(WorkDist_Naive,WorkDist_Full,TimeRange,WorkDist_Naive_Full,WorkDist_Full_Full,TimeRange_Full)


WorkDist_SpaceNaive = []
WorkDist_Space = []

for index in range(len(CPRange)):

	FilenameNaive = FilenameNaiveSpace_Base + str(CPRange[index]) + "_T2000.dat"
	FilenameSpace = FilenameSpace_Base + str(CPRange[index]) + "_T2000.dat"

	#WorkDist_SpaceNaive.append(ReadWorkDist(Path,FilenameNaive))
	WorkDist_Space.append(ReadWorkDist(Path,FilenameSpace))

#WorkHistogram_SpaceSeries2(WorkDist_Space,CPRange)

WorkPlotting_Trend(WorkDist_Naive_Full,WorkDist_Time_Full,WorkDist_Full_Full,TimeRange,TimeRange_Full,WorkDist_SpaceNaive,WorkDist_Space,CPRange)



