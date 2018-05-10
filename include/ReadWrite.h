/* This is a header file for the Discrete Control Nonequilbrium simulations pertaining to protocol read-in */

#include <string>

void ImportProtocol(double * CPVals, double * LagTimes, int NumCPVals, int TotalTime, int FLAG=0);
void ImportProtocol_String(double * CPVals, double * LagTimes, int NumCPVals, std::string FileName);
void WriteWorkArray(std::string WriteName, double * Work, int Repetitions);

