# E.Cloudmesh.Common.3
# Develop a program that demonstrate the use of FlatDict.

from cloudmesh.common.FlatDict import FlatDict

dict = {
    "name": "Zhi",
    "education": "Ph.D. in Public Health",
    "address": {
        "University": "Indiana University - Bloomington",
        "city": "Bloomington",
        "zip": "47404"
    }
}

flattened = FlatDict(dict)

print(flattened)
