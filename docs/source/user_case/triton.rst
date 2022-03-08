*******************************************************
Use Triton inference server with DiCOS System
*******************************************************

.. sectionauthor:: Mike Yang <mike.yang@twgrid.org>


-------------------------------------
Triton Scheme
-------------------------------------
![](/uploads/upload_5ac230455600e32a79c3e1cb295c8df7.png)

-------------------------------------
Triton Server
-------------------------------------
* Using DiCOSAPP to start the Triton server
* Ports will be revealed when the container is started
  - http port
  - grpc port
  - metric port (not opened)
* Specficiations of the image:
  - Triton inference server 2.18
  - P100 GPU x 2
  - CPU x 4
  - Memory: 96 GB
* Usage:
  - Start the Triton DiCOSAPP from DiCOS web
  ![](/uploads/upload_4deb416680e3d7d2ba599022e14da8db.png =400x)
  - When the server start running, you will see the following boxes
  ![](/uploads/upload_8ef756a478a3e452806a7a9c9f1a6af1.png =400x)

  - Get the API port from the DiCOSAPP web page by press **Open** button, ports will be listed
    - HTTP
    - gRPC
  ![](/uploads/upload_a7702ca08c26563c76e2484684ef6e37.png =400x)


  - Run your Triton client (see next section) to communicate with the server
  - Note:
    - The DiCOSAPP of Triton server is only accessable in the DiCOS resources for security reason
    - The API server will be: **k8s-master01.twgrid.org**
    
    
-------------------------------------
Upload Your Model
-------------------------------------

* Currently, we have desginated a ceph path as the model_repository path of the Triton inference server for the users:
  - You could put your file in **/ceph/sharedfs/groups/KAGRA/model_repository**
    - Note:
      - The space will be accounted as KAGRA group user space
      - If you are using DiCOS submit, at this stage, only QDR2 and FDR5 cluster will have access on the /ceph partition
* You could put your customized models to the model directory no matter the Triton server is running or not

-------------------------------------
Triton Client
-------------------------------------
There are two different ways to submit your Triton client to our worker nodes:
  1. DiCOS submit (from dicos-ui05.grid.sinica.edu.tw or dicos-ui06.grid.sinica.edu.tw)
    - Because you are requesting CPU resources, so there is no need to specify the queue with GPU resources
  2. Slurm submit (from slurm-ui01.twgrid.org)
  
Singularity Container
^^^^^^^^^^^^^^^^^^^^^^^^

If you are using python as your programming language for the API access. A singularity image has been built for your usage. Location: **/ceph/astro_phys/singularity_image/python_tritonclient_slim-buster.sif**

Test Programs
^^^^^^^^^^^^^^^^^^^^^^^^

You may get the following test programs from the Triton github repository (https://github.com/triton-inference-server/client/tree/main/src/python/examples):
* simple_grpc_keepalive_client.py
* simple_http_health_metadata.py

A simple test program in shell could be written as (test.sh):

.. code-block:: bash

   server=k8s-master01.twgrid.org
   echo "TEST HTTP"
   wd=$PWD
   http_port=31443 # 8000 port of original triton server
   grpc_port=30457 # 8001 port of original triton server
   python3 $wd/simple_http_health_metadata.py -u $server:$http_port
   echo "----------------------"
   echo "TEST gRPC"
   python3 $wd/simple_grpc_keepalive_client.py -u $server:$grpc_port
   echo "----------------------"

A customized script utlize the singularity container could be written as (start_singularity.sh):

.. code-block:: bash

   #!/bin/bash
   
   singularity instance start /ceph/astro_phys/singularity_image/python_tritonclient_slim-buster.sif triton_client
   singularity exec instance://triton_client bash $PWD/test.sh

DiCOS Submit
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   dicos job submit -i . -c "bash start_singularity.sh" -N triton -j 1

Slurm Submit
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   sbatch start_singularity.sh


------------------
Accounting
------------------

* DiCOSAPP will account for it's GPU and CPU resources
* DiCOS job/slurm job will account for it's CPU resources

