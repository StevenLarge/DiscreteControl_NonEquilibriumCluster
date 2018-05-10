#Python script to generate the CP Trend data for discrete control protocols
#
#Steven Large
#April 18th 2018

import os
import numpy as np
from math import *
import matplotlib.pyplot as plt
import seaborn as sns


Xm = 1
kL = 12
kR = 12
beta = 1
kTrap = 1.5

def GeneratePlot(Path="/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/NonEquilibrium_Local/WorkDistributions_April23/",Param="12_15",Tau = 2000,option=1):

	FilenameNaive_Base = "WorkDist_Master_" + Param + "_Naive_CP" 
	FilenameSpaceOpt_Base = "WorkDist_Master_" + Param + "_SpaceOpt_CP"
	FilenameFullOpt_Base = "WorkDist_Master_" + Param + "_FullOpt_CP"

	CPRange = [4,8,16,32,64,128,256,512]
	TimeRange = [800,1600,3200,6400,12800,25600,51200,102400]

	WorkDist_Naive = []
	WorkDist_SpaceOpt = []
	WorkDist_FullOpt = []

	WorkDist_Naive_Full = []
	WorkDist_SpaceOpt_Full = []
	WorkDist_FullOpt_Full = []

	for index in range(len(CPRange)):

		FilenameNaive = FilenameNaive_Base + str(CPRange[index]) + "_T2000.dat"
		FilenameSpaceOpt = FilenameSpaceOpt_Base + str(CPRange[index]) + "_T2000.dat"
		FilenameFullOpt = FilenameFullOpt_Base + str(CPRange[index]) + "_T2000.dat"

		WorkDist_Naive.append(ReadWorkData(Path,FilenameNaive))
		WorkDist_SpaceOpt.append(ReadWorkData(Path,FilenameSpaceOpt))
		WorkDist_FullOpt.append(ReadWorkData(Path,FilenameFullOpt))

	if(option==1):
		TwoHistoPlot(CPRange,TimeRange,WorkDist_Naive,WorkDist_SpaceOpt)
	elif(option==2):
		ThreeHistoPlot(CPRange,TimeRange,WorkDist_Naive,WorkDist_SpaceOpt,WorkDist_FullOpt)
	else:
		print "\n\n\t\t----- Option Flag not valid -----\n\n"


def WorkAnalysis(WorkArray,CPRange):

	MeanWork = []
	StdErr = []

	#print "Len WorkArray --> " + str(len(WorkArray)) + "\n\n"

	for index in range(len(WorkArray)):
		MeanWork.append(np.mean(WorkArray[index]))
		StdDev = np.std(WorkArray[index])
		StdErr.append(StdDev/sqrt(len(WorkArray[index])-1))

	return MeanWork,StdErr


def TwoHistoPlot(CPRange,TimeRange,Work1,Work2):

	sns.set(style='darkgrid', palette='muted', color_codes=True)

	fig,axes = plt.subplots(3,1,figsize=(5,7))

	pal = sns.cubehelix_palette(2*len(Work1))
	for index in range(len(CPRange)):
		handle = r'$|\{\lambda\}|$ = ' + str(CPRange[index])
		sns.distplot(Work1[index],color=pal[index],ax=axes[0],label=handle)

	pal = sns.cubehelix_palette(2*len(Work2),start=-0.5,rot=-0.25)
	for index in range(len(CPRange)):
		handle = r'$|\{\lambda\}|$ = ' + str(CPRange[index])
		sns.distplot(Work2[index],color=pal[index],ax=axes[1],label=handle)

	axes[0].legend(loc='upper left')
	axes[1].legend(loc='upper left')

	MeanWork1,StdErr1 = WorkAnalysis(Work1,CPRange)
	MeanWork2,StdErr2 = WorkAnalysis(Work2,CPRange)

	axes[2].plot(CPRange,MeanWork1,'r--',linewidth=3.0,alpha=0.75)
	axes[2].plot(CPRange,MeanWork2,'g--',linewidth=3.0,alpha=0.75)

	axes[2].errorbar(CPRange,MeanWork1,yerr=StdErr1,fmt='ro',label="Naive")
	axes[2].errorbar(CPRange,MeanWork2,yerr=StdErr2,fmt='go',label="Space-Optimized")

	axes[2].set_yscale('log')
	axes[2].set_xscale('log')
	axes[2].legend(loc='upper right')

	axes[1].set_xlabel(r'Work $\beta W$',fontsize=15)
	axes[1].set_ylabel(r'$P(\beta W)$',fontsize=15)

	axes[2].set_xlabel(r'Number of $\lambda$ values',fontsize=15)
	axes[2].set_ylabel(r'$\frac{\langle W_{\rm ex}\rangle_{\Lambda}}{\langle W_{\rm ex}\rangle_{\lambda_{\rm i}\rightarrow\lambda_{\rm f}}}$',fontsize=15)

	plt.show()
	plt.close()



