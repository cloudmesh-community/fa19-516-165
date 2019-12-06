#
# import cloudmesh cms command in R
#
cms <-function (command){
  library(reticulate)
  cloudmesh <- import("cloudmesh")
  cloudmesh$cloud$Shell$cms(command)
}