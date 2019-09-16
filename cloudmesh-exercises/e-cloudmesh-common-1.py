# E.Cloudmesh.Common.1 - week 3
# Develop a program that demonstrates the use of banner, HEADING, and VERBOSE.

# from CM import banner function
from cloudmesh.common.util import banner

banner("Name:Zhi Wang | First Cloudmesh program | 09/2019")

# from CM import Heading function
from cloudmesh.common.util import HEADING

HEADING()
print("Name:Zhi Wang | First Cloudmesh program | 09/2019")

# from CM import Verbose, a debugging method
from cloudmesh.common.debug import VERBOSE

dic_value = {"movies": "I.T."}
VERBOSE(dic_value)