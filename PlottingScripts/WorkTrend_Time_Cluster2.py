#This generates the panel plot of time trend work distributions for different bistable parameters
#
#Steven Large
#April 30th 2018

import os
import numpy as np
from math import *
import matplotlib.pyplot as plt
import seaborn as sns

def PlotPanels():
	
	Times = [10,50,200,400,600,800,1000,1200,1400,1600,1800,2000,2200,2400,2600,2800,3000]
	Times_Small = [50,600,1400,2200,3000]

	Filename_N_9_Base = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/NonEquilibrium_Local/WorkDistributions_FromCluster2/WorkDist_N_9_15_T"
	Filename_N_12_Base = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/NonEquilibrium_Local/WorkDistributions_FromCluster2/WorkDist_N_12_15_T"
	Filename_N_15_Base = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/NonEquilibrium_Local/WorkDistributions_FromCluster2/WorkDist_N_15_15_T"

	Filename_T_9_Base = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/NonEquilibrium_Local/WorkDistributions_FromCluster2/WorkDist_T_9_15_T"
	Filename_T_12_Base = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/NonEquilibrium_Local/WorkDistributions_FromCluster2/WorkDist_T_12_15_T"
	Filename_T_15_Base = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/NonEquilibrium_Local/WorkDistributions_FromCluster2/WorkDist_T_15_15_T"

	Filename_F_9_Base = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/NonEquilibrium_Local/WorkDistributions_FromCluster2/WorkDist_F_9_15_T"
	Filename_F_12_Base = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/NonEquilibrium_Local/WorkDistributions_FromCluster2/WorkDist_F_12_15_T"
	Filename_F_15_Base = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/NonEquilibrium_Local/WorkDistributions_FromCluster2/WorkDist_F_15_15_T"

	WorkArray_N_9 = []
	WorkArray_N_12 = []	
	WorkArray_N_15 = []

	WorkArray_T_9 = []
	WorkArray_T_12 = []
	WorkArray_T_15 = []

	WorkArray_F_9 = []
	WorkArray_F_12 = []
	WorkArray_F_15 = []

	MeanWork_N_9 = []
	MeanWork_N_12 = []
	MeanWork_N_15 = []

	MeanWork_T_9 = []
	MeanWork_T_12 = []
	MeanWork_T_15 = []

	MeanWork_F_9 = []
	MeanWork_F_12 = []
	MeanWork_F_15 = []

	WorkErr_N_9 = []
	WorkErr_N_12 = []
	WorkErr_N_15 = []

	WorkErr_T_9 = []
	WorkErr_T_12 = []
	WorkErr_T_15 = []

	WorkErr_F_9 = []
	WorkErr_F_12 = []
	WorkErr_F_15 = []


	for index in range(len(Times)):
		Filename_N_9 = Filename_N_9_Base + str(Times[index]) + "_Master.dat"
		Filename_N_12 = Filename_N_12_Base + str(Times[index]) + "_Master.dat"
		Filename_N_15 = Filename_N_15_Base + str(Times[index]) + "_Master.dat"

		Filename_T_9 = Filename_T_9_Base + str(Times[index]) + "_Master.dat"
		Filename_T_12 = Filename_T_12_Base + str(Times[index]) + "_Master.dat"
		Filename_T_15 = Filename_T_15_Base + str(Times[index]) + "_Master.dat"

		Filename_F_9 = Filename_F_9_Base + str(Times[index]) + "_Master.dat"
		Filename_F_12 = Filename_F_12_Base + str(Times[index]) + "_Master.dat"
		Filename_F_15 = Filename_F_15_Base + str(Times[index]) + "_Master.dat"

		WorkArray_N_9.append(ReadData(Filename_N_9))
		WorkArray_N_12.append(ReadData(Filename_N_12))
		WorkArray_N_15.append(ReadData(Filename_N_15))

		WorkArray_T_9.append(ReadData(Filename_T_9))
		WorkArray_T_12.append(ReadData(Filename_T_12))
		WorkArray_T_15.append(ReadData(Filename_T_15))

		WorkArray_F_9.append(ReadData(Filename_F_9))
		WorkArray_F_12.append(ReadData(Filename_F_12))
		WorkArray_F_15.append(ReadData(Filename_F_15))

		MeanWork,MeanErr = WorkAnalysis(WorkArray_N_9[index],9)
		MeanWork_N_9.append(MeanWork)
		WorkErr_N_9.append(MeanErr)
		MeanWork,MeanErr = WorkAnalysis(WorkArray_N_12[index],12)
		MeanWork_N_12.append(MeanWork)
		WorkErr_N_12.append(MeanErr)
		MeanWork,MeanErr = WorkAnalysis(WorkArray_N_15[index],15)
		MeanWork_N_15.append(MeanWork)
		WorkErr_N_15.append(MeanErr)

		MeanWork,MeanErr = WorkAnalysis(WorkArray_T_9[index],9)
		MeanWork_T_9.append(MeanWork)
		WorkErr_T_9.append(MeanErr)
		MeanWork,MeanErr = WorkAnalysis(WorkArray_T_12[index],12)
		MeanWork_T_12.append(MeanWork)
		WorkErr_T_12.append(MeanErr)
		MeanWork,MeanErr = WorkAnalysis(WorkArray_T_15[index],15)
		MeanWork_T_15.append(MeanWork)
		WorkErr_T_15.append(MeanErr)

		MeanWork,MeanErr = WorkAnalysis(WorkArray_F_9[index],9)
		MeanWork_F_9.append(MeanWork)
		WorkErr_F_9.append(MeanErr)
		MeanWork,MeanErr = WorkAnalysis(WorkArray_F_12[index],12)
		MeanWork_F_12.append(MeanWork)
		WorkErr_F_12.append(MeanErr)
		MeanWork,MeanErr = WorkAnalysis(WorkArray_F_15[index],15)
		MeanWork_F_15.append(MeanWork)
		WorkErr_F_15.append(MeanErr)

	NaiveWriteName_9 = "MeanWorkTrend_N_Time_9.dat"
	NaiveWriteName_12 = "MeanWorkTrend_N_Time_12.dat"
	NaiveWriteName_15 = "MeanWorkTrend_N_Time_15.dat"

	TimeOptWriteName_9 = "MeanWorkTrend_T_Time_9.dat"
	TimeOptWriteName_12 = "MeanWorkTrend_T_Time_12.dat"
	TimeOptWriteName_15 = "MeanWorkTrend_T_Time_15.dat"

	FullOptWriteName_9 = "MeanWorkTrend_F_Time_9.dat"
	FullOptWriteName_12 = "MeanWorkTrend_F_Time_12.dat"
	FullOptWriteName_15 = "MeanWorkTrend_F_Time_15.dat"

	WritePath = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/NonEquilibrium_Local/WorkAnalysisFiles/"

	WriteWorkTrend(WritePath,NaiveWriteName_9,MeanWork_N_9,WorkErr_N_9,Times)
	WriteWorkTrend(WritePath,NaiveWriteName_12,MeanWork_N_12,WorkErr_N_12,Times)
	WriteWorkTrend(WritePath,NaiveWriteName_15,MeanWork_N_15,WorkErr_N_15,Times)

	WriteWorkTrend(WritePath,TimeOptWriteName_9,MeanWork_T_9,WorkErr_T_9,Times)
	WriteWorkTrend(WritePath,TimeOptWriteName_12,MeanWork_T_12,WorkErr_T_12,Times)
	WriteWorkTrend(WritePath,TimeOptWriteName_15,MeanWork_T_15,WorkErr_T_15,Times)

	WriteWorkTrend(WritePath,FullOptWriteName_9,MeanWork_F_9,WorkErr_F_9,Times)
	WriteWorkTrend(WritePath,FullOptWriteName_12,MeanWork_F_12,WorkErr_F_12,Times)
	WriteWorkTrend(WritePath,FullOptWriteName_15,MeanWork_F_15,WorkErr_F_15,Times)

	sns.set(style='darkgrid',palette='muted',color_codes=True)

	fig,axes = plt.subplots(4,3)

	pal = sns.cubehelix_palette(2*len(WorkArray_N_9))

	handle1 = r"$\tau = 50$"
	handle2 = r"$\tau = 600$"
	handle3 = r"$\tau = 1400$"
	handle4 = r"$\tau = 2200$"
	handle5 = r"$\tau = 3000$"

	sns.distplot(WorkArray_N_9[1],ax=axes[0,0],color=pal[0],label=handle1)
	sns.distplot(WorkArray_N_9[4],ax=axes[0,0],color=pal[1],label=handle2)		
	sns.distplot(WorkArray_N_9[8],ax=axes[0,0],color=pal[2],label=handle3)
	sns.distplot(WorkArray_N_9[12],ax=axes[0,0],color=pal[3],label=handle4)
	sns.distplot(WorkArray_N_9[16],ax=axes[0,0],color=pal[4],label=handle5)

	sns.distplot(WorkArray_N_12[1],ax=axes[0,1],color=pal[0],label=handle1)
	sns.distplot(WorkArray_N_12[4],ax=axes[0,1],color=pal[1],label=handle2)		
	sns.distplot(WorkArray_N_12[8],ax=axes[0,1],color=pal[2],label=handle3)
	sns.distplot(WorkArray_N_12[12],ax=axes[0,1],color=pal[3],label=handle4)
	sns.distplot(WorkArray_N_12[16],ax=axes[0,1],color=pal[4],label=handle5)

	sns.distplot(WorkArray_N_15[1],ax=axes[0,2],color=pal[0],label=handle1)
	sns.distplot(WorkArray_N_15[4],ax=axes[0,2],color=pal[1],label=handle2)		
	sns.distplot(WorkArray_N_15[8],ax=axes[0,2],color=pal[2],label=handle3)
	sns.distplot(WorkArray_N_15[12],ax=axes[0,2],color=pal[3],label=handle4)
	sns.distplot(WorkArray_N_15[16],ax=axes[0,2],color=pal[4],label=handle5)


	pal = sns.cubehelix_palette(2*len(WorkArray_T_9), start=0.25, rot=-0.25)

	sns.distplot(WorkArray_T_9[1],ax=axes[1,0],color=pal[0],label=handle1)
	sns.distplot(WorkArray_T_9[4],ax=axes[1,0],color=pal[1],label=handle2)		
	sns.distplot(WorkArray_T_9[8],ax=axes[1,0],color=pal[2],label=handle3)
	sns.distplot(WorkArray_T_9[12],ax=axes[1,0],color=pal[3],label=handle4)
	sns.distplot(WorkArray_T_9[16],ax=axes[1,0],color=pal[4],label=handle5)

	sns.distplot(WorkArray_T_12[1],ax=axes[1,1],color=pal[0],label=handle1)
	sns.distplot(WorkArray_T_12[4],ax=axes[1,1],color=pal[1],label=handle2)		
	sns.distplot(WorkArray_T_12[8],ax=axes[1,1],color=pal[2],label=handle3)
	sns.distplot(WorkArray_T_12[12],ax=axes[1,1],color=pal[3],label=handle4)
	sns.distplot(WorkArray_T_12[16],ax=axes[1,1],color=pal[4],label=handle5)

	sns.distplot(WorkArray_T_15[1],ax=axes[1,2],color=pal[0],label=handle1)
	sns.distplot(WorkArray_T_15[4],ax=axes[1,2],color=pal[1],label=handle2)		
	sns.distplot(WorkArray_T_15[8],ax=axes[1,2],color=pal[2],label=handle3)
	sns.distplot(WorkArray_T_15[12],ax=axes[1,2],color=pal[3],label=handle4)
	sns.distplot(WorkArray_T_15[16],ax=axes[1,2],color=pal[4],label=handle5)


	pal = sns.cubehelix_palette(2*len(WorkArray_F_9), start=-0.5, rot=-0.25)

	sns.distplot(WorkArray_F_9[1],ax=axes[2,0],color=pal[0],label=handle1)
	sns.distplot(WorkArray_F_9[4],ax=axes[2,0],color=pal[1],label=handle2)		
	sns.distplot(WorkArray_F_9[8],ax=axes[2,0],color=pal[2],label=handle3)
	sns.distplot(WorkArray_F_9[12],ax=axes[2,0],color=pal[3],label=handle4)
	sns.distplot(WorkArray_F_9[16],ax=axes[2,0],color=pal[4],label=handle5)

	sns.distplot(WorkArray_F_12[1],ax=axes[2,1],color=pal[0],label=handle1)
	sns.distplot(WorkArray_F_12[4],ax=axes[2,1],color=pal[1],label=handle2)		
	sns.distplot(WorkArray_F_12[8],ax=axes[2,1],color=pal[2],label=handle3)
	sns.distplot(WorkArray_F_12[12],ax=axes[2,1],color=pal[3],label=handle4)
	sns.distplot(WorkArray_F_12[16],ax=axes[2,1],color=pal[4],label=handle5)

	sns.distplot(WorkArray_F_15[1],ax=axes[2,2],color=pal[0],label=handle1)
	sns.distplot(WorkArray_F_15[4],ax=axes[2,2],color=pal[1],label=handle2)		
	sns.distplot(WorkArray_F_15[8],ax=axes[2,2],color=pal[2],label=handle3)
	sns.distplot(WorkArray_F_15[12],ax=axes[2,2],color=pal[3],label=handle4)
	sns.distplot(WorkArray_F_15[16],ax=axes[2,2],color=pal[4],label=handle5)


	axes[3,0].plot(Times,MeanWork_N_9,'r--',linewidth=3.0,alpha=0.5)
	axes[3,0].errorbar(Times,MeanWork_N_9,yerr=WorkErr_N_9,fmt='o',color='r',label="Naive")
	axes[3,0].plot(Times,MeanWork_T_9,'b--',linewidth=3.0,alpha=0.5)
	axes[3,0].errorbar(Times,MeanWork_T_9,yerr=WorkErr_T_9,fmt='o',color='b',label="Time-Optimized")
	axes[3,0].plot(Times,MeanWork_F_9,'g--',linewidth=3.0,alpha=0.5)
	axes[3,0].errorbar(Times,MeanWork_F_9,yerr=WorkErr_F_9,fmt='o',color='g',label="Fully-Optimal")

	axes[3,1].plot(Times,MeanWork_N_12,'r--',linewidth=3.0,alpha=0.5)
	axes[3,1].errorbar(Times,MeanWork_N_12,yerr=WorkErr_N_12,fmt='o',color='r',label="Naive")
	axes[3,1].plot(Times,MeanWork_T_12,'b--',linewidth=3.0,alpha=0.5)
	axes[3,1].errorbar(Times,MeanWork_T_12,yerr=WorkErr_T_12,fmt='o',color='b',label="Time-Optimized")
	axes[3,1].plot(Times,MeanWork_F_12,'g--',linewidth=3.0,alpha=0.5)
	axes[3,1].errorbar(Times,MeanWork_F_12,yerr=WorkErr_F_12,fmt='o',color='g',label="Fully-Optimal")

	axes[3,2].plot(Times,MeanWork_N_15,'r--',linewidth=3.0,alpha=0.5)
	axes[3,2].errorbar(Times,MeanWork_N_15,yerr=WorkErr_N_15,fmt='o',color='r',label="Naive")
	axes[3,2].plot(Times,MeanWork_T_15,'b--',linewidth=3.0,alpha=0.5)
	axes[3,2].errorbar(Times,MeanWork_T_15,yerr=WorkErr_T_15,fmt='o',color='b',label="Time-Optimized")
	axes[3,2].plot(Times,MeanWork_F_15,'g--',linewidth=3.0,alpha=0.5)
	axes[3,2].errorbar(Times,MeanWork_F_15,yerr=WorkErr_F_15,fmt='o',color='g',label="Fully-Optimal")

	axes[3,0].set_yscale('log')
	axes[3,1].set_yscale('log')
	axes[3,2].set_yscale('log')

	axes[0,0].legend(loc='upper left')
	axes[1,0].legend(loc='upper left')
	axes[2,0].legend(loc='upper left')
	axes[3,0].legend(loc='upper right')

	axes[3,0].set_xlabel(r'Protocol duration $\tau$',fontsize=15)
	axes[3,0].set_ylabel(r'Average excess work $\frac{\langle W_{\rm ex}\rangle_{\Lambda}}{\langle W\rangle_{\infty}} - 1$',fontsize=15)

	axes[2,0].set_xlabel(r'Work $\beta W$',fontsize=15)
	axes[2,0].set_ylabel(r'$P(\beta W)$',fontsize=15)

	plt.show()
	plt.close()




