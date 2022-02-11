CryoEM Priority User Guide 
==============================

1. What's different between Priority user queue (PQ) and generic user queue (GQ)?

   -  PQ users have dedicated CPU cluster resource, which allows user to do more CPU intensive computing.

2. How to use such PQ cluster resource?

  - If user is in priority user list, user will see specific PQ app to launch in DiCOSApp list.
  - However, PQ APP uses slurm as cluster resource manager, so, user must do a bit configuration for cisTEM as mentioned at 3).

3. How to configure PQ cisTEM.

   - Leave "Manager Command" as what it is.
   - There is provisioned job script, just need to modify the **Command** option for each run profile to look like:
       sbatch /opt/hpc_soft/cryoEM/job.sh $command
   - Please adjust number of copies accordingly to your jobs scale.
     -The maximum copies(core numbers) will be 60 per user.

   - The screenshot below is what it will look like:

     * cisTEM command configuration

     .. image:: cryoem_priority_user_guide/image/Screenshot_20190513_202812.png

     * Completed cisTEM command configuration

     .. image:: cryoem_priority_user_guide/image/cisTEM_PQ_set.png

4. Since PQ cluster is isolated resource, so, we need to copy data into cluster storage. The cluster storage is mounted at:

   ::

      /cluster_storage/</br>

   - User can only access their group directory at ``/cluster_storage``
   - Please also be aware, the cluster_storage is not meant for long term storage, so, please remember to copy your output back to your $HOME/data or /cryoem_user/scratch/data/ **

5. Please note that, cisTEM user project must be created under /cluster_storage/ as well.
6. How to configure RELION for PQ?

  - RELIOM is pre-configured to use sbatch by default, so, user doesn't have to do any thing.


