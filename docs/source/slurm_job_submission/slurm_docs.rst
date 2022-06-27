Slurm Job Management
=========================

=========================
Check Resources
=========================

Use The 'Sinfo' Command To Display Information About Available Resources:
If you use the command without any options, it will display all available partitions.

::

    $sinfo -p compute
    PARTITION      AVAIL  TIMELIMIT  NODES  STATE NODELIST
    user-interface    up   infinite      2   idle slurm-ui01,slurm-ui-dev
    control           up       2:00      1   idle as-wn651
    compute*          up   infinite      5    mix as-wn[652-656]
    compute*          up   infinite     45   idle as-wn[657-682,701,709-718,720-727]
    v100              up   infinite      1    mix hp-teslav01

=================================
Scripts (Job submission file)
=================================

A job submission file can contain any of the commands that you would otherwise issue yourself from the command line. It is, for example possible to both compile and run a program and also to set any necessary environment values (though remember that SLURM exports the environment variables in your shell per default, so you can also just set them all there before submitting the job).
The results from compiling or running your programs can generally be seen after the job has completed, though as SLURM will write to the output file during the run, some results will be available quicker.

Outputs and any errors will per default be placed in the directory you are running from. Note that this directory should preferrably be placed under the parallel filesystem, since that is the only filesystem the batch system have access to easily.
Both output and errors will, by default, be combined into a file named slurm-<jobid>.out. You can send them to other/separate files with these commands:

::

    #SBATCH --error=job.%J.err
    #SBATCH --output=job.%J.out

These are prefixed with "#SBATCH" and otherwise use the same keywords and syntax as the command line options described for the sbatch command. The following script presents a minimal example:
Example

::

    #!/bin/bash
    #SBATCH --job-name=simplescript #show up in the output of 'squeue'
    #SBATCH --error=job.%J.err      # job error log
    #SBATCH --output=job.%J.out     # job output
    srun /bin/echo "Hello World!"

----------------------------------------------------
Simple Batch Script For Running MPI-Parallel Jobs
----------------------------------------------------

Note: The following example script assumes that you submit the script from the directory where the code will be executed (the path to that directory is stored in the

::

    $SLURM_SUBMIT_DIR

environment variable, and is where SLURM will execute the script from).

::

    #!/bin/bash
    #
    # SLURM resource specifications
    # (use an extra '#' in front of SBATCH to comment-out any unused options)
    #
    #SBATCH --job-name=simplempi   # shows up in the output of 'squeue'
    #SBATCH --time=4-23:59:59       # specify the requested wall-time
    #SBATCH --nodes=4               # -n number of nodes allocated for this job
    #SBATCH --ntasks-per-node=20    # number of MPI ranks per node
    #SBATCH --cpus-per-task=1       # -c number of OpenMP threads per MPI rank
    ##SBATCH --exclude=<node list>  # avoid nodes (e.g. --exclude=node786)

    # If required, replace specific modules
    # module unload intelmpi
    # module load mvapich2

    # When compiling remember to use the same environment and modules

    # Execute the code
    srun <executable> [args...]

----------------------------------------------------
Simple Batch Script For Jobs Using OpenMP Only
----------------------------------------------------

Note: The following example script assumes that you submit the script from the directory where the code will be executed (the path to that directory is stored in the

::

    $SLURM_SUBMIT_DIR

environment variable).
Note: By choosing

::

    --cpus-per-task=40

along with

::

    --ntasks-per-core=2

, you have assumed that your program will take advantage of hyper threading. If this is not the case, or you are uncertain, use

::

    --cpus-per-task=20

along with

::

    --ntasks-per-core=1

, and your program will be executed with 20 threads.

::

    #!/bin/bash
    #
    # Define SLURM resource specifications
    # (use an extra '#' in front of SBATCH to comment-out any unused options)
    #
    #SBATCH --job-name=openmpjob   # shows up in the output of 'squeue'
    #SBATCH --time=4-23:59:59       # specify the requested wall-time
    #SBATCH --cpus-per-task=40      # total number of threads
    #SBATCH --ntasks-per-core=2     # threads per core (hyper-threading)
    ##SBATCH --exclude=<node list>  # avoid nodes (e.g. --exclude=node786)

    # Load default settings for environment variables
    module load astro

    # OpenMP affinity
    # no hyperthreading
    # export KMP_AFFINITY="granularity=core,scatter,1,0"
    # hyperthreading
    export KMP_AFFINITY="granularity=thread,scatter,1,0"

    # When compiling remember to use the same environment

    # Execute the code
    srun --cpu_bind=threads <executable> [args...]

----------------------------------------------------
Hybrid MPI + OpenMP Batch Script:
----------------------------------------------------

Note: The following example script assumes that you submit the script from the directory where the code will be executed (the path to that directory is stored in the

::

    $SLURM_SUBMIT_DIR

environment variable, and is where SLURM will execute the script from).

::

    #!/bin/bash
    #
    # Define SLURM resource specifications
    # (use an extra '#' in front of SBATCH to comment-out any unused options)
    #
    #SBATCH --job-name=hybridopenmpmpijob   # shows up in the output of 'squeue'
    #SBATCH --time=4-23:59:59       # specify the requested wall-time
    #SBATCH --nodes=32              # number of nodes allocated for this job
    #SBATCH --ntasks-per-node=8     # lower than the usual 20 for MPI only
    #SBATCH --cpus-per-task=5       # number of CPUs per MPI rank
    #SBATCH --ntasks-per-core=2     # threads per core (hyper-threading)
    ##SBATCH --exclude=<node list>  # avoid nodes (e.g. --exclude=node786)

    # Load default settings for environment variables
    module load astro

    # OpenMP affinity
    export KMP_AFFINITY="granularity=thread,scatter,1,0"

    # If required, replace specific modules
    # module unload intelmpi
    # module load mvapich2

    # When compiling remember to use the same environment and modules

    # Execute the code
    cd $SLURM_SUBMIT_DIR
    srun --cpu_bind=threads <executable> [args...]

