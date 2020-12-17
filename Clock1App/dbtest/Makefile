TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================
PYTESTS += test_assert.py
PYTESTS += test_db.py

TAPFILES = $(PYTESTS:.py=.py.tap)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

ifeq ($(T_A),$(EPICS_HOST_ARCH))

#export EPICS_HOST_ARCH
#export EPICS_BASE

runtests:
	pytest ../

$(TAPFILES): test_%.py.tap: ../test_%.py
	pytest --tap-files $<

endif
