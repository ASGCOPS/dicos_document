Job Submission Command Line Tool
==================================

==========================
Advance Preparation
==========================

1. Before using DiCOS, you should have the following things : 

  - A grid user certificate, [tutorial](wiki:/certificate/)
  - Join a VO (Virtual Organization), [tutorial](wiki:/account/)
  - A DiCOS account, [tutorial](wiki:/account/)

2. SSH log in DiCOS web UI with your DiCOS account: 

  - **dicos-ui.grid.sinica.edu.tw** or  
  - **dicos-ui.twgrid.org**

==========================
Commands
==========================

----------------
Setup 
----------------

* Initialize the voms proxy

  ``voms-proxy-init -voms <VO>``

::

   $ voms-proxy-init -voms twgrid

* Note:

  - <*VO*> is one the Virtual Organizations you are joining, for example : **twgrid**, **atlas**, **ams02.cern.ch**


-------------------
Submit job
-------------------

Submit job to DiCOS.

``dsub --computingSite <Computing Site> --jobCommands <"Commands">  --runList <Input File List> [--noDM] --taskname <Task Name> --nfiles <Number> --userlib <User Libraries> --transformation http://asgc-ui03.grid.sinica.edu.tw/panda/transformations/user/user.hlee/job-gen.py``

::

   $ dsub --computingSite ANALY_TAIWAN_TWGRID_PHYS_POSIX --jobCommands "myscripts.sh 64"  --runList myinputs.list --noDM --taskname Asize64 --nfiles 2 --userlib libmyprogs.so --transformation http://asgc-ui03.grid.sinica.edu.tw/panda/transformations/user/user.hlee/job-gen.py

