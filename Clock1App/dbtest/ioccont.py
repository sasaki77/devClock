import os
import subprocess
import atexit
import time

class IocControl(object):
    server_port   = 12782
    repeater_port = 12783

    def __init__(self, cpath="softIoc", arg_list=["-d","test.db"], verbose=False):
        self.__command_path = cpath
        self.__child_env    = os.environ.copy()
        self.__process      = None
        self.__arg_list     = arg_list
        self.__devnull      = None if verbose else open(os.devnull, "wb")

    def start(self):
        self.__setup()
        iocCommand = [self.__command_path]
        iocCommand.extend(self.__arg_list)
        self.__process = subprocess.Popen(iocCommand, env=self.__child_env,
                stdin=subprocess.PIPE, stdout=self.__devnull, stderr=subprocess.STDOUT)
        time.sleep(.5)
        atexit.register(self.stop)

    def stop(self):
        if self.__process:
            self.__process.stdin.close()
            self.__process = None
        if self.__devnull:
            self.__devnull.close()

    def __setup(self):
        self.__child_env['EPICS_CA_AUTO_ADDR_LIST']         = "NO"
        self.__child_env['EPICS_CAS_AUTO_BEACON_ADDR_LIST'] = "NO"
        self.__child_env['EPICS_CA_ADDR_LIST']              = "localhost"
        self.__child_env['EPICS_CAS_BEACON_ADDR_LIST']      = "localhost"
        self.__child_env['EPICS_CA_SERVER_PORT']            = str(self.server_port)
        self.__child_env['EPICS_CA_REPEATER_PORT']          = str(self.repeater_port)


def main():
    ioc = IocControl(verbose=True)
    ioc.start()
    time.sleep(30)
    ioc.stop

if __name__ == "__main__":
    main()
