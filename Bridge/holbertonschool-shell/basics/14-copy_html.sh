#!/bin/bash

# copies all the HTML files from the current working directory to 
# the parent of the working directory, but only copy files that 
# did not exist in the parent of the working directory or were 
# newer than the versions in the parent of the working directory.
cp -u *.html ..