#MAKEFILE for Nonequilbirium Propogator routine
#
#Steven Large
#JApril 5th 2018

PRODUCT_NEQ = NoneqPropogator.exe

ODIR = obj
LDIR = lib
IDIR = include
SDIR = src

MAINFILE_NEQ = $(SDIR)/Nonequilibrium_Protocol.cpp

SOURCES_NEQ = $(SDIR)/Propogator.cpp
LIBRARIES_NEQ = $(LDIR)/ReadWrite.cpp
LIBRARIES_NEQ_2 = $(LDIR)/Numerics.cpp
OBJECTS_NEQ = $(SDIR)/$(ODIR)/Propogator.o
OBJECTS_NEQ_LIB = $(SDIR)/$(ODIR)/ReadWrite.o
OBJECTS_NEQ_LIB_2 = $(SDIR)/$(ODIR)/Numerics.o

CFLAGS = -I.

DEPS_NEQ = $(IDIR)/DiscreteControl.h $(IDIR)/ReadWrite.h $(IDIR)/Numerics.h

CC = g++ -std=c++11 -O3

all: $(PRODUCT_NEQ) $(PRODUCT_EQ)

$(OBJECTS_NEQ): $(SOURCES_NEQ)
	$(CC) -c $(SOURCES_NEQ) -o $(OBJECTS_NEQ) $(CFLAGS)

$(OBJECTS_NEQ_LIB): $(LIBRARIES_NEQ)
	$(CC) -c $(LIBRARIES_NEQ) -o $(OBJECTS_NEQ_LIB) $(CFLAGS) 

$(OBJECTS_NEQ_LIB_2): $(LIBRARIES_NEQ_2)
	$(CC) -c $(LIBRARIES_NEQ_2) -o $(OBJECTS_NEQ_LIB_2) $(CFLAGS)

$(PRODUCT_NEQ): $(MAINFILE_NEQ) $(OBJECTS_NEQ) $(OBJECTS_NEQ_LIB) $(OBJECTS_NEQ_LIB_2) $(DEPS_NEQ)
	$(CC) $(MAINFILE_NEQ) $(OBJECTS_NEQ) $(OBJECTS_NEQ_LIB) $(OBJECTS_NEQ_LIB_2) -o $(PRODUCT_NEQ) $(CFLAGS)



clean:
	rm -f $(SDIR)/$(ODIR)/*.o
	rm *.exe

clean_ex:
	rm *.exe

