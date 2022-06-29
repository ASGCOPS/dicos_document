**********************
DiCOS Job System
**********************

.. sectionauthor:: Mike Yang <mike.yang@twgrid.org>

-----------------------------
DiCOS User Interfaces (UIs)
-----------------------------

The available DiCOS UI are listed below. DiCOS users could login with the DiCOS account to access our resources.

.. list-table::
   :header-rows: 1

   * - User Interface Node
     - OS
     - Purpose
   * - dicos-ui02.grid.sinica.edu.tw
     - SLC 6
     - File download/upload
   * - dicos-ui04.grid.sinica.edu.tw
     - CentOS 7
     - File download/upload
   * - dicos-ui05.grid.sinica.edu.tw
     - CentOS 7
     - Job submission, File download/upload
   * - dicos-ui06.grid.sinica.edu.tw
     - CentOS 7
     - Job submission, File download/upload

.. note::

   * The resources of the user interface node is limited, please don't run your jobs in the user interfaces, or your jobs will be killed without notice.

   * To avoid ssh password guessing attack, IP addresses with multiple login failures in a short time will be banned for hours.

   * Installed GUI software in UIs for users to preview files. Please use, for example:

     .. code-block:: bash

        ssh -XY <your_account>@dicos-ui05.grid.sinica.edu.tw

     to login in the UI with X11 forwarding enabled. If you are using Windows system, please install and execute `Xming <https://sourceforge.net/projects/xming/>`_ before connect to the UI.

     .. list-table::
        :header-rows: 1
     
        * - Software
          - Filetype
        * - `eog <https://wiki.gnome.org/Apps/EyeOfGnome>`_
          - images
        * - `xpdf <https://www.xpdfreader.com/>`_
          - pdf files


-----------------------------
DiCOS Queues
-----------------------------

As of 2022-07-13, DiCOS job submission only support for batch GPU jobs. The available DiCOS queues could be found in the table below:

.. list-table::
   :header-rows: 1

   * - Queue Name
     - GPU
   * - ANALY_TAIWAN_TWGRID_V100_GPU_QCD
     - V100
   * - ANALY_TAIWAN_TWGRID_V100_GPU
     - V100
   * - ANALY_TAIWAN_TWGRID_SPECFEM3D_GPU
     - V100
   * - ANALY_TAIWAN_TWGRID_KAGRA_GPU
     - V100
   * - ANALY_TAIWAN_TWGRID_AUTODOCK_GPU
     - V100


-----------------------------
DiCOS Client Tools
-----------------------------

Before using DiCOS CLI Tool
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

----------------------------------------------------
Preparation: Log in DiCOS command-line UI server
----------------------------------------------------

SSH login one of dicos UI server with your DiCOS account and password.

* dicos-ui05 & dicos-ui06.grid.sinica.edu.tw (CentOS7)

::

    (Your_PC)$ ssh users@dicos-ui05.grid.sinica.edu.tw
    (Your_PC)$ ssh users@dicos-ui06.grid.sinica.edu.tw

    [users@dicos-ui05 ~]$
    [users@dicos-ui06 ~]$

You should login successfully.

Quick Start Tutorial
^^^^^^^^^^^^^^^^^^^^^^^^

Here shows a simple example step by step to run job with DiCOS.

Here is an example job, which will generate an output file *MyOutput.txt*, whose content is a string *Hello*.
Please save the following content as a file and named it *PrintHello.sh*.

.. code-block:: bash

    #!/bin/bash
    echo "Hello" > ./HelloWorld.txt

Next, check your file is in your home directory, type ``ls``: to check.

::

    [users@dicos-ui05 ~]$ ls
    PrintHello.sh

Now, we will start to submit a job.

::

    [users@dicos-ui05 ~]$ dicos job submit -i PrintHello.sh -N NameOfJob -c "./PrintHello.sh"

- Command ``dicos`` is the only command to know. All command lines related to DiCOS begin with ``dicos``.
- Command ``job`` is one subcommand of ``dicos``, which means **do some operation about job**.
- Command ``submit`` is one subcommand of 'job', which means **to submit job(s)**.
- The option ``-i`` of ``submit`` is to specify input files of your job. Put your specified local file path after it.
- The option ``-N`` of ``submit`` is to specify the name of this task (job or jobs) to submit.
- The option ``-c`` of ``submit`` is to specify the command to execute. In this example, "./PrintHello.sh" means 'just execute PrintHello.sh'

After executing this command, you will get the JobID (aka PandaID) and TaskID (aka jobDefinitionID) of your job(s):

::

    Job 9999999 is submitted. (TaskID: 9999)

Next, you can check job status via command.

::

    [users@dicos-ui05 ~]$ dicos job status

And you can see something like:

::

     TaskID    PandaID  Name                      Status
    -----------------------------------------------------
     9999      9999999  NameOfJob                 running


Then, wait patiently until the job finishes :)

Now, check the job status again to make sure it is finished.

