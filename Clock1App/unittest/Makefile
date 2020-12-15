TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================
PROD_LIBS += Com

TESTPROD_HOST += clockTest
clockTest_SRCS += test.c
TESTS += clockTest

TESTSCRIPTS_HOST += $(TESTS:%=%.t)

include $(TOP)/configure/RULES
