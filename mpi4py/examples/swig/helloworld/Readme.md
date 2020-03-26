### wrapping mpi4py with swig

Here I use swig to wrap C++ code and make a `.so` file to import in python script.

```sh
$ mpirun -n 4 python3 runme.py 
Hello, World! I am process 0 of 4.
Hello, World! I am process 1 of 4.
Hello, World! I am process 2 of 4.
Hello, World! I am process 3 of 4.
```