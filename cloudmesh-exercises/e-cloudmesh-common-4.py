# E.Cloudmesh.Common.4 Develop a program that demonstrates the use of cloudmesh.common.Shell.

# from CM import Shell
from cloudmesh.common.Shell import Shell

# print out the file location
result = Shell.execute('pwd')
print(result)

result = Shell.ping(host='amazon.com')
print(result)

