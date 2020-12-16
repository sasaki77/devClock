import os
import time

import pytest
from epics import ca

from ioccont import IocControl


@pytest.fixture(scope='module')
def softioc():
    dir_path = os.path.dirname(__file__)
    db_file = os.path.join(dir_path, 'test.db')

    ioc_arg_list = ['-m', 'head=ET_dummyHost', '-d', db_file]
    iocprocess = IocControl(arg_list=ioc_arg_list)
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
