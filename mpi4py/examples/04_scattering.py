from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()  # new: gives number of ranks in comm
rank = comm.Get_rank()

numDataPerRank = 10
data = None
if rank == 0:
    data = np.linspace(1, size*numDataPerRank, numDataPerRank*size)
    # when size=4 (using -n 4), data = [1.0:40.0]

recvbuf = np.empty(numDataPerRank, dtype='d')  # allocate space for recvbuf
comm.Scatter(data, recvbuf, root=0)

print('Rank: ', rank, ', recvbuf received: ', recvbuf)

# In this example, the rank 0 process created the array data. Since this is just a toy example, we made data be a simple linspace array, but in a research code the data might have been read in from a file, or generated by a previous part of the workflow. data is then scattered to all the ranks (including rank 0) using comm.Scatter. Note that we first had to initialize (or allocate) the receiving buffer array recvbuf.