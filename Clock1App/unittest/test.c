#include <math.h>
#include "epicsUnitTest.h"
#include "testMain.h"

MAIN(mathTest)
{
    testPlan(3);
    testOk(sin(0.0) == 0.0, "Sine starts");
    testOk(cos(0.0) == 1.0, "Cosine continues");
    if (!testOk1(M_PI == 4.0*atan(1.0)))
        testDiag("4*atan(1) = %g", 4.0*atan(1.0));
    return testDone();
}
