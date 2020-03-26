# Communicators and Ranks

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print("My rank is ", rank)


"""
mpirun -n 4 python3 comm.py

output:

My rank is  1
My rank is  3
My rank is  0
My rank is  2

"""