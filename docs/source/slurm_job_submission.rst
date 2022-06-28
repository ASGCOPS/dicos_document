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

* :doc:`Resources & Specifications<slurm_job_submission/QDR4_intro>`

-------------------------------
Slurm Software
-------------------------------

* modules
* ssinfo
* CVMFS

* :doc:`MPI / Compilers / software & libraries <slurm_job_submission/available_software>`

-------------------------------
Slurm Tutorials
-------------------------------

* :doc:`Tutorial<slurm_job_submission/slurm_docs>`

-------------------------------------------
Request for specific software installation
-------------------------------------------

If you have special requirement for the software installation, please contact to DiCOS-Support@twgrid.org
