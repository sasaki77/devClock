import time
from epics import PV

def test_db(softioc, caclient):
    pv_in1 = PV("ET_dummyHost:LI1")
    pv_in2 = PV("ET_dummyHost:LI2")
    pv_calc = PV("ET_dummyHost:CALC")

    pv_in1.wait_for_connection(timeout=30)
    pv_in2.wait_for_connection(timeout=30)
    pv_calc.wait_for_connection(timeout=30)

    pv_in1.put(1, timeout=1)
    pv_in2.put(2, timeout=1)

    time.sleep(0.1)

    pv_calc.get()

    assert pv_calc.value == 3