----------------------------------------------------
Embarrassingly Parrallel Workload Examples
----------------------------------------------------

This setup is useful for problems based on random draws (e.g. Monte-Carlo simulations). In such cases, you can have four programs drawing 1000 random samples and combining their output afterwards (with another program) you get the equivalent of drawing 4000 samples.

Another typical use of this setting is parameter sweep. In this case the same computation is carried on several times by a given code, differing only in the initial value of some high-level parameter for each run. An example could be the optimisation of an integer-valued parameter through range scanning:

::

    #!/bin/bash
    #
    #SBATCH --job-name=test_emb_arr
    #SBATCH --output=res_emb_arr.txt
    #
    #SBATCH --ntasks=1
    #SBATCH --time=10:00
    #SBATCH --mem-per-cpu=100
    #
    #SBATCH --array=1-8

    srun ./my_program.exe $SLURM_ARRAY_TASK_ID

In that configuration, the command my_program.exe will be run eight times, creating eight distinct jobs, each time with a different argument passed with the environment variable defined by slurm SLURM_ARRAY_TASK_ID ranging from 1 to 8.

The same idea can be used to process several data files. To different instances of the program we must pass a different file to read, based upon the value set in the $SLURM_* environment variable. For instance, assuming there are exactly eight files in /path/to/data we can create the following script:

::

    #!/bin/bash
    #
    #SBATCH --job-name=test_emb_arr
    #SBATCH --output=res_emb_arr.txt
    #
    #SBATCH --ntasks=1
    #SBATCH --time=10:00
    #SBATCH --mem-per-cpu=100
    #
    #SBATCH --array=0-7

    FILES=(/path/to/data/*)

    srun ./my_program.exe ${FILES[$SLURM_ARRAY_TASK_ID]}

In this case, eight jobs will be submitted, each with a different filename given as an argument to my_program.exe defined in the array FILES[ ]. As the FILES[ ] Bash array is zero-indexed, the Slurm job array IDs must also start at 0 so the argument is --array=0-7. One pain point is that the number of files in the directory must match the number of jobs in the array.

Note that the same recipe can be used with a numerical argument that is not simply an integer sequence, by defining a Bash array ARGS[ ] containing the desired values:

::

    ARGS=(0.05 0.25 0.5 1 2 5 100)

    srun ./my_program.exe ${ARGS[$SLURM_ARRAY_TASK_ID]}

Here again, the Slurm job array numbering must start at 0 to make sure all items in the ARGS[ ] Bash array are processed.

=================================
Job Status
=================================

-------
squeue
-------

Use The 'Squeue' command To display information about scheduled jobs, -u with username to see your jobs only

::

    $ squeue
    $ squeue -u <username>
    $ squeue -l -u
    $ squeue -l -u <username> -p <partition name>


-------
queue
-------

To only view the jobs in the largemem partition on Kebnekaise

::

    $ queue -p largemem

--------
scontrol
--------

Get the status of an individual job

::

    $ scontrol show job <jobid>

=================================
Job Cancellation
=================================

To cancel a job, use scancel. You need the running or pending jobid. It is only the job's owner and SLURM administrators that can cancel jobs.

::

    $ scancel <jobid>

To cancel all your jobs (running and pending) you can run

::

    $ scancel -u <username>

You get the job id when you submit the job

::

    $ sbatch -N 1 -n 4 submitfile
    Submitted batch job 173079
    $ scancel 173079

Or through squeue

::

    $ squeue -u <username>

Alternatively, you can cancel a job submitted by srun or in an interactive shell, with salloc, by pressing Ctrl-C. In the example below, we have asked to start an interactive job, which we then cancel during waiting.

::

    $ salloc -N 2 -n 4
    salloc: Pending job allocation 779
    salloc: job 779 queued and waiting for resources
    ^Csalloc: Job allocation 779 has been revoked.
    salloc: Job aborted due to signal

Note Do not kill/skill srun to cancel a SLURM job! Doing so only terminates srun. The tasks continue to run, but not under SLURM management. If you do kill/skill an srun job, you can use squeue to get the job id and then either scancel the job, or use srun -p <partition> -a <jobid> -j, to reattach srun to the job and then you can use Ctrl-C to cancel it.

=================================
GPU Jobs
=================================

Microway gpu-burn is a free software of stress test for GPU clusters. Here we take it as an example to run jobs with gpu.
gpu_burn.sh is the example of script to run gpu_burn. In the script, you need to specify --partition to V100 or A100 and --gres for numbers of your request gpu cards.
Export the path of CUDA package to /usr/local/cuda in the GPU clusters.

You may find this program and scripts in /ceph/astro_phys/user_document/gpu/

::

    $ vim gpu_burn.sh
    !/bin/bash
    #SBATCH --partition=v100
    #SBATCH --gres=gpu:8

    export CUDA_PATH=/usr/local/cuda/
    make
    ./gpu_burn -d 300

