# load  reticulate in R

# have to indidate the system variable first
Sys.setenv(RETICULATE_PYTHON = "/Users/zwang/ENV3/bin/python")

# use the reticulate library
library(reticulate)
library(rcms)

# double check the python config to enasure
py_config()

# test two simple examples

cms("help")

cms("version")
