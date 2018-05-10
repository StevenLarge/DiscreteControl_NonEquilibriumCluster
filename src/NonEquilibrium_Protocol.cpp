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
	string WritePath = "WorkData_12_15/";

	int Protocol_Repetitions = 10000;

	string ReadName_Time;
	string ReadName_Space;
	string ReadName_Naive;
	string ReadName_Full;

	string WorkWrite_Naive;
	string WorkWrite_SpaceOpt;
	string WorkWrite_TimeOpt;
	string WorkWrite_Full;

	int NumCPVals_TimeTrend = 25;
	int LagTime_StepTrend = 200;
	int LagTime_StepTrend_Long = 2000;

	int CPVal_Vector [] = {4,8,16,32,64,128,256,512};
	int TotalTime_Vector [] = {10,50,200,400,600,800,1000,1200,1400,1600,1800,2000,2200,2400,2600,2800,3000};//,3200,3400,3600,3800,4000,4200,4400,4600,4800,5000};

	//int CPVal_Vector [] = {8,16};
	//int TotalTime_Vector [] = {2000,2200};

	int CPVal_VectorSize = 8;
	int TotalTime_VectorSize = 17;//27;
	
	double * WorkArray;
	WorkArray = new double [Protocol_Repetitions];


	/* CP Trend calculation */

	for(int k = 0 ; k < CPVal_VectorSize ; k++){

		ReadName_Naive = ProtocolPath + "Naive_CP" + std::to_string(CPVal_Vector[k]) + "_T" + std::to_string(LagTime_StepTrend) + ".dat";
		ReadName_Space = ProtocolPath + "SpaceOpt_CP" + std::to_string(CPVal_Vector[k]) + "_T" + std::to_string(LagTime_StepTrend) + ".dat";
		ReadName_Full = ProtocolPath + "FullOpt_CP" + std::to_string(CPVal_Vector[k]) + "_T" + std::to_string(LagTime_StepTrend) + ".dat";

		WorkWrite_Naive = "WorkDistributions/WorkDist_3_" + Param_Ex + "_Naive_CP" + std::to_string(CPVal_Vector[k]) + "_T" + std::to_string(LagTime_StepTrend_Long) + ".dat";
		WorkWrite_SpaceOpt = "WorkDistributions/WorkDist_3_" + Param_Ex + "_SpaceOpt_CP" + std::to_string(CPVal_Vector[k]) + "_T" + std::to_string(LagTime_StepTrend_Long) + ".dat";
		WorkWrite_Full = "WorkDistributions/WorkDist_3_" + Param_Ex + "_FullOpt_CP" + std::to_string(CPVal_Vector[k]) + "_T" + std::to_string(LagTime_StepTrend_Long) + ".dat";

		//cout << "----- Readname -----\n" << ReadName_Naive << "\n\n";

		double * CPVals_Naive;
		double * LagTimes_Naive;
		double * CPVals_SpaceOpt;
		double * LagTimes_SpaceOpt;
		double * CPVals_FullOpt;
		double * LagTimes_FullOpt;

		CPVals_Naive = new double [CPVal_Vector[k]];
		LagTimes_Naive = new double [CPVal_Vector[k]];
		CPVals_SpaceOpt = new double [CPVal_Vector[k]];
		LagTimes_SpaceOpt = new double [CPVal_Vector[k]];
		CPVals_FullOpt = new double [CPVal_Vector[k]];
		LagTimes_FullOpt = new double [CPVal_Vector[k]];

		ImportProtocol_String(CPVals_Naive, LagTimes_Naive, CPVal_Vector[k], ReadName_Naive);
		ImportProtocol_String(CPVals_SpaceOpt, LagTimes_SpaceOpt, CPVal_Vector[k], ReadName_Space);
		ImportProtocol_String(CPVals_FullOpt, LagTimes_FullOpt, CPVal_Vector[k], ReadName_Full);

		for(int j = 0 ; j < CPVal_Vector[k] ; j++){
			LagTimes_Naive[j] = 10.0*LagTimes_Naive[j];
			LagTimes_SpaceOpt[j] = 10.0*LagTimes_SpaceOpt[j];
			LagTimes_FullOpt[j] = 10.0*LagTimes_FullOpt[j];
		}

		PropogateProtocol(WorkArray, CPVals_Naive, LagTimes_Naive, CPVal_Vector[k], Protocol_Repetitions);
		WriteWorkArray(WorkWrite_Naive,WorkArray,Protocol_Repetitions);
		PropogateProtocol(WorkArray, CPVals_SpaceOpt, LagTimes_SpaceOpt, CPVal_Vector[k], Protocol_Repetitions);
		WriteWorkArray(WorkWrite_SpaceOpt,WorkArray,Protocol_Repetitions);
		PropogateProtocol(WorkArray, CPVals_FullOpt, LagTimes_FullOpt, CPVal_Vector[k], Protocol_Repetitions);
		WriteWorkArray(WorkWrite_Full,WorkArray,Protocol_Repetitions);
		
		cout << "\t\t-- CP --\n";

		delete CPVals_Naive;
		delete LagTimes_Naive;
		delete CPVals_SpaceOpt;
		delete LagTimes_SpaceOpt;
		delete CPVals_FullOpt;
		delete LagTimes_FullOpt;

	}
	

	/* Time Trend Calculations */

	double * CPVals_Naive;
	double * LagTimes_Naive;
	double * CPVals_TimeOpt;
	double * LagTimes_TimeOpt;
	double * CPVals_FullOpt;
	double * LagTimes_FullOpt;

	CPVals_Naive = new double [NumCPVals_TimeTrend];
	LagTimes_Naive = new double [NumCPVals_TimeTrend];
	CPVals_TimeOpt = new double [NumCPVals_TimeTrend];
	LagTimes_TimeOpt = new double [NumCPVals_TimeTrend];
	CPVals_FullOpt = new double [NumCPVals_TimeTrend];
	LagTimes_FullOpt = new double [NumCPVals_TimeTrend];


	for(int k = 0 ; k < TotalTime_VectorSize ; k++){

		ReadName_Naive = ProtocolPath + "Naive_CP" + std::to_string(NumCPVals_TimeTrend) + "_T" + std::to_string(TotalTime_Vector[k]) + ".dat";
		ReadName_Time = ProtocolPath + "TimeOpt_CP" + std::to_string(NumCPVals_TimeTrend) + "_T" + std::to_string(TotalTime_Vector[k]) + ".dat";
		ReadName_Full = ProtocolPath + "FullOpt_CP" + std::to_string(NumCPVals_TimeTrend) + "_T" + std::to_string(TotalTime_Vector[k]) + ".dat";

		WorkWrite_Naive = "WorkDistributions/WorkDist_3_" + Param_Ex + "_Naive_CP" + std::to_string(NumCPVals_TimeTrend) + "_T" + std::to_string(TotalTime_Vector[k]) + ".dat";
		WorkWrite_TimeOpt = "WorkDistributions/WorkDist_3_" + Param_Ex + "_TimeOpt_CP" + std::to_string(NumCPVals_TimeTrend) + "_T" + std::to_string(TotalTime_Vector[k]) + ".dat";
		WorkWrite_Full = "WorkDistributions/WorkDist_3_" + Param_Ex + "_FullOpt_CP" + std::to_string(NumCPVals_TimeTrend) + "_T" + std::to_string(TotalTime_Vector[k]) + ".dat";

		ImportProtocol_String(CPVals_Naive, LagTimes_Naive, NumCPVals_TimeTrend, ReadName_Naive);
		ImportProtocol_String(CPVals_TimeOpt, LagTimes_TimeOpt, NumCPVals_TimeTrend, ReadName_Time);
		ImportProtocol_String(CPVals_FullOpt, LagTimes_FullOpt, NumCPVals_TimeTrend, ReadName_Full);

		PropogateProtocol(WorkArray, CPVals_Naive, LagTimes_Naive, NumCPVals_TimeTrend, Protocol_Repetitions);
		WriteWorkArray(WorkWrite_Naive,WorkArray,Protocol_Repetitions);
		PropogateProtocol(WorkArray, CPVals_TimeOpt, LagTimes_TimeOpt, NumCPVals_TimeTrend, Protocol_Repetitions);
		WriteWorkArray(WorkWrite_TimeOpt,WorkArray,Protocol_Repetitions);
		PropogateProtocol(WorkArray, CPVals_FullOpt, LagTimes_FullOpt, NumCPVals_TimeTrend, Protocol_Repetitions);
		WriteWorkArray(WorkWrite_Full,WorkArray,Protocol_Repetitions);
		
		cout << "\t\t-- Time --\n";

	}

	delete CPVals_Naive;
	delete LagTimes_Naive;
	delete CPVals_TimeOpt;
	delete LagTimes_TimeOpt;
	delete CPVals_FullOpt;
	delete LagTimes_FullOpt;
	delete WorkArray;

}
