swig -c++ -python helloworld.i  
mpiCC  -O2 -fPIC -c helloworld_wrap.cxx -I /usr/include/python3.6 -I /usr/local/lib/python3.6/dist-packages/mpi4py/include
mpiCC  -shared helloworld_wrap.o -o _helloworld.so 
