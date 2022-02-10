Computing Resources and Specifications
===========================================

=================
QDR4 Cluster
=================
* 50 homogeneous worker nodes(1000 CPU cores) are available in QDR4.
* The Specifications per nodes:
  - CPU Model: Intel(R) Xeon(R) CPU E5-2650L v2 @ 1.70GHz
  - CPU Number: 20 (10 Core per socket, 2 sockets)
  - Memory Size: 125 GB
  - Disk Space: 1 TB (400 GB reserved for system)
* The connections between each worker nodes and controller node
  - InfiniBand QDR standard, which provide high
speed and low latency connections.

==================
GPU Resources
==================

-------
# V100
-------

* Specifications
  - CPU Model : Intel(R) Xeon(R) Gold 6126 CPU
  - CPU MHz : 2600
  - CPU Cores: 24
  - Memory Size: 755GB
  - Memory Spec: 32GB 2666 MT/s DDR4
  - GPU Spec : NVIDIA Data center GPU V100
  - Disk Space : 1TB (400 GB reserved for system)

-------
# A100
-------

* Specifications
  - CPU Model : AMD EPYC 7302 16-Core Processor
  - CPU MHz : 2994.281
  - CPU Cores: 32
  - Memory Size : 1TB
  - Memory Spec : 64GB 3200 MT/s DDR4
  - GPU Spec : HGX NVIDIA A100 * 8
  - Disk Space : 1.1TB (400 GB reserved for system)

===================
SLURM Queue Policy
===================

* Below is our current configuration of partitions

   .. image:: image/slurm_queue_policy.png

===================
System Topography
===================

* The system scheme could be found in Figure. 1. The network connection is majorly in 10G ethernet.

   .. image:: image/qdr4_topology.png

----------------------
Software Repositories
----------------------

::

    /cvmfs/cvmfs.grid.sinica.edu.tw/


------------------------------------------
Ceph File System (掛載至QDR4: 1 PB)
------------------------------------------

::

    /ceph/sharedfs/groups/<groupname>
    /ceph/sharedfs/users/<initial>/<username>
    (/ceph/astro_phys/ is for AstroPhysics group)

=====================================================
# User Interface for job management and data access
=====================================================

::

    ssh <dicos account>@slurm-ui01.twgrid.org

=====================================================
User working directories
=====================================================

------------------------------------------
User Home
------------------------------------------

It's your home directory in UI. Data access is be limited with NFS system 10Gb/s.

::

    /dicos_ui_home/<your dicos account>/


------------------------------------------
Ceph User Working Directory
------------------------------------------

Strongly recommended for its high performance of data access for inputs/outputs. Please follow the first letter order to find your Ceph working directory. For example, username 'jack' will be in /ceph/sharedfs/users/j/jack.

::

    /ceph/sharedfs/users/<initial>/<your dicos account>
    (etc, for user "jack" /ceph/sharedfs/users/j/jack)

