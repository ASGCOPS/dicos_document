Data Management Command Line Tool
===================================

**This document is only for the users from Institute of Physics, Academia Sinica**

========================
Advance Preparation
========================
 
1. SSH log in **pui01.phys.sinica.edu.tw** or **pui02.phys.sinica.edu.tw**
2. This user manual can also be found on pui01.phys.sinica.edu.tw:/cvmfs/cvmfs.grid.sinica.edu.tw/app/dicos/rucio/basic_rucio_commands.txt

========================
Commands
========================

--------------
Ping
--------------

    Connect to rucio server to see if it's alive. It will return rucio version if everything is OK.

    **rucio ping**

    ::

        $ rucio ping
        0.2.6

--------------
Upload
--------------

Register and upload your files to the storage.

**rucio upload --rse PHYS-EOS01_TWGRIDSCRATCHDISK --scope `<your scpoe>` --did `<your scope>:<dataset name>` --files `<your file path in local>`**

::

    $ rucio upload --rse PHYS-EOS01_TWGRIDSCRATCHDISK --scope twgrid-user-wchang --did twgrid-user-wchang:wjtest_20150324 --files /raid8/wchang/wjtest/wjtest17

* Note:

  - ``dataset name`` must be set.
  - If the ``dataset name`` does not exist in your scope, the system will create it for you.
  - The wildcard * can be used in ``your file path in local``.

----------------- 
Download
----------------- 

Download your files from the storage.

**rucio download `<your scope>:<file name>` --dir `<local directory to put your file>`**

::
   
   $ rucio download twgrid-user-wchang:tid9907_1473730551_wj_test_pilotlog.txt --dir /raid8/wchang

* Note:

  - ``file name`` can be replaced with ``dataset name`` or ``container name``.
  - When download a whole dataset or container, the files in it will all downloaded into a directory without any folder.
  - ``local directory to put your file`` must be a directory, can not be a file name.
  - Not support the wildcard * in ``your scope``:``file name``

------------
Query
------------

List top-level directory structure in your scope.

**rucio list-dids --scope `<your scope>` [--recursive]**

::
   
   $ rucio list-dids --scope twgrid-user-wchang 
   twgrid-user-wchang:JobOutput [CONTAINER]
   twgrid-user-wchang:wjtest19 [FILE]
   twgrid-user-wchang:wjtest_201503 [DATASET]
   twgrid-user-wchang:wjtest_20150315 [DATASET]
   twgrid-user-wchang:wjtest_20150316 [DATASET]
   twgrid-user-wchang:wjtest_2015031601 [DATASET]
   twgrid-user-wchang:wjtest_2015031701 [DATASET]
   twgrid-user-wchang:wjtest_20150324 [DATASET]

you can also list the whole structure in your scope by using "--recursive"

   ::

        $ rucio list-dids --scope twgrid-user-wchang --recursive


List the directory structure under indented did.

**rucio list-dids --scope `<your scope>` `<your scope>:<Dataset/Container name>`**

::

   $ rucio list-dids --scope twgrid-user-wchang twgrid-user-wchang:wjtest_2015031701
    |    |- twgrid-user-wchang:wjtest09 [FILE]
    |    |- twgrid-user-wchang:wjtest10 [FILE]
    |    |- twgrid-user-wchang:wjtest11 [FILE]
    |    |- twgrid-user-wchang:wjtest12 [FILE]
    |    |- twgrid-user-wchang:wjtest13 [FILE]
    |    |- twgrid-user-wchang:wjtest14 [FILE]
    |    |- twgrid-user-wchang:wjtest15 [FILE]
    |    |- twgrid-user-wchang:wjtest16 [FILE]
    |    |- twgrid-user-wchang:wjtest18 [FILE] 


List file information such as file size, checksum and file path.

**rucio list-replicas `<your scope>:<file name>`**

::
   
   $ rucio list-replicas twgrid-user-wchang:tid9885_1473730529_wj_test_pilotlog.txt
