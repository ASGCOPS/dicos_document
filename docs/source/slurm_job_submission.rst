**********************
Slurm Batch System
**********************

.. sectionauthor:: Mike Yang <mike.yang@twgrid.org>

-------------------------------
Slurm User Interfaces (UIs)
-------------------------------

Slurm users need to login one of the following user interface nodes to use the slurm batch job system.

.. list-table::
   :header-rows: 1

   * - User Interface Nodes
     - OS
     - Purpose
   * - slurm-ui01.twgrid.org
     - CentOS 7
     - Job submission, File download/upload
   * - slurm-ui02.twgrid.org
     - CentOS 7
     - Job submission, File download/upload

* :doc:`Login<slurm_job_submission/slurmui>`

-------------------------------
Slurm Queues and Hardware
-------------------------------

.. list-table::
   :header-rows: 1

   * - Partition
     - Timelimit
     - CPU Cores
     - GPU Boards
     - Nodes
   * - large
     - 14-00:00:0
     - 840
     - N/A
     - 42
   * - long_serial
     - 14-00:00:0
     - 100
     - N/A
     - 5
   * - short
     - 3-00:00:0
     - 1000
     - N/A
     - 50
   * - development
     - 1:00:0
     - 20
     - N/A
     - 1
   * - a100
     - 5-00:00:0
     - 64
     - 8*A100
     - 50
   * - v100
     - 5-00:00:0
     - 48
     - 8*V100
     - 50
   * - amd
     - 5-00:00:0
     - 768
     - N/A
     - 6

.. note::

   The resources are shared with different queues, so some of the resources are mutually exclusive with different queues.


* :doc:`Resources & Specifications<slurm_job_submission/QDR4_intro>`

-------------------------------
Slurm Software
-------------------------------

environment-modules
^^^^^^^^^^^^^^^^^^^^^^

You could use use environment-modules (in ``module`` command) for easy setup of your environment with our predefined configurations. Users could find predefined module by:

.. code-block:: bash

   module avail

Load MPICH2 + gcc48:

.. code-block:: bash

   module load gcc/4.8.5
   module load mpich

Unload all loaded modules:

.. code-block:: bash

   module purge

Load Openmpi + Intel2018:

.. code-block:: bash

   module load intel/2018
   module load openmpi

Load OpenMPI + gcc48:

.. code-block:: bash

   module load gcc/4.8.5
   module load openmpi

.. note::

   ``module`` software tree (version: 20211130a)

   ::

      ── Compiler
      │   ├── gcc
      │   │   ├── 10.3.0
      │   │   ├── 11.1.0
      │   │   ├── 4.6.2
      │   │   ├── 4.8.1
      │   │   ├── 4.8.5
      │   │   │   ├── mpich
      │   │   │   │   └── 3.4.1
      │   │   │   ├── mvapich2
      │   │   │   │   └── 2.3.5
      │   │   │   └── openmpi
      │   │   │       ├── 2.1.6
      │   │   │       └── 4.1.0
      │   │   └── 9.3.0
      │   └── intel
      │       ├── 2017
      │       ├── 2018
      │       │   ├── mpich
      │       │   │   └── 3.4.1
      │       │   ├── mvapich2
      │       │   │   └── 2.3.5
      │       │   └── openmpi
      │       │       ├── 2.1.6
      │       │       └── 4.1.0
      │       └── 2020
      │           ├── lammaps
      │           │   └── jct
      │           │       └── 3Mar2020
      │           ├── lammps
      │           │   └── jct
      │           │       └── 3Mar2020
      │           ├── mpich
      │           │   └── 3.4.1
      │           ├── mvapich2
      │           │   └── 2.3.5
      │           └── openmpi
      │               ├── 2.1.6
      │               ├── 3.1.6
      │               └── 4.1.0
      ├── CompilerMPI
      │   ├── gcc
      │   │   └── 4.8.5
      │   │       └── openmpi
      │   │           ├── 2.1.6
      │   │           │   └── hdf5
      │   │           │       ├── 1.12.0
      │   │           │       └── 1.8.21
      │   │           └── 4.1.0
      │   └── intel
      │       └── 2020
      │           └── openmpi
      │               ├── 2.1.6
      │               ├── 3.1.6
      │               └── 4.1.0
      ├── Core
      │   ├── app
      │   │   ├── anaconda3
      │   │   │   ├── 4.10.3
      │   │   │   └── 4.9.2
      │   │   ├── binutils
      │   │   │   └── 2.35.2
      │   │   ├── cmake
      │   │   │   └── 3.20.3
      │   │   ├── make
      │   │   │   └── 4.3
      │   │   └── root
      │   │       └── 6.24
      │   ├── gcc
      │   │   ├── 10.3.0
      │   │   ├── 11.1.0
      │   │   ├── 4.8.5
      │   │   └── 9.3.0
      │   ├── glibc
      │   ├── intel
      │   │   ├── 2017
      │   │   ├── 2018
      │   │   └── 2020
      │   ├── nvhpc_sdk
      │   │   └── 20.11
      │   ├── pgi -> nvhpc_sdk/
      │   └── python
      │       └── 3.9.5
      └── VERSION



.. seealso::

   * `environment-modules <https://modules.readthedocs.io/en/latest/index.html>`_


ssinfo
^^^^^^^^^^

``ssinfo`` is made by DiCOS administrator, and available in **slurm-ui**. It could help users to know some system informations, including accounting, news, and documentation, etc.

* Show document of slurm

.. code-block:: bash

   ssinfo docu

* Show personal information on QDR4 cluster

.. code-block:: bash

   ssinfo me

* Show news of slurm and DiCOS

.. code-block:: bash

   ssinfo news

* Show current slurm information

.. code-block:: bash

   ssinfo slurm
  
* Show module tree and dependencies

.. code-block:: bash

   ssinfo modules


CVMFS
^^^^^^^^

CVMFS represented for CernVM-FS. It's originally used in the grid computing, and try to deliver the updated software for the computation. The file system is read-only, so it is very suitable for the software delivery. In DiCOS system, CVMFS file system is for the software repository for users, and mounted in ``/cvmfs``. The ``modules`` environment in slurm system help user to setup the environment for specifically software, and the software is located in CVMFS.

.. seealso::

   * https://cernvm.cern.ch/fs/

Docs
^^^^^^^^

* :doc:`MPI / Compilers / Software and Libraries <slurm_job_submission/software>`

-------------------------------
Slurm Tutorials
-------------------------------

* :doc:`Tutorial<slurm_job_submission/slurm_docs>`

-------------------------------------------
Request for Specific Software Installation
-------------------------------------------

If you have special requirement for the software installation, please contact to DiCOS-Support@twgrid.org.

