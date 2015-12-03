__author__ = 'Frenky'

import win32service
import win32serviceutil
import win32event
import win32con
import win32api
import win32security
import win32process
import pywintypes
from subprocess import Popen
from win32process import DETACHED_PROCESS


# def attempt_to_logon():
#     username = "Frenky"
#     password = "karel"
#     try:
#         hUser = win32security.LogonUser(username, None,
#                                         password, win32security.LOGON32_LOGON_INTERACTIVE,
#                                         win32security.LOGON32_PROVIDER_DEFAULT)
#     except win32security.error:
#         print "unable to logon"
#         return None
#     return hUser
#
# def run_as_user(hUser):
#     startup = win32process.STARTUPINFO()
#     startup.dwFlags = win32process.STARTF_USESHOWWINDOW
#     startup.wShowWindow = win32con.SW_SHOW
#     startup.lpDesktop = 'winsta0\default'
#
#
#     try:
#         result = win32process.CreateProcessAsUser(hUser,
#                                                   None,  # appName
#                                                   "c:\\windows\\notepad.exe",  # notepad.exe
#                                                   None,  # process attrs
#                                                   None,  # thread attrs
#                                                   0,  # inherit handles
#                                                   0,  # create flags
#                                                   None,  # new environment dict
#                                                   None,  # current directory
#                                                   startup)  # startup info
#         print result
#     except pywintypes.error, (errcode, method, msg):
#         print errcode, method, msg
#
#
#
# def AdjustPriv(priv, enable=1):
#     flags = win32security.TOKEN_ADJUST_PRIVILEGES | win32security.TOKEN_QUERY
#     htoken = win32security.OpenProcessToken(
#         win32api.GetCurrentProcess(), flags)
#     id = win32security.LookupPrivilegeValue(None, priv)
#     if enable:
#         newPriv = [(id, win32security.SE_PRIVILEGE_ENABLED)]
#     else:
#         newPriv = [(id, 0)]
#     win32security.AdjustTokenPrivileges(htoken, 0, newPriv)






class aservice(win32serviceutil.ServiceFramework):
    # _svc_name_ = "Stratosphere_service"
    # _svc_display_name_ = "Stratosphere"
    # _svc_description_ = "Stratosphere is your shield!"

    _svc_name_ = "myserv"
    _svc_display_name_ = "Stratosphere"
    _svc_description_ = "Stratosphere is your shield!"


    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        import servicemanager
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE, servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))


        self.timeout = 3000  # 10 seconds
        while 1:
            # Wait for service stop signal, if I timeout, loop again
            rc = win32event.WaitForSingleObject(self.hWaitStop, self.timeout)
            # Check to see if self.hWaitStop happened
            if rc == win32event.WAIT_OBJECT_0:
                break
            else:
                try:




                    execfile("C:\\Users\\Frenky\\Documents\\Skola\\Stratosphere\\windowsService\\just_try.py")


                    # AdjustPriv(win32security.SE_TCB_NAME)
                    # AdjustPriv(win32security.SE_ASSIGNPRIMARYTOKEN_NAME)
                    # AdjustPriv(win32security.SE_INCREASE_QUOTA_NAME)
                    #
                    # hUser = attempt_to_logon()
                    # run_as_user(hUser)

                    #file_path = "C:\Users\Frenky\Documents\Skola\Stratosphere\windowsService\configfile_check.py"
                    #execfile(file_path)  # Execute the script
                except:
                    pass



def ctrlHandler(ctrlType):
    return True


if __name__ == '__main__':
    win32api.SetConsoleCtrlHandler(ctrlHandler, True)
    win32serviceutil.HandleCommandLine(aservice)

