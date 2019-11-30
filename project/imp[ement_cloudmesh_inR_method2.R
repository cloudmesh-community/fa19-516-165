# Title     : implement Cloudmesh in R
# Objective : to call Python script from R environment
# Created by: zwang
# Created on: 11/29/19

# install.packages("reticulate")

# load  reticulate in R
library(reticulate)

# activate the Python virtual environment
# please use the use_virtualenv command as it should be
use_virtualenv("/Users/zwang/ENV3/bin/python")

# run provider script in the same location
# the provider file may was based on the
py_run_file("Provider.py")




