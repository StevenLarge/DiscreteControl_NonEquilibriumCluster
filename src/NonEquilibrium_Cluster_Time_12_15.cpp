/* This is a C++ implementation of a dynamical nonequilibrium propogator for calculating the work required to execute a discrete protocol */

#include <fstream>
#include <iostream>
#include <random>
#include <cmath>
#include <string>
#include <ctime>

#include "include/DiscreteControl.h"
#include "include/ReadWrite.h"
#include "include/Numerics.h"

using namespace std;


int main(){

	string Param_Ex = "12_15";
	string ProtocolPath = "Protocols_12_15/";

	int Protocol_Repetitions = 1000000;

	string ReadName_Time;
	string ReadName_Naive;
	string ReadName_Full;

	string WorkWrite_Naive;
	string WorkWrite_TimeOpt;
	string WorkWrite_Full;

	int NumCPVals_TimeTrend = 25;
	int TotalTime_Vector [] = {10,50,200,400,600,800,1000,1200,1400,1600,1800,2000,2200,2400,2600,2800,3000};

	int TotalTime_VectorSize = 17;

	double * WorkArray;
	WorkArray = new double [Protocol_Repetitions];


	/* Time Trend Calculations */

	double * CPVals_Naive;
	double * LagTimes_Naive;
	double * CPVals_TimeOpt;
	double * LagTimes_TimeOpt;
	double * CPVals_Full;
	double * LagTimes_Full;

	CPVals_Naive = new double [NumCPVals_TimeTrend];
	LagTimes_Naive = new double [NumCPVals_TimeTrend];
	CPVals_TimeOpt = new double [NumCPVals_TimeTrend];
	LagTimes_TimeOpt = new double [NumCPVals_TimeTrend];
	CPVals_Full = new double [NumCPVals_TimeTrend];
	LagTimes_Full = new double [NumCPVals_Time];

	for(int k = 0 ; k < TotalTime_VectorSize ; k++){

		ReadName_Naive = ProtocolPath + "Naive_CP" + std::to_string(NumCPVals_TimeTrend) + "_T" + std::to_string(TotalTime_Vector[k]) + ".dat";
		ReadName_Time = ProtocolPath + "TimeOpt_CP" + std::to_string(NumCPVals_TimeTrend) + "_T" + std::to_string(TotalTime_Vector[k]) + ".dat";
		ReadName_Full = ProtocolPath + "FullOpt_CP" + std::to_string(NumCPVals_TimeTrend) + "_T" + std::to_string(TotalTime_Vector[k]) + ".dat";

		WorkWrite_Naive = "WorkDistributions/WorkDist_" + Param_Ex + "_Naive_CP" + std::to_string(NumCPVals_TimeTrend) + "_T" + std::to_string(TotalTime_Vector[k]) + ".dat";
		WorkWrite_TimeOpt = "WorkDistributions/WorkDist_" + Param_Ex + "_TimeOpt_CP" + std::to_string(NumCPVals_TimeTrend) + "_T" + std::to_string(TotalTime_Vector[k]) + ".dat";
		WorkWrite_FullOpt = "WorkDistributions/WorkDist_" + Param_Ex + "_FullOpt_CP" + std::to_string(NumCPVals_TimeTrend) + "_T" + std::to_string(TotalTime_Vector[k]) + ".dat";

		ImportProtocol_String(CPVals_Naive, LagTimes_Naive, NumCPVals_TimeTrend, ReadName_Naive);
		ImportProtocol_String(CPVals_TimeOpt, LagTimes_TimeOpt, NumCPVals_TimeTrend, ReadName_Time);
		ImportProtocol_String(CPVals_FullOpt, LagTImes_FullOpt, NumCPVals_TimeTrend, ReadName_Full);

		//cout << "\n\nLagTimes --> \t\t" << std::to_string(TotalTime_Vector[k]) << "\n";

		PropogateProtocol(WorkArray, CPVals_Naive, LagTimes_Naive, NumCPVals_TimeTrend, Protocol_Repetitions);
		WriteWorkArray(WorkWrite_Naive,WorkArray,Protocol_Repetitions);
		PropogateProtocol(WorkArray, CPVals_TimeOpt, LagTimes_TimeOpt, NumCPVals_TimeTrend, Protocol_Repetitions);
		WriteWorkArray(WorkWrite_TimeOpt,WorkArray,Protocol_Repetitions);
		PropogateProtocol(WorkArray, CPVals_FullOpt, LagTimes_FullOpt, NumCPVals_TimeTrend, Protocol_Repetitions);
		WriteWorkArray(WorkWrite_FullOpt,WorkArray,Protocol_Repetitions);

	}

	delete CPVals_Naive;
	delete LagTimes_Naive;
	delete CPVals_TimeOpt;
	delete LagTimes_TimeOpt;
	delete CPVals_FullOpt;
	delete LagTimes_FullOpt;

	delete WorkArray;


}