def ThreeHistoPlot(CPRange,TimeRange,Work1,Work2,Work3):

	sns.set(style='darkgrid', palette='muted', color_codes=True)

	fig,axes = plt.subplots(3,1,figsize=(5,10))

	pal = sns.cubehelix_palette(2*len(Work1))
	for index in range(len(CPRange)):
		handle = r'$|\{\lambda\}|$ = ' + str(CPRange[index])
		sns.distplot(Work1[index],color=pal[index],ax=axes[0],label=handle)

	pal = sns.cubehelix_palette(2*len(Work2),start=-0.5,rot=-0.25)
	for index in range(len(CPRange)):
		handle = r'$|\{\lambda\}|$ = ' + str(CPRange[index])
		sns.distplot(Work2[index],color=pal[index],ax=axes[1],label=handle)

	pal = sns.cubehelix_palette(2*len(Work3),start=0.5,rot=-0.25)
	for index in range(len(CPRange)):
		handle = r'$|\{\lambda\}|$ = ' + str(CPRange[index])
		sns.distplot(Work3[index],color=pal[index],ax=axes[2],label=handle)

	axes[0].legend(loc='upper left')
	axes[1].legend(loc='upper left')

	MeanWork1,StdErr1 = WorkAnalysis(Work1,CPRange)
	MeanWork2,StdErr2 = WorkAnalysis(Work2,CPRange)
	MeanWork3,StdErr3 = WorkAnalysis(Work3,CPRange)

	axes[3].plot(CPRange,Work1,'r--',linewidth=3.0,alpha=0.75)
	axes[3].plot(CPRange,Work2,'g--',linewidth=3.0,alpha=0.75)
	axes[3].plot(CPRange,Work3,'p--',linewidth=3.0,alpha=0.75)

	axes[3].errorbar(CPRange,Work1,yerr=StdErr1,fmt='ro',label="Naive")
	axes[3].errorbar(CPRange,Work2,yerr=StdErr2,fmt='go',label="Space-Optimized")
	axes[3].errorbar(CPRange,Work3,yerr=StdErr3,fmt='po',label="Fully-Optimized")

	axes[3].set_yscale('log')
	axes[3].set_xscale('log')
	axes[3].legend(loc='upper right')

	axes[2].set_xlabel(r'Work $\beta W$',fontsize=15)
	axes[2].set_ylabel(r'$P(\beta W)$',fontsize=15)

	axes[3].set_xlabel(r'Number of $\lambda$ values',fontsize=15)
	axes[3].set_ylabel(r'$\frac{\langle W_{\rm ex}\rangle_{\Lambda}}{\langle W_{\rm ex}\rangle_{\lambda_{\rm i}\rightarrow\lambda_{\rm f}}}$',fontsize=15)

	plt.show()
	plt.close()


def ReadWorkData(Path,Filename):

	CompleteName = os.path.join(Path,Filename)

	file1 = open(CompleteName,'r')
	TempData = file1.readlines()
	file1.close()

	WorkArray = []

	for index in range(len(TempData)):
		WorkArray.append(eval(TempData[index]))

	return WorkArray


GeneratePlot()

