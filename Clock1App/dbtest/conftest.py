import os
import time

import pytest
from epics import ca

from ioccont import IocControl


@pytest.fixture(scope='module')
def softioc():
    hostArch = 'linux-x86_64'
    if 'EPICS_HOST_ARCH' in os.environ:
        hostArch = os.environ['EPICS_HOST_ARCH']
    elif 'T_A' in os.environ:
        hostArch = os.environ['T_A']
    else:
        print("Warning: EPICS_HOST_ARCH not set. Using default value of '{0}'".format(hostArch))

    iocExecutable = 'softIoc'
    if 'IOC_EPICS_BASE' in os.environ:
        iocExecutable = os.path.join(os.environ['IOC_EPICS_BASE'], 'bin', hostArch, 'softIoc')
    elif 'EPICS_BASE' in os.environ:
        iocExecutable = os.path.join(os.environ['EPICS_BASE'], 'bin', hostArch, 'softIoc')
    else:
        print("Warning: IOC_EPICS_BASE or EPICS_BASE not set. Running 'softIoc' executable in PATH")

    dir_path = os.path.dirname(__file__)
    db_file = os.path.join(dir_path, 'test.db')

    ioc_arg_list = ['-m', 'head=ET_dummyHost', '-d', db_file]
    iocprocess = IocControl(cpath=iocExecutable, arg_list=ioc_arg_list)
    iocprocess.start()

    yield iocprocess

    iocprocess.stop()


@pytest.fixture(scope='session', autouse=True)
def caclient():
    ca.finalize_libca()
    time.sleep(1)

    sport = str(IocControl.server_port)
    os.environ['EPICS_CA_AUTO_ADDR_LIST'] = 'NO'
    os.environ['EPICS_CA_ADDR_LIST'] = 'localhost:{}'.format(sport)

    ca.initialize_libca()
    time.sleep(1)
    yield
    ca.finalize_libca()
    time.sleep(1)
