
import win32service
import win32serviceutil
import win32event
import servicemanager
import pythoncom
import winsound
import logging
import socket
import os
import traceback
import subprocess



def launchWithoutConsole(command, args):
   """Launches 'command' windowless"""
   startupinfo = subprocess.STARTUPINFO()
   startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

   return subprocess.Popen([command] + args, startupinfo=startupinfo,
                    stderr=subprocess.PIPE, stdout=subprocess.PIPE)

logging.basicConfig(
    filename = 'c:\\Windows\\Temp\\hello-service2.log',
    level = logging.DEBUG,
    format = '[helloworld-service2] %(levelname)-7.7s %(message)s'
)

class AppServerSvc(win32serviceutil.ServiceFramework):
    _svc_name_ = "MyService1"
    _svc_display_name_ = "Test Service1"
    #_svc_description_ = "This service writes stuff to a file"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        #socket.setdefaulttimeout(60)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        logging.info('Running ...')

        #self.run = True
        try:
            self.new_function()
        except:
            servicemanager.LogErrorMsg(traceback.format_exc())  # if error print it to event log
            os._exit(-1)  # return some value other than 0 to os so that service knows to restart


    def new_function(self):
        logging.info('Testing my function')

        #os.system("C:\\Windows\\Temp\\notepad++.lnk")
        #os.system('"C:/Windows/System32/notepad.exe"')
        #os.system('"C:/Windows/System32/notepad.exe"')
        #subprocess.call(["C:\\Windows\\System32\\notepad.exe"])

        process = launchWithoutConsole("c:\\Windows\\System32\\notepad.exe", ["-ahojJardo"])
        stderr, stdout = process.communicate()


        f = open('c:\\Windows\\Temp\\test_frenky.dat', 'w+')
        f.write('ahoj prde\n')
        f.write('jak se mas\n')
        f.write('mam se dobre...\n')
        f.flush()
        f.close()

        rc = None
        while rc != win32event.WAIT_OBJECT_0:
            rc = win32event.WaitForSingleObject(self.hWaitStop, 3000)



if __name__ == '__main__':
    winsound.Beep(2500, 500)
    logging.info('Starting service ...')
    win32serviceutil.HandleCommandLine(AppServerSvc)



("\"\n"
 "class PySvc(win32serviceutil.ServiceFramework):\n"
 "    # you can NET START/STOP the service by the following name  \n"
 "    _svc_name_ = \"PySvc\"\n"
 "    # this text shows up as the service name in the Service  \n"
 "    # Control Manager (SCM)  \n"
 "    _svc_display_name_ = \"Python Test Service\"\n"
 "    # this text shows up as the description in the SCM  \n"
 "    _svc_description_ = \"This service writes stuff to a file\"\n"
 "\n"
 "    def __init__(self, args):\n"
 "        win32serviceutil.ServiceFramework.__init__(self, args)\n"
 "        # create an event to listen for stop requests on  \n"
 "        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)\n"
 "\n"
 "    # core logic of the service\n"
 "    def SvcDoRun(self):\n"
 "        #print(\"jsem v run....\")\n"
 "\n"
 "        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,\n"
 "                              servicemanager.PYS_SERVICE_STARTED,\n"
 "                              (self._svc_name_,''))\n"
 "\n"
 "        freq = 2500\n"
 "        length = 1000\n"
 "        winsound.Beep(freq, length)\n"
 "\n"
 "        f = open('test.dat', 'w+')\n"
 "        rc = None\n"
 "\n"
 "\n"
 "        # if the stop event hasn't been fired keep looping\n"
 "        while rc != win32event.WAIT_OBJECT_0:\n"
 "            f.write('TEST DATA\n')\n"
 "            f.flush()\n"
 "            winsound.Beep(freq, length)\n"
 "            # block for 5 seconds and listen for a stop event\n"
 "            rc = win32event.WaitForSingleObject(self.hWaitStop, 3000)\n"
 "\n"
 "        f.write('SHUTTING DOWN\n')\n"
 "        f.close()\n"
 "\n"
 "    # called when we're being shut down      \n"
 "    def SvcStop(self):\n"
 "        # tell the SCM we're shutting down\n"
 "        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)\n"
 "        # fire the stop event\n"
 "        win32event.SetEvent(self.hWaitStop)\n"
 "\n"
 "\n"
 "if __name__ == '__main__':\n"
 "    freq = 2500\n"
 "    length = 500\n"
 "    winsound.Beep(freq, length)\n"
 "    win32serviceutil.HandleCommandLine(PySvc)\n"
 "")
