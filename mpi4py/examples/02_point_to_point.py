# Point-to-Point Communication

from mpi4py import MPI
import numpy as np

# Now we will look at how to pass data from one process to another. Here is a very simple example where we pass a dictionary from process 0 to process 1:

def send_dict():
    """
    sending a dictionaty by comm.send
    """

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    if rank == 0:
        data = {'a': 7, 'b': 3.14}
        comm.send(data, dest=1)
    elif rank == 1:
        data = comm.recv(source=0)
        print("On process1, data is ", data)

    # Note how comm.send and comm.recv have lower case s and r.


#*******************************************************************#
# Now let's look at a more complex example where we send a numpy array:


def send_numpy_array():
    """
    sending numpy array 
    """

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    if rank == 0:
        # in real code, this section might
        # read in data parameters from a file
        num_data = 5
        comm.send(num_data, dest=1)

        data = np.linspace(0.0, 2, num_data)
        comm.Send(data, dest=1)

    elif rank == 1:

        num_data = comm.recv(source=0)
        print('Number of data to receive: ', num_data)

        # allocate space to receive the array
        data = np.empty(num_data, dtype='d')
        comm.Recv(data, source=0)

        print('data received: ', data)

    # Note how comm.Send and comm.Recv used to send and receive the numpy array have upper case S and R.


# send_dict()
send_numpy_array()


"""
mpirun -n 2 python3 point_to_point.py  
On process1, data is  {'a': 7, 'b': 3.14}
"""
