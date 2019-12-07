# discoer the current python versions in the system
library(reticulate)
py_config()

# choose the one that have Cloudmesh installed
Sys.setenv(RETICULATE_PYTHON = "/Users/ENV3/bin/python")

library(rcms)

# test two examples

cms("help")

cms("version")

