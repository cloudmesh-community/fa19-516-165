# E.Cloudmesh.Common.4 Develop a program that demonstrates the use of cloudmesh.common.Shell.

# from CM import Shell
from cloudmesh.common.Shell import Shell

# print out the file location
result_1 = Shell.execute('pwd') # section 6.5, result should be pre-defined
print(result_1)

result_2 = Shell.ping(host='amazon.com')
print(result_2)