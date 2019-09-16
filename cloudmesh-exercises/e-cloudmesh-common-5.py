# E.Cloudmesh.Common.5 Develop a program that demonstartes the use of cloudmesh.common.StopWatch

# import StopWatch file
from cloudmesh.common.StopWatch import StopWatch
import time

StopWatch.start("test clock")

time.sleep(7) # section 6.6, OS library does not have time function

StopWatch.stop("test clock")

print(StopWatch.get("test clock"))
