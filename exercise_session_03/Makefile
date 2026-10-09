CC=gcc
MPICC=mpicc
CFLAGS=-O3

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

clean:
	rm -f cpi cpi_mpi *.o
