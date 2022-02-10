HTCondor Job Management
========================

--------------------
Check resources
--------------------

Use the ``condor_status`` command to show the slot (machine) status on the worker nodes. e.g.

::

    $ condor_status

                  Machines Owner Claimed Unclaimed Matched Preempting  Drain

     X86_64/LINUX      414     0     322        92       0          0      0

            Total      414     0     322        92       0          0      0

--------------------
Check queue status
--------------------

Running and queuing jobs will be shown with condor_q command

::

     $ condor_q

     -- Schedd: test_queue@condor-ui01.twgrid.org : <202.140.186.222:9618?... @ 09/07/21 13:54:01
     OWNER    BATCH_NAME    SUBMITTED   DONE   RUN    IDLE   HOLD  TOTAL JOB_IDS
     mky      ID: 48977    9/7  08:32      _      _      _      1      1 48977.0

------------------------------
Check historical status
------------------------------

If a job is finished/failed/cancelled, it will be moved from queue status to history status, you could use condor_history to check the historical jobs. The ST column means the status of the job. C: completed, X: failed.

::

    $ condor_history
     ID     OWNER          SUBMITTED   RUN_TIME     ST COMPLETED   CMD
    49015.0   harvesteruser   9/7  11:44   0+02:11:46 C   9/7  13:55 /sharedfs/common/ams-MCgen.sh /sharedfs/common/ProcessMonitor.py
    49014.0   harvesteruser   9/7  11:42   0+02:10:21 C   9/7  13:53 /sharedfs/common/ams-MCgen.sh /sharedfs/common/ProcessMonitor.py
    49013.0   harvesteruser   9/7  11:41   0+02:11:47 C   9/7  13:53 /sharedfs/common/ams-MCgen.sh /sharedfs/common/ProcessMonitor.py
    49012.0   harvesteruser   9/7  11:39   0+02:12:58 C   9/7  13:52 /sharedfs/common/ams-MCgen.sh /sharedfs/common/ProcessMonitor.py

------------------------------
Job Description File
------------------------------

A job description language (jdl) is written as a file with suffix .jdl. It's essential for the job submission with condor system. A very simple example is:

::

    executable = hello_world.sh
    output = hello_world.job.$(cluster).$(process).out
    error = hello_world.job.$(cluster).$(process).err
    log = hello_world.job.$(cluster).$(process).log

    queue 1

Note
^^^^^^

* **Executable**: Executable in jdl file could be a shell script or an executable. In general, we will recommend you to use a shell script as executable, and this make you more flexible to turn your job.
* **Macros**: $(cluster) and $(process) are macros in jdl file. The number "$(cluster).$(process)" is represent for a condor job ID, which is identical across condor system, and you could manipulate your job with the condor job ID.
* **Working Directory**: By default, the job submission directory will be the working directory of condor job. If your input/output file doesn't have absolute path, then it should be related to the current path of your job submission.
* **Job Outputs**
   - output: the stdout output of your job
   - error: the stderr output of your job
   - log: the accounting and housekeeping data of your condor job

------------------------------
Submit a job
------------------------------

If you have simple.jdl ready, you could submit your job via (your job ID will be prompted upon submission):

::

    $ condor_submit simple.jdl

------------------------------
Check the job status
------------------------------

You could use condor_q to check your job status. If you need detail information of the job, use:

::

    $ condor_q -long your_job_id

for that purposes.

----------------------------------
Check the historical job status
----------------------------------

You could get detail information of your historical job information with the command:

::

    $ condor_history -long your_job_id

------------------------------
Cancellation of a job
------------------------------

You could cancel your job via:

::

    $ condor_rm your_job_id

to cancel your running/pending jobs.

------------------------------
Modules in FDR5
------------------------------

To apply different settings of different software for various of users, we adopted environment-module package for the user oriented package management.

Show available modules
^^^^^^^^^^^^^^^^^^^^^^^^^

::

   $ module avail

         --------------------------------------------------------------------------- /cvmfs/cvmfs.grid.sinica.edu.tw/hpc/modules/modulefiles/Core ---------------------------------------------------------------------------
    app/anaconda3/4.9.2  app/cmake/3.20.3  app/root/6.24  gcc/9.3.0   gcc/11.1.0  intel/2018  nvhpc_sdk/20.11  python/3.9.5
    app/binutils/2.35.2  app/make/4.3      gcc/4.8.5      gcc/10.3.0  intel/2017  intel/2020  pgi/20.11

Load module
^^^^^^^^^^^^^^^
::

    $ module load intel/2020

Unload module
^^^^^^^^^^^^^^^
::

    $ module unload intel/2020

Hierarchy of modules
^^^^^^^^^^^^^^^^^^^^^^

Some modules are dependent on specific parent modules. To see the dependent child modules, you need to load parent module first, and then see the child modules through:

::

    $ module avail

command

Unload all modules
^^^^^^^^^^^^^^^^^^^^^
::

    $ module purge


------------------------------
MCORE Job Example
------------------------------

* Example JDL

::

    executable = stress
    arguments = "-c 4 -t 100"
    output = stress.$(cluster).$(process).out
    error = stress.$(cluster).$(process).err
    log = stress.job.log
    request_cpus = 4

    queue 1

------------------------------
# MPI Job Example
------------------------------

* run_lammps_mpi.sh

::

    #!/bin/bash

    source /etc/profile.d/dicos-environment-modules.sh
    module load intel
    module load mpich
    module load lammps
    mpirun -np 3 lmp -in SSMD_input1.txt

    tar cvf ./lammps_run_mpi.tar ./*

* run_lammps_mpi.jdl

::

    universe = parallel
    executable = run_lammps_mpi.sh
    machine_count = 4
    should_transfer_files = yes
    when_to_transfer_output = on_exit
    transfer_input_files = SSMD_input1.txt
    output = lammps_mpi.$(cluster).$(process).out
    error = lammps_mpi.$(cluster).$(process).err
    log = lammps_mpi.job.log
    transfer_output_files = lammps_run_mpi.tar
    should_transfer_files   = YES
    when_to_transfer_output = ON_EXIT

    queue 1
