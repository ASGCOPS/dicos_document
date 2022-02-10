DiCOS CLI Tool (Deprecated)
=============================

========================================================
NOTE! DiCOS Services are no longer required CA & VO.
========================================================

* Refer to :doc:`DiCOS_Client_Tool <dicos_cli_tool_bridge>` for instructions of dicos-client-tools.
* Only specific grid resources will need CA & VO authentication.

===================================================
Before using DiCOS CLI Tool with CA & VO...
===================================================

--------------------------------------
About Certificates & VO
--------------------------------------

#. [Apply for certificate](wiki:/apply_for_certificate)
#. [Import certificate to browser](wiki:/import_certificate_to_browser)
#. [Join Virtual Organization](wiki:/join_virtial_organization)

--------------------------------------------------------------
### Preparation 0: Log in DiCOS command-line UI server
--------------------------------------------------------------

SSH login one of dicos UI server with your DiCOS account and password.

* dicos-ui02 (CentOS6)
* dicos-ui04 & dicos-ui06.grid.sinica.edu.tw (CentOS7)

::

    (Your_PC)$ ssh users@dicos-ui02.grid.sinica.edu.tw

    [users@dicos-ui02 ~]$

You should login successfully.

----------------------------------------------------------------
### Preparation 1: Put your Grid key/certificate in place
----------------------------------------------------------------

To use DiCOS CLI Tool, you need to prepare the Grid key/certificate file pair (usually named `usercert.pem` and `userkey.pem`), which is the same certificate you applied for your DiCOS account with.

Create a directory named ``.globus`` under your home directory.

::

    [users@dicos-ui02 ~]$ mkdir -p ~/.globus/

Copy your key/certificate file pair into the directory ``~/.globus/`` on DiCOS command-line UI server.
For example, you may copy your key/certificate from your PC via scp:

::

    (Your_PC)$ scp usercert.pem <your account name>@dicos-ui02.grid.sinica.edu.tw:~/.globus/
    (Your_PC)$ scp userkey.pem <your account name>s@dicos-ui02.grid.sinica.edu.tw:~/.globus/

Make sure the key and certificate are named ``usercert.pem`` and ``userkey.pem`` respectively under your ``~/.globus/`` directory.

::

    [users@dicos-ui02 ~]$ ls ~/.globus/
    usercert.pem  userkey.pem

Change permission of your key and certificate.
Note the permission of ``usercert.pem`` should be ``0644``, and ``userkey.pem`` should be ``0400``.

::

    [users@dicos-ui02 ~]$ chmod 644 ~/.globus/usercert.pem
    [users@dicos-ui02 ~]$ chmod 400 ~/.globus/userkey.pem
    [users@dicos-ui02 ~]$ ll ~/.globus/
    -rw-r--r-- 1 users 99999 9999 Jan 01 00:00 usercert.pem
    -r-------- 1 users 99999 9999 Jan 01 00:00 userkey.pem

----------------------------------------------------------------
Preparation 2: Initialize your voms proxy.
----------------------------------------------------------------

You need to initialize voms proxy to access DiCOS services.

You should already have a membership of specific VO (Virtual Organization, usually ``twgrid``) associated with your user certificate. (If not, see :doc:`here <./../dicos_account/account_old>`)

Initialize voms proxy with the command:

::

    [users@dicos-ui02 ~]$ dicos proxy initialize <your_vo>

For example, with ``twgird`` vo :

::

    [users@dicos-ui02 ~]$ dicos proxy initialize twgrid

Enter the password of your key (paired with your Grid certificate), and you will get a success message.

::

    User proxy initialized

**Troubleshooting.** When you see this:

::

    [WARNING] Cannot get Credential Information on MyProxy.
    [ERROR] Your voms proxy has been (or is about to be) expired !!
    [ERROR] Please initialize your voms proxy again.

It means ``your proxy is expired``. Please re-initialize your proxy by execute the same command above.

---------------------------
Quick Start Tutorial
---------------------------

Here shows a simple example step by step to run job with DiCOS.

Here is an example job, which will generate an output file ``MyOutput.txt``, whose content is a string ``Hello``.
Please save the following content as a file and named it ``PrintHello.sh``.

::

    #!/bin/bash
    echo "Hello" > ./HelloWorld.txt


Next, check your file is in your home directory, type `ls` to check.

::

    [users@dicos-ui02 ~]$ ls
    PrintHello.sh

Now, we will start to submit a job.

::

    [users@dicos-ui02 ~]$ dicos job submit -i PrintHello.sh -N NameOfJob -c "./PrintHello.sh"

- Command ``dicos`` is the only command to know. All command lines related to DiCOS begin with `dicos`.
- Command ``job`` is one subcommand of `dicos`, which means `do some operation about job`.
- Command ``submit`` is one subcommand of 'job', which means `to submit job(s)`.
- The option ``-i`` of ``submit`` is to specify input files of your job. Put your specified local file path after it.
- The option ``-N`` of ``submit`` is to specify the name of this task (job or jobs) to submit.
- The option ``-c`` of ``submit`` is to specify the command to execute. In this example, "./PrintHello.sh" means 'just execute PrintHello.sh'

After executing this command, you will get the JobID (aka PandaID) and TaskID (aka jobDefinitionID) of your job(s):

::

    Job 9999999 is submitted. (TaskID: 9999)

Next, you can check job status via command.

::

    [users@dicos-ui02 ~]$ dicos job status

And you can see something like:

::

     TaskID    PandaID  Name                      Status
     -----------------------------------------------------
     9999      9999999  NameOfJob                 running


Then, wait patiently until the job finishes :)

Now, check the job status again to make sure it is finished.

