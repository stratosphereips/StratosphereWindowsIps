__author__ = 'Frenky'


import ConfigParser


file_name = 'configfile.cfg'
config = ConfigParser.RawConfigParser()
config.read(file_name)

try:
    running = config.getboolean('Section1', "running")
    if running:
        #Nothing to do.
        print "Program is running."
    else:
        #Create new process by " CreateProcessAsUser" in session 1
        print "Start program again!"
except:
    print "No config Variable!"
    config.add_section('Section1')
    config.set('Section1', 'running', 'False')
    with open(file_name, 'wb') as configfile:
        config.write(configfile)