def WorkAnalysis(WorkArray,kBi,CPNum=25):

	MeanWork = np.mean(WorkArray)
	StdDev = np.std(WorkArray)
	StdErr = 2*StdDev/float(sqrt(len(WorkArray)-1))

	InfiniteWork = CalculateInfiniteWork(CPNum,kBi)

	CorrectedWork = ((MeanWork/float(InfiniteWork)) - 1)
	CorrectedErr = (StdErr/float(InfiniteWork))

	return CorrectedWork,CorrectedErr


def CalculateInfiniteWork(CPNum,kBi):

	CPInit = -1
	CPStep = 2/float(CPNum-1)

	CPVals = []

	CurrCP = CPInit

	for index in range(CPNum):
		CPVals.append(CurrCP)
		CurrCP += CPStep

	WorkAcc = 0

	for index in range(len(CPVals)-1):
		WorkAcc += WorkStep(CPVals[index],CPVals[index+1],kBi)

	return WorkAcc


def WorkStep(CP1,CP2,kBi):

	XMin = -5
	XMax = 5
	dX = 0.01

	XRange = []
	XCurr = XMin

	while XCurr <= XMax:
		XRange.append(XCurr)
		XCurr += dX

	Dist1 = Boltzmann(CP1,XRange,kBi)
	Dist2 = Boltzmann(CP2,XRange,kBi)

	Work = (1/float(1))*RelativeEntropy(Dist1,Dist2,dX)

	return Work