::

    [users@dicos-ui05 ~]$ dicos job status

    TaskID    PandaID  Name                      Status
    -----------------------------------------------------
    9999      9999999  NameOfJob                 finished

If the job status has become **finished**, it is time to get the output!

::

    [users@dicos-ui05 ~]$ dicos job getoutput <YourJobID>

In this example. <YourJobID> is **9999999**.

::

    [users@dicos-ui05 ~]$ dicos job getoutput 9999999

And you will get a successful message.

    Got output of job 9999999 in ./DiCOS_job_9999999_NameOfJob_output

where shows the directory containing the outputs of your job.

Now, use ``ls`` command to check this directory .

::

    [users@dicos-ui05 ~]$ ls ./DiCOS_job_9999999_NameOfJob_output
    HelloWorld.txt

And you can check if the output file is as expected:

::

    [users@dicos-ui05 ~]$ cat ./DiCOS_job_9999999_NameOfJob_output/HelloWorld.txt
    Hello

Bravo!

The quick start tutorial ends here. For more details, see the description below.

How to use these dicos subcommands and options?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can use ``-h`` or ``--help`` after any command lines starting with ``dicos`` to get the help message of the subcommands or options.

For example, to see what subcommands of ``dicos`` are available:

::

    [users@dicos-ui04 ~]$ dicos --help

For example, to see what options of ``dicos job submit`` are available:

::

    [users@dicos-ui04 ~]$ dicos job submit --help

More Tips about DiCOS Subcommands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-------
ping
-------

Ping DiCOS server, check server status and connection.

    [users@dicos-ui05 ~]$ dicos ping

-------
job
-------

Operations about jobs.
See its subcommands description below, or use `--help` to see details of options.

submit
^^^^^^

Submit job(s) to DiCOS server.

::

    [users@dicos-ui05 ~]$ dicos job submit -i <FileName> -c '<YourCommand>'

Or you can prepare one file list contain file name which you want to submit to DiCOS server.

::

    [users@dicos-ui05 ~]$ dicos job submit -f <FileNameList> -c '<YourCommand>' -j <NumberOfJobs>

You can also use -A to submit jobs with different arguments.

::

    [users@dicos-ui05 ~]$ dicos job submit -A <ArgumentList> -c '<YourCommand>' -i <LocalInput>

Specify the computing resource requirement of your job.

::

    [users@dicos-ui05 ~]$ dicos job submit -i <FileName> -c '<YourCommand>' --requireCores 20 --requireRAM 1000

status
^^^^^^^^^

Check status of job. The default subcommand just shows jobs within 240 hours, and 15 jobs at most.

::

    [users@dicos-ui05 ~]$ dicos job status

Maybe You want to check a single job

::

    [users@dicos-ui05 ~]$ dicos job status <JobID>

You can get job status display in long format, and sort these result with specified column.

::

    [users@dicos-ui05 ~]$ dicos job status -l
    [users@dicos-ui05 ~]$ dicos job status -l <JobID>
    [users@dicos-ui05 ~]$ dicos job status -l -S <ColumnTitle>

Of course you can sort by reverse order.

::

    [users@dicos-ui05 ~]$ dicos job status -l -R
    [users@dicos-ui05 ~]$ dicos job status -l -S <ColumnTitle> -R

Now usable <ColumnTitle> are 'TaskID', 'PandaID', 'Name', 'Queue', 'Creation_Time', 'End_Time', 'Status'.

<ColumnTitle> can be found when you check display in long format.


In default display format, all jobs that have been resubmitted will not appear.
If you need to check the information of all jobs, add `-al` option after command.

::

    [users@dicos-ui05 ~]$ dicos job status -al
    [users@dicos-ui05 ~]$ dicos job status -l -al
    [users@dicos-ui05 ~]$ dicos job status -l -S <ColumnTitle> -al


If you want to check jobs submitted more than 240 hours ago or display more jobs, you can do it:

::

    [users@dicos-ui05 ~]$ dicos job status -t <hour>
    [users@dicos-ui05 ~]$ dicso job status -n <number of jobs>
    [users@dicos-ui05 ~]$ dicso job status -n <number of jobs> -t <specified hour> <JobID>

Also, it is able to get job status by specifying <TaskID> (instead of <JobID>).

::

    [users@dicos-ui05 ~]$ dicos job status -T <TaskID>

cancel
^^^^^^^^

Cancel submitted job

::

    [users@dicos-ui05 ~]$ dicos job cancel <JobID>

resubmit
^^^^^^^^^

Resubmit submitted job

::

    [users@dicos-ui05 ~]$ dicos job resubmit <JobID>

getoutput
^^^^^^^^^^^^

Get output files of submitted job

::

    [users@dicos-ui05 ~]$ dicos job getoutput <JobID>

Also, it is able to get output of all jobs in the same task by specifying <TaskID>.

::

    [users@dicos-ui05 ~]$ dicos job getoutput -T <TaskID>


**Don't forget to use `-h` or `--help` for more information.**


