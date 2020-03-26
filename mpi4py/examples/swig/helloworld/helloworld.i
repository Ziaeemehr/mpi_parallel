// file: helloworld.i
%module helloworld

%{
#include "helloworld.hpp"
%}

%include /usr/local/lib/python3.6/dist-packages/mpi4py/include/mpi4py/mpi4py.i
%mpi4py_typemap(Comm, MPI_Comm);

%include "helloworld.hpp"