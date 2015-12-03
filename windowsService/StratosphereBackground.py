__author__ = 'Frenky'

import os
import signal
import subprocess
import tempfile
import time
import sys
import ConfigParser
import logging
import datetime
import ConfigParser
import datetime
import urllib2


##### POINTS #####
# run process from bash script
# cmd = "sh C:\\Users\\Frenky\\bash01.sh"
# p = subprocess.Popen(cmd , shell=True)
######
# subprocess.call(['python', 'somescript.py', somescript_arg1, somescript_val1,...])

######
# udelej SW a kontroluj v list process, zda SW bezi....pokud ne ynovu zapni
# udelej cteni a vkladani casi do config file
# udelej to aby SB se zaplo po yapnuti pc.. naka ta sloyka roaming.....
#####



def download_upadte():
    print 'Downloading updates.'
    url = "https://raw.githubusercontent.com/stratosphereips/StratosphereIps/Frenky/windowsService/configfile_check.py"

    file_name = url.split('/')[-1]
    u = urllib2.urlopen(url)
    f = open(file_name, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (file_name, file_size)

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print status,

    f.close()


def set_config(days_update_again):
    print 'Setting Config file.'
    next_update = datetime.date.today() + datetime.timedelta(days_update_again)

    file_name = 'configfile.cfg'
    config = ConfigParser.RawConfigParser()
    config.read(file_name)
    config.set('Section2','time', next_update)
    with open(file_name, 'wb') as configfile:
        config.write(configfile)



def check_config():
    file_name = 'configfile.cfg'
    config = ConfigParser.RawConfigParser()
    config.read(file_name)
    try:
        days_update_again = config.getint('Section3', 'days_update_again')

        is_forbidden = config.getboolean('Section1', 'IsForbidden')

        date_string = config.get('Section2', 'time')
        date_upadte = datetime.datetime.strptime(date_string, '%Y-%m-%d')
        date_now = datetime.datetime.now()
        if date_upadte < date_now:
            if is_forbidden is False:
                print 'Downloading new update.'
                download_upadte()
                print 'Set config file'
                set_config(days_update_again)
            else:
                 print "Updating is forbidden!"
    except:
        print 'There is no config file or config file is not valid.'
        config.add_section('Section1')
        config.set('Section1', 'IsForbidden', 'False')
        config.add_section('Section2')
        config.set('Section2','time', datetime.date.today())
        config.add_section('Section3')
        config.set('Section3', 'days_update_again', '3')
        with open(file_name, 'wb') as configfile:
            config.write(configfile)




if __name__ == "__main__":
    # check config file
    check_config()

    # Create process.
    p = subprocess.Popen('python C:\Users\Frenky\Documents\Skola\Stratosphere\windowsService\StratosphereWindow.py', shell=True)
    # Wait until process terminates.
    while True:

        if p.poll() is None:
            print "Process is still runnning..."
            time.sleep(3)
        else:
            p = subprocess.Popen('python C:\Users\Frenky\Documents\Skola\Stratosphere\windowsService\StratosphereWindow.py', shell=True)

    print "Process ended, ret code:", p.returncode
