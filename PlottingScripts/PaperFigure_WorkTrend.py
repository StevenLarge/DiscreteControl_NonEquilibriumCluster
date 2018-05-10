#This python script generates the work comparison plot for the discrete control paper
#
#Steven Large
#April 24th 2018

import os
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from math import *

def GeneratePlot_Time(Path="/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/NonEquilibrium_Local/WorkDistributions_FromCluster/",option=1):

	Filename_Naive_Base_9 = "WorkDist_9_15_Naive_CP25_T"
	Filename_Naive_Base_12 = "WorkDist_12_15_Naive_CP25_T"	
	Filename_Naive_Base_15 = "WorkDist_15_15_Naive_CP25_T"

	Filename_TimeOpt_Base_9 = "WorkDist_9_15_TimeOpt_CP25_T"
	Filename_TimeOpt_Base_12 = "WorkDist_12_15_TimeOpt_CP25_T"
	Filename_TimeOpt_Base_15 = "WorkDist_15_15_TimeOpt_CP25_T"

	Filename_FullOpt_Base_9 = "WorkDist_9_15_FullOpt_CP25_T"
	Filename_FullOpt_Base_12 = "WorkDist_12_15_FullOpt_CP25_T"
	Filename_FullOpt_Base_15 = "WorkDist_15_15_FullOpt_CP25_T"
	
	Times = [10,50,200,400,600,800,1000,1200,1400,1600,1800,2000,2200,2400,2600,2800,3000]

	InfWork_9 = InfiniteWork(9)
	InfWork_12 = InfiniteWork(12)
	InfWork_15 = InfiniteWork(15)

	for index in range(len(Times)):

		WorkNaive_9 = ImportData(Path,Filename_Naive_Base_9+str(Times[index])+".dat")
		WorkNaive_12 = ImportData(Path,Filename_Naive_Base_12+str(Times[index])+".dat")
		WorkNaive_15 = ImportData(Path,Filename_Naive_Base_15+str(Times[index])+".dat")

		WorkTimeOpt_9 = ImportData(Path,Filename_TimeOpt_Base_9+str(Times[index])+".dat")
		WorkTimeOpt_12 = ImportData(Path,Filename_TimeOpt_Base_12+str(Times[index])+".dat")
		WorkTimeOpt_15 = ImportData(Path,Filename_TimeOpt_Base_15+str(Times[index])+".dat")

		WorkFullOpt_9 = ImportData(Path,Filename_FullOpt_Base_9+str(Times[index])+".dat")
		WorkFullOpt_12 = ImportData(Path,Filename_FullOpt_Base_12+str(Times[index])+".dat")
		WorkFullOpt_15 = ImportData(Path,Filename_FullOpt_Base_15+str(Times[index])+".dat")

		MeanNaive_9.append(np.mean(WorkNaive_9)/InfWork_9)
		MeanNaive_12.append(np.mean(WorkNaive_12)/InfWork_12)
		MeanNaive_15.append(np.mean(WorkNaive_15)/InfWork_15)

		MeanTimeOpt_9.append(np.mean(WorkTimeOpt_9)/InfWork_9)
		MeanTimeOpt_12.append(np.mean(WorkTimeOpt_12)/InfWork_12)
		MeanTimeOpt_15.append(np.mean(WorkTimeOpt_15)/InfWork_15)

		MeanFullOpt_9.append(np.mean(WorkFullOpt_9)/InfWork_9)
		MeanFullOpt_12.append(np.mean(WorkFullOpt_12)/InfWork_12)
		MeanFullOpt_15.append(np.mean(WorkFullOpt_15)/InfWork_15)

		StdErrNaive_9.append(np.std(WorkNaive_9)/sqrt(len(WorkNaive_9)-1)*(float(1)/InfWork_9))
		StdErrNaive_12.append(np.std(WorkNaive_12)/sqrt(len(WorkNaive_12)-1)*(float(1)/InfWork_12))
		StdErrNaive_15.append(np.std(WorkNaive_15)/sqrt(len(WorkNaive_15)-1)*(float(1)/InfWork_15))

		StdErrTimeOpt_9.append(np.std(WorkTimeOpt_9)/sqrt(len(WorkTimeOpt_9)-1)*(float(1)/InfWork_9))
		StdErrTimeOpt_12.append(np.std(WorkTimeOpt_12)/sqrt(len(WorkTimeOpt_12)-1)*(float(1)/InfWork_12))
		StdErrTimeOpt_15.append(np.std(WorkTimeOpt_15)/sqrt(len(WorkTimeOpt_15)-1)*(float(1)/InfWork_15))

		StdErrFullOpt_9.append(np.std(WorkFullOpt_9)/sqrt(len(WorkFullOpt_9)-1)*(float(1)/InfWork_9))
		StdErrFullOpt_12.append(np.std(WorkFullOpt_12)/sqrt(len(WorkFullOpt_12)-1)*(float(1)/InfWork_12))
		StdErrFullOpt_15.append(np.std(WorkFullOpt_15)/sqrt(len(WorkFullOpt_15)-1)*(float(1)/InfWork_15))

	sns.set()

	fig,ax = plt.subplots(1,3,sharex=True,sharey=True)

	ax[0].plot(Times,MeanNaive_9,'--',color='r',linewidth=3.0,alpha=0.5)
	ax[1].plot(Times,MeanNaive_12,'--',color='r',linewidth=3.0,alpha=0.5)
	ax[2].plot(Times,MeanNaive_15,'--',color='r',linewidth=3.0,alpha=0.5)	

	ax[0].plot(Times,MeanTimeOpt_9,'--',color='b',linewidth=3.0,alpha=0.5)
	ax[1].plot(Times,MeanTimeOpt_12,'--',color='b',linewidth=3.0,alpha=0.5)
	ax[2].plot(Times,MeanTimeOpt_15,'--',color='b',linewidth=3.0,alpha=0.5)	

	ax[0].plot(Times,MeanFullOpt_9,'--',color='m',linewidth=3.0,alpha=0.5)
	ax[1].plot(Times,MeanFullOpt_12,'--',color='m',linewidth=3.0,alpha=0.5)
	ax[2].plot(Times,MeanFullOpt_15,'--',color='m',linewidth=3.0,alpha=0.5)	

	ax[0].errorbar(Times,MeanNaive_9,yerr=StdErrNaive_9,'ro',linewidth=2.5)
	ax[1].errorbar(Times,MeanNaive_12,yerr=StdErrNaive_12,'ro',linewidth=2.5)
	ax[2].errorbar(Times,MeanNaive_15,yerr=StdErrNaive_15,'ro',linewidth=2.5)

	ax[0].errorbar(Times,MeanTimeOpt_9,yerr=StdErrTimeOpt_9,'ro',linewidth=2.5)
	ax[1].errorbar(Times,MeanTimeOpt_12,yerr=StdErrTimeOpt_12,'ro',linewidth=2.5)
	ax[2].errorbar(Times,MeanTimeOpt_15,yerr=StdErrTimeOpt_15,'ro',linewidth=2.5)

	ax[0].errorbar(Times,MeanFullOpt_9,yerr=StdErrFullOpt_9,'ro',linewidth=2.5)
	ax[1].errorbar(Times,MeanFullOpt_12,yerr=StdErrFullOpt_12,'ro',linewidth=2.5)
	ax[2].errorbar(Times,MeanFullOpt_15,yerr=StdErrFullOpt_15,'ro',linewidth=2.5)

	ax[0].set_yscale('log')
	ax[1].set_yscale('log')
	ax[2].set_yscale('log')

	ax[0].set_xlabel(r'Protocol duration $\tau$',fontsize=16)
	ax[0].set_ylabel(r'Average excess work $\frac{\langle W_{\rm ex}\rangle_{\Lambda}}{\langle W_{\rm ex}^{\infty}\rangle_{\Lambda}}$',fontsize=16)

	ax[0].set_title(r'$k_{\rm bi}^* = 9$',fontsize=16)
	ax[1].set_title(r'$12$',fontsize=16)
	ax[2].set_title(r'$15$',fontsize=16)

	plt.show()
	plt.close()


def InfiniteWork(kBi):

	InfWork = 0

	return InfWork


def ImportData(Path,Filename):

	CompleteName = os.path.join(Path,Filename)

	WorkArray = []
	file1 = open(CompleteName,'r')
	TempData = file1.readlines()
	file1.close()

	for index in range(len(TempData)):
		WorkArray.append(eval(TempData[index]))

	return WorkArray





