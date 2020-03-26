# Communicators and Ranks

from mpi4py import MPI

rank = MPI.COMM_WORLD.Get_rank()
size = MPI.COMM_WORLD.Get_size()
name = MPI.Get_processor_name()
print("My rank is: ", rank)

if rank == 0:
    print("size : ", size)
    print("name : ", name)


"""
mpirun -n 4 python3 01_comm.py

output:

My rank is:  0
size :  4
name :  abolfazl
My rank is:  1
My rank is:  2
My rank is:  3

"""