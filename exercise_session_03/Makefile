CC=gcc
MPICC=mpicc
CFLAGS=-O3 -fopenmp
LDFLAGS=-fopenmp

cpi: cpi.o gettime.o
	$(CC) -o cpi cpi.o gettime.o

cpi.o: cpi.c gettime.h
	$(CC) $(CFLAGS) -c cpi.c

gettime.o: gettime.c gettime.h
	$(CC) $(CFLAGS) -c gettime.c

cpi_mpi: cpi_mpi.o gettime.o
	$(MPICC) -o cpi_mpi cpi_mpi.o gettime.o

cpi_mpi.o: cpi_mpi.c gettime.h
	$(MPICC) $(CFLAGS) -c cpi_mpi.c

sum: sum.o gettime.o
	$(CC) $(LDFLAGS) -o sum sum.o gettime.o -lm

sum.o: sum.c gettime.h
	$(CC) $(CFLAGS) -c sum.c

clean:
	rm -f cpi cpi_mpi sum *.o
