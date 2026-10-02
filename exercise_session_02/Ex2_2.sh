#!/bin/bash
mpicc 2> mpicc_error.txt
module load cray-mpich
mpicc > mpicc_loaded.txt