def Boltzmann(CPVal,XRange,kBi):

	Prob = []
	NormFactor = 0

	dX = XRange[1] - XRange[0]

	for index in range(len(XRange)):

		Energy = TotalEnergy(CPVal,XRange[index],kBi)
		Prob.append(exp(-1*Energy))
		NormFactor += exp(-1*Energy)*dX

	for index in range(len(Prob)):
		Prob[index] = Prob[index]/float(NormFactor)

	return Prob


def RelativeEntropy(Dist1,Dist2,dX):

	RelativeEntropy = 0

	for index in range(len(Dist1)):
		RelativeEntropy += log(Dist1[index]/Dist2[index])*Dist1[index]*dX

	return RelativeEntropy


def TotalEnergy(CP, position, kBi):

	EnergyTrap = 0.5*1.5*((position - CP)**2)
	EnergyBistable = -(1/float(1))*log(exp(-1*0.5*kBi*((position + 1)**2)) + exp(-1*0.5*kBi*((position - 1)**2)))

	TotalEnergy = EnergyTrap + EnergyBistable

	return TotalEnergy


def ReadData(Filename):

	Work = []

	file1 = open(Filename,'r')
	TempData = file1.readlines()
	file1.close()

	for index in range(len(TempData)):
		Work.append(eval(TempData[index]))

	return Work


#def WorkAnalysis(WorkArray):

	#MeanWork = np.mean(WorkArray)
	#WorkErr = np.std(WorkArray)/sqrt(len(WorkArray)-1)

	#return MeanWork,WorkErr

def WriteWorkTrend(Path,Filename,Work,Err,Time):

	CompleteName = os.path.join(Path,Filename)

	file1 = open(CompleteName,'w')

	for index in range(len(Work)):
		file1.write("%lf\t%lf\t%lf\n" % (Time[index],Work[index],Err[index]))

	file1.close()




PlotPanels()


