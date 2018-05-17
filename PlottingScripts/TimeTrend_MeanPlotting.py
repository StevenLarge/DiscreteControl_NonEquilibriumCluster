#This plotting script shows the ratio of time optimized vs naive protocols in discrete control simulations
#
#Steven Large
#May16th 2018

import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from math import *

def ReadData(Path,Filename):

	CompleteName = os.path.join(Path,Filename)
	file1 = open(CompleteName,'r')
	TempData = file1.readlines()
	file1.close()

	Work = []
	CPVals = []
	StdErr = []

	for index in range(len(TempData)):
		Parsed = TempData[index].split()

		CPVals.append(eval(Parsed[0]))
		Work.append(eval(Parsed[1]))
		StdErr.append(eval(Parsed[2]))

	return CPVals,Work,StdErr


Path = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/NonEquilibrium_Local/WorkAnalysisFiles/"

NaiveName = "MeanWorkTrend_N_Time_12.dat"
SpaceName = "MeanWorkTrend_T_Time_12.dat"

CPVals_Naive,Work_Naive,Err_Naive = ReadData(Path,NaiveName)
CPVals_Space,Work_Space,Err_Space = ReadData(Path,SpaceName)

WorkRatio = []

for index in range(len(Work_Naive)):
	WorkRatio.append(Work_Space[index]/Work_Naive[index])

sns.set(style='darkgrid',palette='muted',color_codes=True)

fig,ax = plt.subplots(2,1)

ax[0].plot(CPVals_Naive,Work_Naive,'r--',linewidth=2.5)
ax[0].plot(CPVals_Space,Work_Space,'b--',linewidth=2.5)

ax[0].errorbar(CPVals_Naive,Work_Naive,yerr=Err_Naive,fmt='o',color='r')
ax[0].errorbar(CPVals_Space,Work_Space,yerr=Err_Space,fmt='o',color='b')

ax[0].set_yscale('log')

ax[1].plot(CPVals_Naive,WorkRatio,'k--',linewidth=2.5)
ax[1].plot(CPVals_Naive,WorkRatio,'ko',linewidth=2.5)

ax[1].set_xlabel(r'Number of control parameter values',fontsize=20)
ax[0].set_ylabel(r'$\frac{\langle W_{\rm ex}\rangle_{\Lambda}}{\langle W\rangle_{\infty}} - 1$',fontsize=20)

ax[1].set_ylabel(r'$\frac{\langle W_{\rm ex}\rangle_{\rm Opt}}{\langle W_{\rm ex}\rangle_{\rm Naive}}$',fontsize=20)

plt.show()
plt.close()