# Stratosphere Windows IPS
Stratosphere Windows IPS is the Microsoft version of the Stratosphere IPS project. The tool runs in the same way as the Stratosphere Linux IPS, but using windows libraries.
This tool is provided for being used by personal users in their computers. The tool can provide a reliable detection of malicious connections based on the download models. Please note that this tool is still Beta.
See the oficial web page of the [Stratosphere Project](https://stratosphereips.org)

# How to Use it

There are three ways of using the Stratosphere Windows IPS. By giving the binetflow file as parameter, by reading the binetflow file from Stdin, or by reading the flows from an Argus tool by Stdin. If you want to analyze your own traffic to make detections, you need to install an Argus program
in some computer that has access to the traffic. The Argus program can run under the same Windows computer (see [Installation of Argus under Windows](#installation of argus under windows)) or can be run in any other computer.
If the Argus server is running in other computer, you still need to have the ra program (from Argus client tools) running in the Windows computer with Stratosphere Windows IPS.


## Running it by giving the binetflows file as parameter:
To give the binetflow file as a parameter, just put the name of the file after the StratosphereWatcher program

        python your_path\StratosphereWatcher.py test7.binetflow

The test7.binetflow file is provided as an example. The StratosphereWatcher.py program will first download some necessary files from the Internet and then it will run the detection on the binetflow file. 
    See the following sections to know exactly what StratosphereWatcher.py is doing.

## Running it by reading the flows from Stdin
This method can be used to read the flows using Stdin from a file or to read the flows from a ra program (Argus client suite).

### From a file
To read the flows from a file do

    cat test7.binetflow | python StratosphereFlow.py

Note that we are using now StratosphereFlow.py directly. This is because the StratosphereWatcher takes care of the download of models and that the service is running continually. In this case, StratosphereFlow.py read the flows directly without any update.
To be able to use this way of reading a file from Stdin, Stratosphere still needs to create its configuration file, that is way at first is better to run it at least once with the file as a parameter.

## From an Argus installation
If you have Argus running in Windows you can start the Argus server in your network like this

    argus -i <name of your windows network device>

And then you can run Startosphere like this

    ra -n -Z b -S localhost | python StratosphereFlow.py

In case the Argus program is running in other computer, you can connect to it and analyze the flows in your Windows like this

    ra -n -Z b -S remote-host:remote-port | python StratosphereFlow.py

# Configuration
Stratosphere Windows IPS uses a configuration file to tune its behavior. This file is automatically created when you run StratosphereWatcher.py. After the configuration file is created, you can manually edit it and the program will notice and honor the changes. 


# What each files does in Stratosphere Windows IPS
## StratosphereWatcher.py 

- Downloads updates, models files and modules files.
- Creating the main detection process
- In the future it should start windows service.

## StratosphereFlow.py

- It can read flows from Stdin.
- It decides when the  time window of the detection starts and ends.
- It stores the flows in a queue.
- It manages the tuple objects.

## StratosphereTuple.py

- It creates the tuple objects.
- It computes the state of the current tuple.

## StratosphereDetector.py
- It calls the modules for detecting.
- The modules are downloaded from the Internet and may be updated.

## StratosphereConfig.py
- It creates the config file with implicit settings if there is no config file.

## StratosphereOutput.py
- For printing a logging.

# Installation of Argus under Windows
Coming soon.

# TODO
- Create install app.
- Windows service
