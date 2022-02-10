RELION Job Configuration
========================================

* Q: What's the ideal MPI number and thread number with current RELION APP?

  - A: *4 MPI* with *4 threads*. If it's GPU accelerated process, please use *5 MPI* with *4 threads*

* Q: What's the ideal MPI number and thread number with Premium RELION v100 app?

  - A: The v100 GPU is relatively powerful GPU against GTX-1080Ti. So, it can bear much load than 1080ti. In principle, with following job setup, user can get pretty nice speed up when dealing 2D and 3D classifications:

    * *2D*: Number of *MPI procs: 16*, Number of *Threads: 1*
    * *3D*: Number of *MPI procs: 9*, Number of *Threads: 2*

* Q: What if RELION encounters error?

  - A: RELION is often stable. When error occurs, it would usually caused by:

     #. Memory or resources are not enough. For such error, simply reducing Thread number would just help. If the error lasts, then try reducing MPI number.
     #. Input file error. Checking log and removing problematic file indicated in log may just solve this issue.
