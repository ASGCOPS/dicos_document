********************
Available Software
********************

=================================
Module toolkit to load software
=================================

To check available modules(softwares) and its version

.. code-block:: bash

   $ module avail

To clear the environment from any previously loaded modules

.. code-block:: bash

   $ module purge

To load intel or gcc compiler


.. code-block:: bash

   $ module load intel/2018
   $ module load gcc/


==================
MPI
==================

User can always find MPI libraries in the following path:

::

    /cvmfs/cvmfs.grid.sinica.edu.tw/hpc/mpi/

To setup mpi environment, please source setup script at following path:

::

    /cvmfs/cvmfs.grid.sinica.edu.tw/hpc/mpi/scripts/

You should be able to find various mpi version there. If you don't what you need, please contact us.

==================
Compilers
==================

User can always find different compiler at following path:

::

    /cvmfs/cvmfs.grid.sinica.edu.tw/hpc/compiler/

To setup compiler environment, please source specific setup script at following path:

::

    /cvmfs/cvmfs.grid.sinica.edu.tw/hpc/compiler/scripts/


===================================
Scientific Software and Libraries
===================================

Some specific scientific softwares and libraries will be installed at following path:

::

    /cvmfs/cvmfs.grid.sinica.edu.tw/twgrid/

User can always find a setup script: setup.sh at software directory respectively. To setup specific software/libraries environment, simply source those setup.sh to activate it:

.. code-block:: bash

    source /cvmfs/cvmfs.grid.sinica.edu.tw/twgrid/<software name>/setup.sh

If you don't find software you need, please contact our dicos support team. We will try to install those software for you.

