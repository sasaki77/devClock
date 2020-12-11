#!../../bin/linux-x86_64/Clock1

## You may have to change Clock1 to something else
## everywhere it appears in this file

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase("dbd/Clock1.dbd",0,0)
Clock1_registerRecordDeviceDriver(pdbbase)

## Load record instances
dbLoadRecords("db/aiSecond.db","user=ET_SASAKI")

cd ${TOP}/iocBoot/${IOC}
iocInit()

## Start any sequence programs
#seq sncxxx,"user=ET_SASAKI"
dbl
