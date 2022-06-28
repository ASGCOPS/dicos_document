****************************
Data Storage and Transfer
****************************

======================================
User/Group Spaces in DiCOS System
======================================

----------------------
DiCOS UI Home
----------------------

::

   /dicos_ui_home/jack

------------------------
User Working Directory
------------------------

::

   /ceph/sharedfs/users/j/jack

------------------------
Group Working Directory
------------------------

::

   /ceph/sharedfs/groups/jack_group


======================================
Different Types of Storage in DiCOS
======================================

----------------------
File output (EOS)
----------------------

----------------------
Cloud Storage (Ceph)
----------------------

* :doc:`Tutorial <dicos_ddm/dicos_cloud_se>`

----------------------
CVMFS
----------------------

----------
DiCOSBox
----------

* :doc:`Tutorial <dicos_ddm/dicosbox>`

==================================
Transfer data from/to DiCOS
==================================

------------------
scp (command line)
------------------

If your are Linux or Mac users, just simply open a terminal with command line interface and use ``scp`` to copy the files/directories between the DiCOS UI and your computer. For users using newer Windows system, you could use `WSL2 <https://docs.microsoft.com/en-us/windows/wsl/install>` to open a terminal.

For example:

.. code-block:: bash

   # Copy my_result.txt from the DiCOS UI home to local directory
   scp jack@dicos-ui05.grid.sinica.edu.tw:my_result.txt /home/jack

   # Copy my_input.txt from my computer to DiCOS UI home
   scp my_input.txt jack@dicos-ui05.grid.sinica.edu.tw:

--------------------------------
filezilla (Windows/MacOS/Linux)
--------------------------------

`FileZilla <https://filezilla-project.org/>`_ have file manager like UI. Connect to our UI with your DiCOS account, and the left panel will show the files in the UI, then you could go ahead with the download/upload.

.. seealso::

   * `filezilla <https://filezilla-project.org/>`_

-------------------------
MobaXterm (Windows)
-------------------------

`MobaXterm <https://mobaxterm.mobatek.net/>`_ has a built-in function for SFTP. Connect to our UI with your DiCOS account, and the left panel will show the files in the UI, then you could go ahead with the download/upload.

.. seealso::

   * `MobaXterm <https://mobaxterm.mobatek.net/>`_

-------------------------
winscp (Windows)
-------------------------

`WinSCP <https://winscp.net/eng/index.php>`_ and `FileZilla <https://filezilla-project.org/>`_ have file manager like UI. You could install one of them and login with SFTP/SCP protocol to our user interface, then you could drag to copy your files/directories between the UI and your computer.

.. seealso::

   * `winscp <https://winscp.net/eng/index.php>`_
