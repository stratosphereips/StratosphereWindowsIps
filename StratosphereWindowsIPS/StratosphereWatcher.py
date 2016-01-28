__author__ = 'Frenky'
import subprocess
import time
import datetime
import urllib2
import StratosphereConfig
import StratosphereOutput


def download_upadte(url):
    StratosphereOutput.show('Downloading updates.', 2)
    # url = "https://raw.githubusercontent.com/stratosphereips/StratosphereIps/Frenky/windowsService/configfile_check.py"

    file_name = url.split('/')[-1]
    u = urllib2.urlopen(url)
    f = open(file_name, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    StratosphereOutput.show(("Downloading: %s Bytes: %s" % (file_name, file_size)), 2)

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
        file_size_dl = len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8) * (len(status) + 1)
        StratosphereOutput.show(status, 2)

    f.close()


def check_if_upadte():
    date_upadte = datetime.datetime.strptime(StratosphereConfig.date_string, '%Y-%m-%d')
    date_now = datetime.datetime.now()
    print date_upadte
    print date_now
    if date_upadte < date_now:
        if StratosphereConfig.is_forbidden is False:
            StratosphereOutput.show("Downloading new update.", 1)
            # download_upadte(ConfigFile.url_string) #  (pak je treba dat do funkce download exception pro pripad, ze nejsi propojenej k netu)
            StratosphereOutput.show('Set config file.', 1)
            StratosphereConfig.set_config()
        else:
            print ("Updating is forbidden!", 1)


if __name__ == "__main__":
    # Loading or creating config file.
    StratosphereConfig.check_config()
    # checking if
    check_if_upadte()
    # Path to Stratospehere Window
    # path = 'C:\Users\Frenky\Documents\Skola\Stratosphere\StratosphereWindowsIPS\StratosphereWindow.py'
    path = 'C:\Users\Frenky\Documents\Skola\Stratosphere\StratosphereWindowsIPS'
    # Create process.
    # p = subprocess.Popen('python ' + path, shell=True)
    print 'cat' +path+ '\test8.binetflow | python ' + path + '\StratosphereFlow.py'
    p = subprocess.Popen('cat ' +path+ '\\example-flows.binetflow | python ' + path + '\\StratosphereFlow.py', shell=True)
    # Wait until process terminates.
    while True:
        if p.poll() is None:
            StratosphereOutput.show("Process is still runnning...", 3)
            time.sleep(StratosphereConfig.check_if_process_work)
        else:
            p = subprocess.Popen('python ' + path, shell=True)
    StratosphereOutput.show(("Process ended, ret code:", p.returncode), 2)
