FDR5 Resources and Specifications
===================================

================
FDR5 Cluster
================

* 92 homogeneous worker nodes(2208 CPU cores) are available in FDR5.

-----------------------------------
## The Specifications per nodes:
-----------------------------------

* CPU Model: Intel(R) Xeon(R) CPU E5-2650 v4 @ 2.20GHz
* CPU Number: 24 (12 Core per socket, 2 sockets)
* Memory Size: 125 GB
* Disk Space: 1.8 TB

======================
# System Topography
======================
* The system scheme could be found in Figure. 1. The network connection is majorly in 10G ethernet.

    [image:108 align:left]

-----------------------------------------------------
## Software Repositories (same in DiCOS clusters)
-----------------------------------------------------

::

    /cvmfs/cvmfs.grid.sinica.edu.tw/

-----------------------------------------------------
## Ceph File System
-----------------------------------------------------

::

    /ceph/sharedfs/groups/<groupname>
    /ceph/sharedfs/users/<initial>/<username>
    (/ceph/astro_phys/ is for AstroPhysics group)

==========================================================
# User Interface for job management and data access
==========================================================

::

    ssh <dicos account>@condor-ui01.twgrid.org

==========================================================
# User working directories
==========================================================

User Home
^^^^^^^^^^^
It's your home directory in UI. Data access is be limited with NFS system 10Gb/s.

::

    /dicos_ui_home/<your dicos account>/

Ceph User Working Directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Strongly recommended for its high performance of data access for inputs/outputs. Please follow the first letter order to find your Ceph working directory. For example, username 'jack' will be in /ceph/sharedfs/users/j/jack.

::

    /ceph/sharedfs/users/<initial>/<your dicos account>
    (etc, for user "jack" /ceph/sharedfs/users/j/jack)


==========================================================
# Condor Queue Policy
==========================================================

* Below is our current configuration of partitions (Condor JobFlavour (queue) policy):

  .. image:: image/condor_queue_policy.jpg


