DiCOSAPP Introduction
=========================

======================
DiCOSAPP introduction
======================

DiCOSAPP is web based micro-service that handles different application individually. Here is the page to introduce its SPEC for each APP.

------------------------
CryoEM specific APPs
------------------------

.. list-table:: CryoEM specific APPs
   :header-rows: 1

   * - APP name
     - CPU cores
     - GPU
     - Memory
     - SSD
   * - CisTEM
     - 32
     - 0
     - 100GB
     - no
   * - RELION3
     - 16
     - 4 (1080Ti)
     - 380GB
     - yes
   * - RELION2
     - 16
     - 4 (1080Ti)
     - 380GB
     - yes
   * - CisTEM-cluster
     - 40 per job, max to 600
     - 0
     - 256GB ~ 3840GB
     - no
   * - CryoSPARC(*no longer up2date*)
     - 16
     - 1 (1080Ti)
     - 380GB
     - yes

------------------------
Jupyter Notebooks
------------------------

.. list-table:: Jupyter Notebooks
   :header-rows: 1

   * - APP name
     - CPU coures
     - GPU
     - Memory
     - SSD
   * - JupyterLab(CPU)
     - 12
     - 0
     - 64GB
     - yes
   * - JupyterLab(GPU)
     - 12
     - 1 (P100)
     - 128GB
     - yes

