****************************
Data Storage and Transfer
****************************

======================================
User/Group Spaces in DiCOS System
======================================

----------------------
DiCOS UI Home (NFS)
----------------------

When you login in ``dicos_ui`` or ``slurm_ui``, you are in your DiCOS UI home. For example, if your username is ``jack``, then you will be in ``/dicos_ui_home/jack``. You could store some files or data for your convenience. However, because the storage of DiCOS UI home is a NFS mount, it will have some performance issue. Besides, we didn't guarantee the data preservation in the DiCOS UI home. So, you are recommended to use ceph working directory for your long-term storage.

.. important::

   * Please be advised that we do not guarantee the data preservation in your home directory. Please backup your data in the home directory by yourself, or use the ceph working directory for your storage.

-------------------------------
User Working Directory (Ceph)
-------------------------------

For better performance and data preservation, DiCOS users are provided with a dedicated working directory. The working directory is mounted in a **ceph** storage pool. We recommend DiCOS users to use the ceph working directory for their job calculations and I/Os. If your username is ``jack``, then the working directory will be in ``/ceph/sharedfs/users/j/jack``. The information will be shown when you login in the ``slurm_ui``.

--------------------------------
Group Working Directory (Ceph)
--------------------------------

For the data sharing among the group collaboration, user could make use of the group working directory for data sharing. Only group members could access to the group working directory. For example, the group working directory will be in ``/ceph/sharedfs/groups/<group_name>``

======================================
Different Types of Storage in DiCOS
======================================

----------------------
File Output (EOS)
----------------------

An EOS file system in ASGC is used as the output staging area for the jobs from ``dicos job submit``. With the DiCOS command line tools, the staging area is transparent to users. The EOS filesystem was adopted because the ``dicos job submit`` is originated from the grid system. EOS is capable for the authentication and authroization for a grid users with the grid security infrastructure (GSI). Basically, general users could skip this session.

.. seealso::

   * `EOS <https://eos-web.web.cern.ch/eos-web/>`_

----------------------
Cloud Storage (Ceph)
----------------------

Ceph pool in DiCOS system plays an important role. In general, ceph provides capability with more intensive I/O operations and loading sharing with multiple machines. Therefore, DiCOS users are encouraged to use the ceph storage for the data I/O and storage. 

.. seealso::

   * `Ceph <https://docs.ceph.com/>`_

----------------------
CernVM-FS (CVMFS)
----------------------

CVMFS represented for CernVM-FS. It's originally used in the grid computing, and try to deliver the updated software for the computation. The file system is read-only, so it is very suitable for the software delivery. In DiCOS system, CVMFS file system is for the software repository for users, and mounted in ``/cvmfs``. The ``modules`` environment in slurm system help user to setup the environment for specifically software, and the software is located in CVMFS.

.. seealso::

   * `CernVM-FS <https://cernvm.cern.ch/fs/>`_

----------
DiCOSBox
----------

`DiCOSBox <https://dicosbox.twgrid.org/>`_ is derived from `CERNBox <https://swan.docs.cern.ch/intro/cernbox/>`_, which is a `Dropbox™ <https://www.dropbox.com>`_-like cloud storage system. DiCOS users could use DiCOSBox to share data/files to the collaborators seamlessly through the sharing web URL.

.. note::

   Currently, for each DiCOS user, the quota limit is 2GB.

.. seealso::

   * `DiCOSBox <https://dicosbox.twgrid.org/>`_

==================================
Transfer data from/to DiCOS
==================================

-------------------
scp (command line)
-------------------

If your are Linux or Mac users, just simply open a terminal with command line interface and use ``scp`` to copy the files/directories between the DiCOS UI and your computer. For users using newer Windows system, you could use `WSL2 <https://docs.microsoft.com/en-us/windows/wsl/install>` to open a terminal.

For example:

.. code-block:: bash

   # Copy my_result.txt from the DiCOS UI home to local directory
   scp jack@dicos-ui05.grid.sinica.edu.tw:my_result.txt /home/jack

   # Copy my_input.txt from my computer to DiCOS UI home
   scp my_input.txt jack@dicos-ui05.grid.sinica.edu.tw:

--------------------------------
filezilla™ (Windows/MacOS/Linux)
--------------------------------

`FileZilla™ <https://filezilla-project.org/>`_ have file manager like UI. Connect to our UI with your DiCOS account, and the left panel will show the files in the UI, then you could go ahead with the download/upload.

.. seealso::

   * `filezilla™ <https://filezilla-project.org/>`_

-------------------------
MobaXterm™ (Windows)
-------------------------

`MobaXterm™ <https://mobaxterm.mobatek.net/>`_ has a built-in function for SFTP. Connect to our UI with your DiCOS account, and the left panel will show the files in the UI, then you could go ahead with the download/upload.

.. seealso::

   * `MobaXterm™ <https://mobaxterm.mobatek.net/>`_

-------------------------
WinSCP™ (Windows)
-------------------------

`WinSCP™ <https://winscp.net/eng/index.php>`_ have file manager like UI. You could install one of them and login with SFTP/SCP protocol to our user interface, then you could drag to copy your files/directories between the UI and your computer.

.. seealso::

   * `WinSCP™ <https://winscp.net/eng/index.php>`_

