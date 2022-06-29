********************************
Frequent Asked Questions (FAQ)
********************************

.. sectionauthor:: Felix Lee <felix@twgrid.org>, Mike Yang <mike.yang@twgrid.org>

---------------------------
General
---------------------------

How could I know the computing environment (including the library, compiler, etc.) of DiCOS ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are using ``slurm_ui``, the software stacks are maintained with the environment-modules software. Please follow `this link <https://dicos-document.readthedocs.io/en/latest/slurm_job_submission.html#environment-modules>`_ for the instruction. 

Please contact us by e-mail (DiCOS-Support@twgrid.org) or fill the form in `this link <https://dicos.grid.sinica.edu.tw/contact>`_ for any required system software.

How to use the Command Line Interface in DiCOS?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Login to ``dicos-ui05.grid.sinica.edu.tw`` by using the account/password used in the DiCOS Web User Interface.  

When I login in ``dicos-ui04.grid.sinica.edu.tw``, I got port:22 connection denial. Why?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It's most likely that you are banned due to multiple login failures with your IP address. Please wait for 2 to 3 hours then try again. Or use other machines to login. If your forget your password, please use `this link <https://canew.twgrid.org/ApplyAccount/nocertModify.php>`_ to reset your password.

---------------------------
DiCOS Job System
---------------------------

When I use ``dicos ddm download`` command, it failed with the following messages: **[2022-04-12 03:35:31,188 ERROR] Failed to download**. What happened?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There should be something wrong with our DDM subsystem. You can use ``dicos ddm ping`` to check if it returns: ``Ping Rucio OK !`` message. If not, please contact to DiCOS-Support@twgrid.org to report the issue. Thank you.

---------------------------
Slurm
---------------------------

How do I know the current usage/vacancy of specific machine of slurm?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For example, we could use the following command to get the status of hp-teslav01:

.. code-block:: bash

   sinfo --format="%10n %.14C %.10T" -n hp-teslav01

---------------------------
DiCOSApp
---------------------------

-------------------------------------------------------------------------------------------------------
How to get a Cryosparc license?
-------------------------------------------------------------------------------------------------------

CryoSPARC™ and cryoSPARC Live™ are available free of charge for non-profit academic use. Please go to https://cryosparc.com/download to apply your own Cryosparc license and then import it when you launch Cryosparc application.  

-------------------------------------------------------------------------------------------------------
Why I cannot click the launch button of specific DiCOSApp?
-------------------------------------------------------------------------------------------------------

There are some reasons cause this issue:

* There are no sufficient resources left for the requirements of your application
* The application is now in maintenance mode (please see relative announcements)

-------------------------------------------------------------------------------------------------------
What happened that I cannot launch specific DiCOSApp even if the launch button is clickable?
-------------------------------------------------------------------------------------------------------

There should be some technical issues of our microservice, please contact ``DiCOS-Support@twgrid.org`` for quick solution.

