Data Management Client Command Line Tool
===========================================

===========================================================
Data Management Client Command Line Tool (ddmc)
===========================================================

--------------------------
Advance Preparation
--------------------------

1. Before using DiCOS, you should have the following things : 

    - A grid user certificate, [tutorial](wiki:/certificate/)

    - Join a VO (Virtual Organization), [tutorial](wiki:/account/)

    - A DiCOS account, [tutorial](wiki:/account/)

2. SSH log in DiCOS web UI with your DiCOS account: 

    - **dicos-ui.grid.sinica.edu.tw** or  
    - **dicos-ui.twgrid.org**

--------------------------
Commands
--------------------------

Setup 
^^^^^^^^^^^^^^^^

Initialize the voms proxy before using ddmc.

* ``voms-proxy-init -voms <VO>``

::

    $ voms-proxy-init -voms twgrid


* Note:

  - <*VO*> is one the Virtual Organizations you are joining, for example : **twgrid**, **atlas**, **ams02.cern.ch**
  - If you have already initialized a voms proxy in last 12 hours (so the proxy is not expired), you don't need to do this step again. In fact, "ddmc" will remind you if you don't have a valid and unexpired voms proxy initialized.


Ping
^^^^^^^^^^^^^^^^

Connect to DiCOs Data Management (DDM) server to see if it's alive. It will return OK if everything is fine.

* ``ddmc ping``

::

   $ ddmc ping
   RUCIO Version: 0.2.6
   DDM Ping OK!

Upload
^^^^^^^^^^^^^^^^

Upload and register your local file to a DDM dataset.

* ``ddmc ul|upload <local file path> <DDM dataset>``

::
   
   $ ddmc ul /home/wchang/wjtest/wjtest17 wjtest_dataset1

   $ ddmc ul /home/wchang/wjtest/wjtest* wjtest_dataset1

* Note:

  - The ``<local file path>`` can be either absolute path or relative path.
  - Wildcard * is available in ``local file path`` to upload multiple files.
  - ``local file path`` has to be **regular file(s)**; any directory (and everything under it) or irregular file will NOT be uploaded. 
  - The ``DDM dataset`` MUST be defined in this command.
  - If the dataset ``DDM dataset`` has not existed in your scope yet, it will be automatically created first.
 

Download
^^^^^^^^^^^^^^^^

Download a file or all files in a container/dataset on DDM to your local directory.

* ``ddmc dl|download <DDM container/dataset/file> [<local directory path>]``

::
   
   $ ddmc dl tid9907_1473730551_wj_test_pilotlog.txt /home/wchang

* Note:

  - When downloading a whole dataset or container, all files in it will be downloaded to the local directory WITHOUT any nested sub-directory.
  - ``local directory path`` MUST be a **directory**, not a file. If this argument is missed in the command, present working directory (pwd) will be the default directory.
  - Wildcard * is NOT supported in ``DDM container/dataset/file``

Query
^^^^^^^^^^^^^^^^

List content in a container/dataset in your scope on DDM.

* ``ddmc ls [-r] [<DDM container/dataset>]``

::

   $ ddmc ls wjtest_2015031701
    |    |- wjtest09 [FILE]
    |    |- wjtest10 [FILE]
    |    |- wjtest11 [FILE]
    |    |- wjtest12 [FILE]
    |    |- wjtest13 [FILE]
    |    |- wjtest14 [FILE]
    |    |- wjtest15 [FILE]
    |    |- wjtest16 [FILE]
    |    |- wjtest18 [FILE] 
   
   $ ddmc ls 
   JobOutput [CONTAINER]
   wjtest2194 [FILE]
   wjtest_20150313 [DATASET]
   wjtest_20150315 [DATASET]
   wjtest_20150316 [DATASET]
   wjtest_2015031601 [DATASET]
   wjtest_2015031701 [DATASET]
   wjtest_20150324 [DATASET]

   $ ddmc ls -r
   JobOutput [CONTAINER]
    |    |- wjtest_20150312 [DATASET]
    |    |    |- wjtest111 [FILE]
    |    |- wjtest_20150313 [DATASET]
    |    |    |- wjtest112 [FILE]
    |    |    |- wjtest113 [FILE]
   wjtest2194 [FILE]
   wjtest_20150313 [DATASET]
    |    |- wjtest101 [FILE]
    |    |- wjtest102 [FILE]
    |    |- wjtest103 [FILE]
   ......

* Note:

  - If ``DDM container/dataset`` is missing in the command, content in the top scope will be listed.
  - With option '-r', one can list all files exhaustively (recursively) in the container/dataset.


List file information such as file size, checksum, and direct link.

* ``ddmc getlink <DDM file>``

::
   
   $ ddmc getlink tid9885_1473730529_wj_test_pilotlog.txt

============
Note
============

This command-line tool is meant to deal with massive local file upload/download only. To use complete data management functions (such as copy/paste, creating a new container/dataset, etc.), please go to `DiCOS Data Management Webpage <https://dicos.grid.sinica.edu.tw/ddm/>`_.
