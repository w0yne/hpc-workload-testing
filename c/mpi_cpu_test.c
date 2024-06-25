/**
 * Generate by AI
*/
#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to perform heavy computation
void perform_computation(int rank) {
    double x = 0.0001;
    for (int i = 0; i < 1000000000; i++) {
        x += x * x + (double)rank;
    }
    printf("Rank %d: Computation result = %f\n", rank, x);
}

int main(int argc, char *argv[]) {
    int rank, size;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    
    // Time variables to ensure the program runs for approximately 5 minutes
    time_t start_time = time(NULL);
    time_t end_time = start_time + 300; // 300 seconds = 5 minutes
    
    while (time(NULL) < end_time) {
        perform_computation(rank);
    }

    MPI_Finalize();
    return 0;
}
