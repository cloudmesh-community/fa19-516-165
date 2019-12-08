library(rcms)
library(reticulate)

# test
library(testthat)

test_that("help command", {
  expect_equal(cms("help"),"\nDocumented commands (type help <topic>):\n========================================\nEOF        data     host       man       register  ssh        vcluster      \nadmin      debug    image      open      sec       start      version       \nbanner     default  info       pause     service   stop       vm            \nclear      echo     init       plugin    set       stopwatch  workflow_draft\ncommands   flavor   inventory  provider  shell     sys      \nconfig     group    ip         q         sleep     var      \ncontainer  help     key        quit      source    vbox     \n\n")
})




