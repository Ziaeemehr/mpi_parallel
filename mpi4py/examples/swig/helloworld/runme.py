from mpi4py import MPI
import helloworld

helloworld.sayhello(MPI.COMM_WORLD)
# Hello, World! I am process 0 of 1.