::

    [users@dicos-ui02 ~]$ dicos job status

    TaskID    PandaID  Name                      Status
    -----------------------------------------------------
    9999      9999999  NameOfJob                 finished

If the job status has become ``finished``, it is time to get the output!

::

    [users@dicos-ui02 ~]$ dicos job getoutput <YourJobID>

In this example. <YourJobID> is ``9999999``.

::

    [users@dicos-ui02 ~]$ dicos job getoutput 9999999

And you will get a successful message.

::

    Got output of job 9999999 in ./DiCOS_job_9999999_NameOfJob_output

where shows the directory containing the outputs of your job.

Now, use ``ls`` command to check this directory .

::

    [users@dicos-ui02 ~]$ ls ./DiCOS_job_9999999_NameOfJob_output
    HelloWorld.txt

And you can check if the output file is as expected:

::

    [users@dicos-ui02 ~]$ cat ./DiCOS_job_9999999_NameOfJob_output/HelloWorld.txt
    Hello

Bravo!

The quick start tutorial ends here.
For more details, see the description below.


===================================================
How to use these dicos subcommands and options?
===================================================

You can use ``-h`` or ``--help`` after any command lines starting with ``dicos`` to get the help message of the subcommands or options.

For example, to see what subcommands of ``dicos`` are available:

::

    [users@dicos-ui02 ~]$ dicos --help

For example, to see what options of ``dicos job submit`` are available:

::

    [users@dicos-ui02 ~]$ dicos job submit --help


===================================================
More Tips about DiCOS Subcommands
===================================================

ping:
^^^^^^^^^^

Ping DiCOS server, check server status and connection.

::

    [users@dicos-ui02 ~]$ dicos ping

whoami:
^^^^^^^^^^

Check your proxy and get your ID infomation

::

    [users@dicos-ui02 ~]$ dicos whoami

proxy:
^^^^^^^^^^

Deal with user voms proxy.
See its subcommands description below.

initialize
^^^^^^^^^^^^^^^^

Initialize your proxy for use DiCOS.

::

    [users@dicos-ui02 ~]$ dicos proxy initialize

setvoms
^^^^^^^^^^

Set or change to specific VO of your proxy.

::

    [users@dicos-ui02 ~]$ dicos proxy setvoms <YourVO>

destroy
^^^^^^^^^^

Destroy your current proxy.

::

    [users@dicos-ui02 ~]$ dicos proxy destroy

------
Job
------

Operations about jobs. See its subcommands description below, or use `--help` to see details of options.

submit
^^^^^^^^^^^

Submit job(s) to DiCOS server.

::

    [users@dicos-ui02 ~]$ dicos job submit -i <FileName> -c '<YourCommand>'

Or you can prepare one file list contain file name which you want to submit to DiCOS server.

::

    [users@dicos-ui02 ~]$ dicos job submit -f <FileNameList> -c '<YourCommand>' -j <NumberOfJobs>

You can also use -A to submit jobs with different arguments.

::

    [users@dicos-ui02 ~]$ dicos job submit -A <ArgumentList> -c '<YourCommand>' -i <LocalInput>

Specify the computing resource requirement of your job.

::

    [users@dicos-ui02 ~]$ dicos job submit -i <FileName> -c '<YourCommand>' --requireCores 20 --requireRAM 1000

status
^^^^^^^^^^^

Check status of job. The default subcommand just shows jobs within 240 hours, and 15 jobs at most.

::

    [users@dicos-ui02 ~]$ dicos job status

Maybe You want to check a single job

::

    [users@dicos-ui02 ~]$ dicos job status <JobID>

You can get job status display in long format, and sort these result with specified column.

::

    [users@dicos-ui02 ~]$ dicos job status -l
    [users@dicos-ui02 ~]$ dicos job status -l <JobID>
    [users@dicos-ui02 ~]$ dicos job status -l -S <ColumnTitle>

Of course you can sort by reverse order.

::

    [users@dicos-ui02 ~]$ dicos job status -l -R
    [users@dicos-ui02 ~]$ dicos job status -l -S <ColumnTitle> -R

Now usable <ColumnTitle> are 'TaskID', 'PandaID', 'Name', 'Queue', 'Creation_Time', 'End_Time', 'Status'.

<ColumnTitle> can be found when you check display in long format.


In default display format, all jobs that have been resubmitted will not appear.
If you need to check the information of all jobs, add `-al` option after command.

::

    [users@dicos-ui02 ~]$ dicos job status -al
    [users@dicos-ui02 ~]$ dicos job status -l -al
    [users@dicos-ui02 ~]$ dicos job status -l -S <ColumnTitle> -al


If you want to check jobs submitted more than 240 hours ago or display more jobs, you can do it:

::

    [users@dicos-ui02 ~]$ dicos job status -t <hour>
    [users@dicos-ui02 ~]$ dicso job status -n <number of jobs>
    [users@dicos-ui02 ~]$ dicso job status -n <number of jobs> -t <specified hour> <JobID>

Also, it is able to get job status by specifying <TaskID> (instead of <JobID>).

::

    [users@dicos-ui02 ~]$ dicos job status -T <TaskID>

cancel
^^^^^^^^^^

Cancel submitted job

::

    [users@dicos-ui02 ~]$ dicos job cancel <JobID>

resubmit
^^^^^^^^^^^^

Resubmit submitted job

::

    [users@dicos-ui02 ~]$ dicos job resubmit <JobID>

getoutput
^^^^^^^^^^^^

Get output files of submitted job

::

    [users@dicos-ui02 ~]$ dicos job getoutput <JobID>

Also, it is able to get output of all jobs in the same task by specifying <TaskID>.

::

    [users@dicos-ui02 ~]$ dicos job getoutput -T <TaskID>


**Don't forget to use `-h` or `--help` for more information.**
