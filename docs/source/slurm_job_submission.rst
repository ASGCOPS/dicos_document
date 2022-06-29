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

.. note::

   * The resources of the user interface node is limited, please don't run your jobs in the user interfaces, or your jobs will be killed without notice.

   * To avoid ssh password guessing attack, IP addresses with multiple login failures in a short time will be banned for hours.

   * Installed GUI software in UIs for users to preview files. Please use, for example:

     .. code-block:: bash

        ssh -XY <your_account>@dicos-ui05.grid.sinica.edu.tw

     to login in the UI with X11 forwarding enabled. If you are using Windows system, please install and execute `Xming <https://sourceforge.net/projects/xming/>`_ before connect to the UI.

     .. list-table::
        :header-rows: 1
     
        * - Software
          - Filetype
        * - `eog <https://wiki.gnome.org/Apps/EyeOfGnome>`_
          - images
        * - `xpdf <https://www.xpdfreader.com/>`_
          - pdf files

-------------------------------
Slurm Resources and Queues
-------------------------------

.. list-table:: Slurm Resources 2022-06-27
   :header-rows: 1

   * - Cluster
     - Worker Nodes
     - Total CPU cores
     - CPU/node
     - CPU model
     - Memory/node
     - Disk space/node
     - Network
     - GPU model
     - GPU/node
   * - HPC_FDR5
     - 92
     - 2208
     - 24
     - Intel(R) Xeon(R) CPU E5-2650 v4 @ 2.20GHz
     - 125GB
     - 2TB (System: 400GB)
     - 10GbE
     - N/A
     - N/A
   * - HPC_HDR1
     - 2
     - 768
     - 128
     - AMD EPYC 7662 64-Core Processor
     - 1520GB
     - 1TB (System: 20GB)
     - 100GbE
     - N/A
     - N/A
   * - GPU_V100
     - 1
     - 48
     - 48
     - Intel(R) Xeon(R) Gold 6126 CPU @ 2.60GHz
     - 768GB
     - 1TB (System: 20GB)
     - 10GbE
     - V100
     - 8
   * - GPU_A100
     - 1
     - 64
     - 64
     - AMD EPYC 7302 16-Core Processor
     - 1024GB
     - 1TB (System: 20GB)
     - 100GbE
     - A100
     - 8
     

.. list-table:: Slurm Partitions 2022-06-27
   :header-rows: 1

   * - Partition
     - Timelimit
     - CPU Cores
     - GPU Boards
     - Nodes
     - Resource
   * - large
     - 14-00:00:0
     - 840
     - N/A
     - 42
     - QDR4
   * - long_serial
     - 14-00:00:0
     - 100
     - N/A
     - 5
     - QDR4
   * - short
     - 3-00:00:0
     - 1000
     - N/A
     - 50
     - QDR4
   * - development
     - 1:00:0
     - 20
     - N/A
     - 1
     - QDR4
   * - a100
     - 5-00:00:0
     - 64
     - 8*A100
     - 50
     - A100
   * - v100
     - 5-00:00:0
     - 48
     - 8*V100
     - 50
     - V100
   * - amd
     - 5-00:00:0
     - 768
     - N/A
     - 6
     - HDR1

.. note::

   The resources are shared with different queues, so some of the resources are mutually exclusive with different queues.


-------------------
System Topography
-------------------

* The system scheme could be found in the following image. The network connection is majorly in 10G ethernet.

  .. image:: image/qdr4_topology.png

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

   * `CernVM-FS <https://cernvm.cern.ch/fs/>`_

Docs
^^^^^^^^

* :doc:`MPI / Compilers / Software and Libraries <slurm_job_submission/software>`

-------------------------------
Slurm Tutorials
-------------------------------

* :doc:`Tutorial<slurm_job_submission/slurm_docs>`

-------------------------
On Site Slurm Documents
-------------------------

User documents for SLURM are located in

::

    /ceph/astro_phys/user_document/

Create a working directory, assume it as mpi_work in your HOME directory. Copy all the scripts from the following directory to start.

::

    /ceph/astro_phys/user_document/scripts/*


-------------------------------------------
Request for Specific Software Installation
-------------------------------------------

If you have special requirement for the software installation, please contact to DiCOS-Support@twgrid.org.

