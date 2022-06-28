************
DiCOSApps
************

* :doc:`DiCOS APP FAQ<dicos/dicosapp_faq>`

   - :doc:`Introduction and Specs<dicos/dicosapp_faq/dicosapp>`
   - :doc:`Data handling with DiCOS Apps<dicos/dicosapp_faq/dicos_app_data_handling>`
   - :doc:`RELION job configuration<dicos/dicosapp_faq/relion_job_configuration>`

======================
DiCOSAPP Introduction
======================

DiCOSAPP is web based micro-service that handles different application individually. Here is the page to introduce its SPEC for each APP.

------------------------
CryoEM Specific APPs
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



=========================
DiCOSAPP Data Handling
=========================

The DiCOSAPP is ephemeral and isolated application, everything changed or created in APP will be wiped out after the APP is terminated. However, there are three persistent spaces, everything storing there will be kept:

**NOTICE: The CryoEM data from ASCEM to ASGC will be stored at /cryoEM/tmp**

--------------------------
1. User HOME space
--------------------------

- The user home space is connected inside the APP by following paths:

::

   -  ~/data/
   -  $HOME/data
   -  /dicos_ui_home/[ your username ]/data

- **Please note, the user home space doesn't guarantee any data protection or space for every user. So, please be careful what you store on it. And please make backup by yourself, if you will only use home space.**

- All data in user home space can be also accessible from outside APP by sftp (using `filezilla <https://filezilla-project.org/download.php>`_ or sftp client) with following endpoints:

::

   - dicos-ui02.grid.sinica.edu.tw
   - dicos-ui04.grid.sinica.edu.tw

------------------------------------
2. DiCOSBOX(Cloud storage) space
------------------------------------

- DiCOSBOX is Dropbox-like storage, it is also connected inside the APP by following path:
::

   - ~/DiCOSBox
   - $HOME/DiCOSBox
   - /dicos_ui_home/[ your username ]/DiCOSBox

- DiCOSBOX can be also accessible from outside APP by login to following page:

  * https://dicosbox.twgrid.org

------------------------------------------------
3. CryoEM group space (CryoEM user only)
------------------------------------------------

- CryoEM group space is for CryoEM user only, which must be requested by PI.
- CryoEM group space is connected inside the APP by following path:

::

   - /cryoEM/

- All data in CryoEM group space can be also accessible from outside APP by sftp( using `filezilla <https://filezilla-project.org/download.php>`_ or sftp client) with following endpoints:

::

   - dicos-ui02.grid.sinica.edu.tw
   - dicos-ui04.grid.sinica.edu.tw

- The path is also */cryoEM/*



How to Use 
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Request for Specific Application Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have special requirement for the application installation, please contact to DiCOS-Support@twgrid.org.