* Note:

  - --computingSite

    - Use to specify computing sites. 
    - Each VO has its corresponding computing sites and each sits contains different resources.
    - For twgrid user or IOP users. please always use sites with prefix ANALY_TAIWAN_TWGRID_*
    - Reference :  [Available Computing Sites](wiki:/available_computing_sites/)


  - --jobCommands

    - <*"Commands"*> is the command that runs your applications or scripts.
    - Just like that your run on your PC.
    - It can be any UNIX commands, shell scripts or other executable applications.
    - For example : 

      * --jobCommands "sh myScript.sh arg1 arg2"
      * --jobCommands "echo hostname; cat myInput.txt"
      * --jobCommands "python myAPP.py"


  - --runList

    - <*Input File List*> is a **local text file** to specify input list.
    - Each line will be treated as one input file.
    - There are three kinds of formats : 
        1. Using our Distributed Data Management (DDM), the format will be : **[scope]:[filename]**
            - You have to upload the input files to our DDM first, via [web UI](https://dicos.grid.sinica.edu.tw/ddm/) or [command-line](wiki:/data_management_command_line_tool/).
            - The input files will be downloaded from DDM to the working directory by pilot automatically.
            - For example : 

                    ams-user-felixlee:Trigger_1368946224.00000001.root
                    ams-user-felixlee:Trigger_1368947640.00000001.root
                    ams-user-felixlee:Trigger_1368949011.00000001.root


  - --noDM

    - It's important if you don't use inputs from our Distributed Data Management (DDM) system, use this option, the pilot will not go to data management system to get your inputs.


  - --taskname

    - Use to specify task name, it will be also used as the output dataset name.


  - --nfiles

    - Use to specify how many inputs files per job.

      - dusb will divide the files in the <*Input File List*> by the sequence. 
      - For example, there 50 files listed in the <*Input File List*> and --nfiles 5. It means that dsub will submit 10 jobs, each with 5 inputs.

  - --userlib

    - Use to specify user libraries.
    - These user libraries must be registered in user scope in our distributed data management system(RUCIO).
    - If the libraries are tarball, pilot will untar for you in the working directory.
    - You could use "**,**" to separate the multiple files.
    - Just give it the file name, for example : 

      ::

         --userlib ISS_Proton_Dec12_V1.tar.gz, myLib.so

  - --transformation

    - Use to specify transformation script.
    - At this moment, please use  http://asgc-ui03.grid.sinica.edu.tw/panda/transformations/user/user.hlee/job-gen.py
    - To know more about the transformation script. [What is the transformation script ?](wiki:/what_is_the_transformation_script/)
    - Once you know how transformation script works, you can have your own transformation.
    - For example : 

      ::

         --transformation http://asgc-ui03.grid.sinica.edu.tw/panda/transformations/user/user.hlee/job-gen.py

  - --help

    - Get more information about dsub with command dsub --help

      ::

         $ dsub --help

-------------------
Get job status
-------------------

    Get the job status and other related information.
  
    ``getjobstatus.py <panda ID 1> <panda ID 2> ... <panda ID N>``

::

        $ getjobstatus.py 1473799114 1473799115


- Note:

  - You could also go to `web UI <https://dicos.grid.sinica.edu.tw/monitor/>`_ to monitor the jobs.


-------------------
Cancel job
-------------------

    Cancel the jobs in status "running" or "activated".
  
    ``killjobs.py <panda ID 1> <panda ID 2> ... <panda ID N>``

::

        $ killjobs.py 1473799114 1473799115

* Note:

  - "activated" jobs will be cancelled entirely. 
  - It's not guaranteed that all the "running" jobs will be killed. Some of them will still run until it finish themselves. 

-------------------
Rerun job
-------------------

    In case job failed, rerun jobs without changing anything.
  
    ``rerunjobs.py <panda ID 1> <panda ID 2> ... <panda ID N>``

::

   $ rerunjobs.py 1473799114 1473799115

* Note:

  - rerunjobs.py will submit jobs again with all the same arguments that you submitted first time, and return the new panda ID.      

===================
Practice
===================

- Preparation

    1. Assuming you have application and job script like:

        - ``myprog.exe``

            The myprog.exe needs following arguments

            ::

                ./myprog.exe [array size] [input file 1] [input file 2] ...[input file(N)]

        - ``libmyprogs.so``

        - ``myscript.sh``

            Here is myscripts.sh:

            ::

                #!/bin/bash
                # The "noDmFile0.txt" comes with --noDM, in this case, we don't use DDM system to get inputs
                ./myprog.exe $1 $( cat noDmFile0.txt | awk '{printf $0" "}' )

    2.  Then, you need to make them into tarball, let's say "myuserlib.tar.gz".

        ::

            tar -czf myuserlib.tar.gz myprog.exe libmyprogs.so myscript.sh

    3. Upload myuserlib.tar.gz to our data management system. please refer: :doc:`web UI <dicos_djm/dicos/dicos101>`) or :doc:`command-line <other/data_management_command_line_tool>`)

    4. Once your ``myuserlib.tar.gz`` is available at our distributed DM system, you can then pick up your inputs either from our distributed DM system or anywhere as long as the cluster worker node can have access to it.

    5. Here we assume input files are stored at local NFS, so, we create a list called "myinputs.list" with following contents:

       ::

            /nfs/data01/user/mydata/myinput1.dat
            /nfs/data01/user/mydata/myinput2.dat
            /nfs/data01/user/mydata/myinput3.dat
            /nfs/data01/user/mydata/myinput4.dat

- Execute 

    1. Initialize the voms proxy, assuming you have twgrid VO.

       ::

            $ voms-proxy-init -voms twgrid

    2. Submit job

        - We want to process two inputs for each jobs, and we want to run a small case with array size 64, and the run jobs at ANALY_TAIWAN_TWGRID_PHYS. 
        - Because the inputs are not from the DDM, use --noDM
        - The following command will do:

          ::

             $ dsub --computingSite ANALY_TAIWAN_TWGRID_PHYS --jobCommands "myscripts.sh 64"  --runList myinputs.list --noDM --taskname Asize64 --nfiles 2 --userlib libmyprogs.so --transformation http://asgc-ui03.grid.sinica.edu.tw/panda/transformations/user/user.hlee/job-gen.py

    3. If the job is submitted successfully, it will return panda ID like this:

       ::

            PandaID: 1473799114
            PandaID: 1473799115

- Result

    1. Use getjobstatus.py to check job status or visit `web UI <https://dicos.grid.sinica.edu.tw/monitor/>`_ to monitor.

       ::

            $ getjobstatus.py 1473799114 1473799115  

    2. In case job failed, use rerunjobs.py to rerun jobs.

       ::

            $ rerunjobs.py 1473799114 1473799115

    3. In case job finished, download the output to check.

        - The taskname "Asize64" will also be the name of output dataset, download this dataset to get the outputs.

            - Use :doc:`command-line tool <other/data_management_command_line_tool>`
            - Use `web UI https://dicos.grid.sinica.edu.tw/ddm/>`_
    
