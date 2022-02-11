What is the transformation script
===================================

==============
Description 
==============

You can call transformation script as job initiator, it's first script that pilot executes. It can be used to run job directly, but you can also use it to launch another script for much more complex works.


==============
Example
==============

``http://asgc-ui03.grid.sinica.edu.tw/panda/transformations/user/user.hlee/job-gen.py``

It's very simple transformation script written in python, you can use it to do most of works, here are what it does.

1. Extract json from panda.

    - All parameters will be passed to pilot from panda in json format, so, what we need to do is to extract those json parameters and pass them to your job scripts.

    - In most of cases, the json will look like following:

      ::
         {"files": ["ams-user-felixlee:Trigger_1368946224.00000001.root"], "params": "cat noDmFile0.txt", "output": "test02", "scope": "ams-user-felixlee", "userlib": ["ams-user-felixlee:ISS_Proton_Dec12_V1.tar.gz"]}

    - the job-gen.py will extract such key-value and store value them into file, it will use key+0.txt as file name, for example, "files": ["ams-user-felixlee:Trigger_1368946224.00000001.root"] will be stored as "files0.txt", and the contents will be(with DM, the file will be downloaded to local disk, so, scopename must be removed):

      ::

         Trigger_1368946224.00000001.root

    - In such cases, you can make your job to read files0.txt, so you can simply get input file and process it.

2. Run job accordingly by "parames" as "command1 ; command2 ; and so on"

    - It can be any unix command, shell script or your binaries.

3. Move all the files your job produced to ./outdir, and then, pilot will upload those files to storage.

    - It's important that the files must be moved to ./outdir, because pilot will only check that directory and upload everything under ./outdir to storages.

    - If you don't like the way that the job-gen.py does with outputs, you can mark MoveOutput('dir0.snapshot', outdir) as comment and use your own way to upload files.

4. Return job status to pilot. 
