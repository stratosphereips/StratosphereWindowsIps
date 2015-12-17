__author__ = 'Frenky'

import win32con
import win32api
import win32security
import win32process
import pywintypes


def attempt_to_logon():
    username = "Frenky"
    password = "karel"
    try:
        hUser = win32security.LogonUser(username, None,
                                        password, win32security.LOGON32_LOGON_INTERACTIVE,
                                        win32security.LOGON32_PROVIDER_DEFAULT)
    except win32security.error:
        print "unable to logon"
        return None
    return hUser


def run_as_user(hUser):
    startup = win32process.STARTUPINFO()
    startup.dwFlags = win32process.STARTF_USESHOWWINDOW
    startup.wShowWindow = win32con.SW_SHOW
    startup.lpDesktop = 'winsta0\default'


    try:
        result = win32process.CreateProcessAsUser(hUser,
                                                  None,  # appName
                                                  "c:\\windows\\notepad.exe",  # notepad.exe
                                                  None,  # process attrs
                                                  None,  # thread attrs
                                                  0,  # inherit handles
                                                  0,  # create flags
                                                  None,  # new environment dict
                                                  None,  # current directory
                                                  startup)  # startup info
        print result
    except pywintypes.error, (errcode, method, msg):
        print errcode, method, msg


def print_info(hUser):
    print win32security.GetTokenInformation(hUser,win32security.TokenPrivileges)


def AdjustPriv(priv, enable=1):
    flags = win32security.TOKEN_ADJUST_PRIVILEGES | win32security.TOKEN_QUERY
    htoken = win32security.OpenProcessToken(
        win32api.GetCurrentProcess(), flags)
    id = win32security.LookupPrivilegeValue(None, priv)
    if enable:
        newPriv = [(id, win32security.SE_PRIVILEGE_ENABLED)]
    else:
        newPriv = [(id, 0)]
    win32security.AdjustTokenPrivileges(htoken, 0, newPriv)


AdjustPriv(win32security.SE_TCB_NAME)
AdjustPriv(win32security.SE_ASSIGNPRIMARYTOKEN_NAME)
AdjustPriv(win32security.SE_INCREASE_QUOTA_NAME)

hUser = attempt_to_logon()
print_info(hUser)
run_as_user(hUser)

