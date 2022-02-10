DiCOSAPP Data Handling
=========================

The DiCOSAPP is ephemeral and isolated application, everything changed or created in APP will be wiped out after the APP is terminated. However, there are three persistent spaces, everything storing there will be kept:

**NOTICE: The CryoEM data from ASCEM to ASGC will be stored at /cryoEM/tmp**

==========================
1. User HOME space
==========================

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

========================================
2. DiCOSBOX(Cloud storage) space
========================================

- DiCOSBOX is Dropbox-like storage, it is also connected inside the APP by following path:
::

   - ~/DiCOSBox
   - $HOME/DiCOSBox
   - /dicos_ui_home/[ your username ]/DiCOSBox

- DiCOSBOX can be also accessible from outside APP by login to following page:

  * https://dicosbox.twgrid.org

==================================================
3. CryoEM group space (CryoEM user only)
==================================================

- CryoEM group space is for CryoEM user only, which must be requested by PI.
- CryoEM group space is connected inside the APP by following path:

::

   - /cryoEM/

- All data in CryoEM group space can be also accessible from outside APP by sftp( using `filezilla <https://filezilla-project.org/download.php>`_ or sftp client) with following endpoints:

::

   - dicos-ui02.grid.sinica.edu.tw
   - dicos-ui04.grid.sinica.edu.tw

- The path is also */cryoEM/*
