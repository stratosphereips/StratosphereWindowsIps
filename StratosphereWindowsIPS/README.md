STRATOSPHERE WINDOWS IPS
=======

How to execute it ?
-----------
1.
Run comand line and put this:

python  your_path + \StratosphereWatcher.py arg1

where:

arg1 is path to binetflow file: your_path + \file.binetflow

Example:

"python C:\Users\User\Documents\StratosphereWindowsIPS\StratosphereWatcher.py C:\Users\User\Documents\StratosphereWindowsIPS\test7.binetflow"

First the program downloads necessary files and then runs. You can also manage the configuration file, where are some features for this program.

2.
Next way is:

"cat test7.binetflow | python StratosphereFlow.py"

This possibility is better for fast case, because there is not checking updates.
Caution: For first running this program, you use first case for running. The reason is config file, which is created in StratosphereWatcher.


Files in project
----------------------

StratosphereWatcher.py 
- downloading updates and files
- creating process
- in future it shoud start windows service.

StratosphereFlow.py
- it takes flows from stdin
- it decides when tim_window starts and ends
- it stores flows in queue
- it stores tuple object a ip 

StratosphereTuple.py
- it creates tuple_objects
- one tuple object has a list of flows
- it computes state for current tuple

StratosphereDetector.py
- it calles modules for detecting.

StratosphereConfig.py
- it creates config file with implicit settings, if there is no config file.

StratosphereOutput.py
- For printing a logging.


TODO:
---------------------
* create install app.
* runable argus.
* windows service

