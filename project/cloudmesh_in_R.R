# load  reticulate in R

# have to indidate the system variable first in order to use it later
Sys.setenv(RETICULATE_PYTHON = "/Users/zwang/ENV3/bin/python")

# use the reticulate library
library(reticulate)

# activate the Python environment
use_python("/Users/zwang/ENV3/bin/python", required = TRUE)

# double check the python config to enasure
py_config()

# import cloudmesh
cloudmesh <- import("cloudmesh")

# call cms function
cloudmesh$cloud$Shell$cms("help")

# define cms function
cms <-function (command){
  cloudmesh <- import("cloudmesh")
  cloudmesh$cloud$Shell$cms(command)
}

# test two simple examples
cms("help")
cms("config")