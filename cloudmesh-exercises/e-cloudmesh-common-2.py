# E.Cloudmesh.Common.2 - week 3
# Develop a program that demonstartes the use of dotdict

# from CM import dotdict fuction
from cloudmesh.common.dotdict import dotdict

info = {"name": "Zhi", "title": "Ph.D. candidate in public health", "depart": "dept. of applied health science"}

data = dotdict(info)

if data.name is "Zhi":
    print("this is quite readable")
else:
    print("this is non-readable")

