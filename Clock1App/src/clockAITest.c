#include <unistd.h>
#include "epicsUnitTest.h"
#include "testMain.h"

#include "devAiSecond.h"

MAIN(mathTest)
{
  unsigned int val = 0, sec = 0;
  time_t t;
  struct tm *tm;
  
  testPlan(1);
  time(&t);
  tm = localtime(&t);
  sec = tm->tm_sec;

  //sleep(2);

  val = get_value();

  if (!testOk1(sec == val))
      testDiag("sec = %u, val = %u", sec, val);
  return testDone();
}
