/* This C++ file contains the Protocol read/write routines */

//#include "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/lib/DiscreteControl.h" 			//This is the Discrete control header file, containing function prototypes

#include "include/ReadWrite.h"

#include <fstream>
#include <iostream>
#include <random>
#include <cmath>
#include <string>
#include <ctime>

using namespace std;

void ImportProtocol(double * CPVals, double * LagTimes, int NumCPVals, int TotalTime, int FLAG){

	string ImportName;

	if(FLAG == 0){
		//ImportName = "Protocols_Feb12/Naive_CP" + std::to_string(NumCPVals) + "_T" + std::to_string(TotalTime) + ".dat";
		ImportName = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/NonEquilibrium_Cluster/Protocols/Naive_CP" + std::to_string(NumCPVals) + "_T" + std::to_string(TotalTime) + ".dat";
	}
	else{
		//ImportName = "Protocols_Feb12/TimeOpt_CP" + std::to_string(NumCPVals) + "_T" + std::to_string(TotalTime) + ".dat";
		ImportName = "/Users/stevelarge/Research/DiscreteControl/LinkedCode_CPP/NonEquilibrium_Cluster/Protocols/TimeOpt_CP" + std::to_string(NumCPVals) + "_T" + std::to_string(TotalTime) + ".dat";
	} 

	std::ifstream ReadFile;

	ReadFile.open(ImportName);

	for(int counter = 0 ; counter < NumCPVals ; counter++){
		ReadFile >> CPVals[counter] >> LagTimes[counter];
	}

	ReadFile.close();
	
}

void ImportProtocol_String(double * CPVals, double * LagTimes, int NumCPVals, string ImportName){

	std::ifstream ReadFile;

	ReadFile.open(ImportName);

	for(int counter = 0 ; counter < NumCPVals ; counter ++){
		ReadFile >> CPVals[counter] >> LagTimes[counter];
	}

	ReadFile.close();

}

void WriteWorkArray(string WriteName, double * Work, int Protocol_Repetitions){

	std::ofstream WriteFile;

	WriteFile.open(WriteName);

	for(int k = 0; k < Protocol_Repetitions; k++){
		WriteFile << std::to_string(Work[k]) << "\n";
	}

	WriteFile.close();

}

