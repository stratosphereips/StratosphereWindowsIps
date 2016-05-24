# Stratosphere Windows IPS
Stratosphere Windows IPS is the Microsoft version of the Startosphere IPS project. The tool runs in the same way as the Stratosphere Linux IPS, but using windows libraries.
This tool is provided for being used by personal users in their computers. The tool can provide a reliable detection of malicious connections based on the download models. Please note that this tool is still Beta.

# How to Use it

There are three ways of using the Stratosphere Windows IPS. By giving the binetflow file as parameter, by reading the binetflow file from StdIn, or by reading the flows from an Argus tool by StdIn. If you want to analyze your own traffic to make detections, you need to install an Argus program
in some computer that has accesss to the traffic. The Argus program can run under the same Windows computer (see [Installation of Argus under Windows](#installation of argus under windows)) or can be run in any other computer.
If the Argus server is running in other computer, you still need to have the ra program (from Argus client tools) running in the Windows computer with Stratosphere Windows IPS.


## Runing it by giving the binetflows file as paramter:
To give the binetflow file as a parameter, just put the name of the file after the StratosphereWatcher program

        python your_path\StratosphereWatcher.py test7.binetflow

The test7.binetflow file is provided as an example. The StratosphereWatcher.py program will first download some necessary files from the Internet and then it will run the detection on the binetflow file. 
    See the following sections to know exactly what StratosphereWatcher.py is doing.

## Running it by reading the flows from StdIn
This method can be used to read a file or to read the flows from an ra program (Argus client suite).

### From a file

    cat test7.binetflow | python StratosphereFlow.py

This possibility is better for fast case, because there is not checking updates.
Caution: For first running this program, you use first case for running. The reason is config file, which is created in StratosphereWatcher.

# Configuration
This program 
You can also manage the configuration file, where are some features for this program.

# Files in project
## StratosphereWatcher.py 

- downloading updates and files
- creating process
- in future it shoud start windows service.

## StratosphereFlow.py

- it takes flows from stdin
- it decides when tim_window starts and ends
- it stores flows in queue
- it stores tuple object a ip 

## StratosphereTuple.py

- it creates tuple_objects
- one tuple object has a list of flows
- it computes state for current tuple

## StratosphereDetector.py
- it calles modules for detecting.

## StratosphereConfig.py
- it creates config file with implicit settings, if there is no config file.

## StratosphereOutput.py
- For printing a logging.

# Installation of Argus under Windows

# TODO:
- create install app.
- runable argus.
- windows service


