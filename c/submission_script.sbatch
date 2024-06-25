#!/bin/bash
#SBATCH --job-name=mpi_cpu_test
#SBATCH --ntasks=20
#SBATCH --output=%x_%j.out

mpirun ./mpi_cpu_test
