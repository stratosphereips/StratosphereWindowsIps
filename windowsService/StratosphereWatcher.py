__author__ = 'Frenky'

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
#
# time to config file
# qt - graphicakl lib nfor gui
#
# Piping
# echo" karel" | grep "karel"



def download_upadte(url):
   print 'Downloading updates.'
   #url = "https://raw.githubusercontent.com/stratosphereips/StratosphereIps/Frenky/windowsService/configfile_check.py"

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
       file_size_dl = len(buffer)
       f.write(buffer)
       status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
       status =status + chr(8)*(len(status)+1)
       print status,

   f.close()


def set_config(days_update_again):
   print 'Setting Config file.'
   next_update = datetime.date.today() + datetime.timedelta(days_update_again)

   file_name = 'configfile.cfg'
   config = ConfigParser.RawConfigParser()
   config.read(file_name)
   config.set('STRATOSPHERE_WINDOW','DATE_OF_NEXT_UPDATE', next_update)
   with open(file_name, 'wb') as configfile:
       config.write(configfile)


def check_config():
   file_name = 'configfile.cfg'
   config = ConfigParser.RawConfigParser()
   config.read(file_name)
   try:
       days_update_again = config.getint('STRATOSPHERE_WINDOW', 'DAYS_UPDATE_AGAIN')
       is_forbidden = config.getboolean('STRATOSPHERE_WINDOW', 'DONT_UPDATE')
       date_string = config.get('STRATOSPHERE_WINDOW', 'DATE_OF_NEXT_UPDATE')
       url_string = config.get('STRATOSPHERE_WINDOW', 'UPDATE_URL')

       date_upadte = datetime.datetime.strptime(date_string, '%Y-%m-%d')
       date_now = datetime.datetime.now()

       if date_upadte < date_now:
           if is_forbidden is False:
               print 'Downloading new update.'
               download_upadte(url_string)
               print 'Set config file'
               set_config(days_update_again)
           else:
                print "Updating is forbidden!"
   except:
       print 'There is no config file or config file is not valid.'
       print 'Creating new config file.'

       # FIRST SECTION
       config.add_section('STRATOSPHERE_WINDOW')
       config.set('STRATOSPHERE_WINDOW', 'DONT_UPDATE', 'False')
       config.set('STRATOSPHERE_WINDOW', 'DATE_OF_NEXT_UPDATE', datetime.date.today())
       config.set('STRATOSPHERE_WINDOW', 'DAYS_UPDATE_AGAIN', '3')
       config.set('STRATOSPHERE_WINDOW', 'CHECK_IF_UP_EVERY', '3')
       config.set('STRATOSPHERE_WINDOW', 'UPDATE_URL', 'https://raw.githubusercontent.com/stratosphereips/StratosphereIps/Frenky/windowsService/configfile_check.py')
       # SECOND SECTION
       config.add_section('STRATOSPHERE_WATCHER')
       config.set('STRATOSPHERE_WATCHER', 'RUN_ON_START_UP', 'True')

       with open(file_name, 'wb') as configfile:
           config.write(configfile)

 
if __name__ == "__main__":
   # check config file
   check_config()
   # Path to Stratospehere Window
   path = 'C:\Users\Frenky\Documents\Skola\Stratosphere\windowsService\StratosphereWindow.py'
   # Create process.
   p = subprocess.Popen('python ' +path, shell=True)
   # Wait until process terminates.
   while True:
       if p.poll() is None:
           print "Process is still runnning..."
           time.sleep(3)
       else:
           p = subprocess.Popen('python '+ path, shell=True)
   print "Process ended, ret code:", p.returncode