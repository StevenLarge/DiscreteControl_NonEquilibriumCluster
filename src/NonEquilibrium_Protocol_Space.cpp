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
	int CPTime_Vector [] = {800,1600,3200,6400,12800,25600,51200,102400};

	int CPVal_VectorSize = 8;
	
	double * WorkArray;
	WorkArray = new double [Protocol_Repetitions];


	/* CP Trend calculation */

	for(int k = 0 ; k < CPVal_VectorSize ; k++){

		ReadName_Naive = ProtocolPath + "Naive_CP" + std::to_string(CPVal_Vector[k]) + "_T" + std::to_string(LagTime_StepTrend) + ".dat";
		ReadName_Space = ProtocolPath + "SpaceOpt_CP" + std::to_string(CPVal_Vector[k]) + "_T" + std::to_string(LagTime_StepTrend) + ".dat";
		ReadName_Full = ProtocolPath + "FullOpt_CP" + std::to_string(CPVal_Vector[k]) + "_T" + std::to_string(LagTime_StepTrend) + ".dat";

		WorkWrite_Naive = "WorkDistributions/WorkDist_" + Param_Ex + "_Naive_CP" + std::to_string(CPVal_Vector[k]) + "_T" + std::to_string(LagTime_StepTrend_Long) + ".dat";
		WorkWrite_SpaceOpt = "WorkDistributions/WorkDist_" + Param_Ex + "_SpaceOpt_CP" + std::to_string(CPVal_Vector[k]) + "_T" + std::to_string(LagTime_StepTrend_Long) + ".dat";
		WorkWrite_Full = "WorkDistributions/WorkDist_" + Param_Ex + "_FullOpt_CP" + std::to_string(CPVal_Vector[k]) + "_T" + std::to_string(LagTime_StepTrend_Long) + ".dat";

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
			LagTimes_Naive[j] = (CPTime_Vector[k]/200.0)*LagTimes_Naive[j];
			LagTimes_SpaceOpt[j] = (CPTime_Vector[k]/200.0)*LagTimes_SpaceOpt[j];
			LagTimes_FullOpt[j] = (CPTime_Vector[k]/200.0)*LagTimes_FullOpt[j];
		}

		PropogateProtocol(WorkArray, CPVals_Naive, LagTimes_Naive, CPVal_Vector[k], Protocol_Repetitions);
		WriteWorkArray(WorkWrite_Naive,WorkArray,Protocol_Repetitions);
		PropogateProtocol(WorkArray, CPVals_SpaceOpt, LagTimes_SpaceOpt, CPVal_Vector[k], Protocol_Repetitions);
		WriteWorkArray(WorkWrite_SpaceOpt,WorkArray,Protocol_Repetitions);
		PropogateProtocol(WorkArray, CPVals_FullOpt, LagTimes_FullOpt, CPVal_Vector[k], Protocol_Repetitions);
		WriteWorkArray(WorkWrite_Full,WorkArray,Protocol_Repetitions);

		delete CPVals_Naive;
		delete LagTimes_Naive;
		delete CPVals_SpaceOpt;
		delete LagTimes_SpaceOpt;
		delete CPVals_FullOpt;
		delete LagTimes_FullOpt;

	}
	
	delete WorkArray;

}
