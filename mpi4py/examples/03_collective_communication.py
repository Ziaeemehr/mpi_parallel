# Collective Communication

from mpi4py import MPI
import numpy as np

# Broadcasting takes a variable and sends an exact copy of it to all processes on a communicator. Here are some examples:

# Broadcasting a dictionary:


def broadcast_dict():

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    if rank == 0:
        data = {'key1': [1, 2, 3],
                'key2': ('abc', 'xyz')}
    else:
        data = None

    data = comm.bcast(data, root=0)
    print("Rank: ", rank, ', data: ', data)


def broadcast_array():

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    if rank == 0:
        # create a data array on process 0
        # in real code, this section might
        # read in data parameters from a file
        num_data = 5
        data = np.linspace(0, 2, num_data)
    else:
        num_data = None

    # broadcast num_data and allocate array on other ranks:

    num_data = comm.bcast(num_data, root=0)
    if rank != 0:
        data = np.empty(num_data, dtype='d')

    # broadcast the array from rank 0 to all others
    comm.Bcast(data, root=0)
    print("Rank: ", rank, ", data received: ", data)



if __name__ == "__main__":

    # broadcast_dict()

    """
    mpirun -n 4 python3 collective_communication.py 
    Rank:  0 , data:  {'key1': [1, 2, 3], 'key2': ('abc', 'xyz')}
    Rank:  2 , data:  {'key1': [1, 2, 3], 'key2': ('abc', 'xyz')}
    Rank:  1 , data:  {'key1': [1, 2, 3], 'key2': ('abc', 'xyz')}
    Rank:  3 , data:  {'key1': [1, 2, 3], 'key2': ('abc', 'xyz')}
    """

    broadcast_array()

    """
    Rank:  0 , data received:  [0.  0.5 1.  1.5 2. ]
    Rank:  1 , data received:  [0.  0.5 1.  1.5 2. ]
    Rank:  2 , data received:  [0.  0.5 1.  1.5 2. ]
    Rank:  3 , data received:  [0.  0.5 1.  1.5 2. ]

    """
