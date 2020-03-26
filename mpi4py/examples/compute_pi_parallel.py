from mpi4py import MPI
import numpy as np 
import math
import sys
from time import time


def compute_pi(n, start=0, step=1):
    h = 1.0 / n
    s = 0.0

    for i in range(start, n, step):
        x = h * (i + 0.5)
        s += 4.0 / (1.0 + x * x)
    
    return s * h



def main(num_steps=10):

    comm = MPI.COMM_WORLD
    nprocs = comm.Get_size()
    myrank = comm.Get_rank()

    t1 = 0.0

    if myrank == 0:
        n = num_steps
        t1 = MPI.Wtime()
    else:
        n = None

    n = comm.bcast(n, root=0)
    mypi = compute_pi(n, myrank, nprocs)
    pi = comm.reduce(mypi, op=MPI.SUM, root=0)

    if myrank == 0:
        error = abs(pi - math.pi)
        print("pi is approximately %.16f, "
            "error is %.16f" % (pi, error))
        t2 = MPI.Wtime()
        print("elapsed time is %10.4f:" % (t2 - t1))


if __name__ == "__main__":

    assert len(sys.argv)>1, "calling e.g : python filename.py 10"
    main(int(sys.argv[1]))
    
    




