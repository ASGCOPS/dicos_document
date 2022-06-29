********************************
Frequent Asked Questions (FAQ)
********************************

.. sectionauthor:: Felix Lee <felix@twgrid.org>, Mike Yang <mike.yang@twgrid.org>

---------------------------
General
---------------------------

How could I know the computing environment (including the library, compiler, etc.) of DiCOS ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Please contact us by e-mail (DiCOS-Support@twgrid.org) or fill the form in https://dicos.grid.sinica.edu.tw/contact for any required system software.

How to use the Command Line Interface in DiCOS?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Login to ``dicos-ui05.grid.sinica.edu.tw`` by using the account/password used in the DiCOS Web User Interface.  

When I login in ``dicos-ui04.grid.sinica.edu.tw``, I got port:22 connection denial. Why?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It's most likely that you are banned due to multiple login failures with your IP address. Please wait for 2 to 3 hours then try again. Or use other machines to login. If your forget your password, please use `this link <https://canew.twgrid.org/ApplyAccount/nocertModify.php>`_ to reset your password.

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
How to get Cryosparc license?
-------------------------------------------------------------------------------------------------------

CryoSPARC™ and cryoSPARC Live™ are available free of charge for non-profit academic use. Please go to https://cryosparc.com/download to apply your own Cryosparc license and then import it when you launch Cryosparc application.  

-------------------------------------------------------------------------------------------------------
Why I cannot click the launch button of specific DiCOSApp?
-------------------------------------------------------------------------------------------------------

There are some reasons cause this issue:

* There is no enough resources left for your application
* The application is now in maintenance mode (please see relative announcements)

-------------------------------------------------------------------------------------------------------
What happened that I cannot launch specific DiCOSApp even if the launch button is clickable?
-------------------------------------------------------------------------------------------------------

There show be some technical issues of our microservice, please contact ``DiCOS-Support@twgrid.org`` for quick solution.

