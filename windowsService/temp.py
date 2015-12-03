__author__ = 'Frenky'


import win32event
import win32service
import win32serviceutil
import win32service
import win32serviceutil
import win32event
import win32con
import win32api
import subprocess
import time
import datetime



# d3 = datetime.date.today() + datetime.timedelta(31)
#
# print d3




# dt1 = datetime.datetime(2011, 03, 03, 11, 12)
# day = datetime.date(2011, 03, 02)
# dt2 = datetime.datetime.combine(day, datetime.time(0, 0))
#
# print dt1 > dt2






import urllib2

#url = "http://download.thinkbroadband.com/10MB.zip"
#url = "http://media.zenfs.com/en-US/video/video.pd2upload.com/video.yahoofinance.com@fc01f40d-8f4e-3cbc-9d8f-a7b9e79d95fd_FULL.jpg"
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