# Cloudmesh Compute Project with Google Cloud Platform (GCP)

Zhi Wang, [fa19-516-165](https://github.com/cloudmesh-community/fa19-516-165), School of Public Health, Indiana University Bloomington

## Abstract

## Introduction

The purpose of this project is to implement related features to simplify compute
interface. The project implementation will include the following clouds:  

* Google Cloud Platform
* OpenStack

The benchmarks for this project will include the following components:

* virtual machine
* image
* flavor
* security groups

## Progress

### Week October 14 

#### Solved Cloudmesh setting issues on macOS Catalina 

#### Learned command line, bash file, and zsh in macOS Catalina

Since Catalina uses zsh as its default shell, installation process is 
a little different compared with previous bash file. Thanks to Dr. Laszewski
I was able to install Cloudmesh smoothly. Besides this, I also studied a 
little further on shell on .bash_profile and .zprofile. 

##### Why switch from .bash_profile to .zprofile

I found that it is even though there are bash v4 and v5 available, Apple 
does not update to newer versions because of the licenses (bash v3.2 with 
GPL v2. and v4/v5 with GPL v3.). 

##### Solution to stick to bash without warning message

Bash file is not gone but will not last indefinitely either. For Catalina
users, if you want to stick to bash, you can add follow environment variable 
to your .bash_profile or .bashrc. 

 ~~~~
 export BASH_SILENCE_DEPRECATION_WARNING=1
 ~~~~

For more information about zsh configuration, please visit [oh-my-zsh](https://ohmyz.sh)
for more information. 

## Results

### Limitations 

## Conclusion

## References

* [Cloudmesh Development Projects- Cloudmesh Compute](https://cloudmesh.github.io/cloudmesh-manual/projects/project-compute.html)
* [Using the Cloud Client Libraries for Python](https://cloud.google.com/compute/docs/tutorials/python-guide)
* [Github Cloudmesh Compute](https://github.com/cloudmesh/cloudmesh-cloud/tree/master/cloudmesh/compute)
* [oh-my-zhs]((https://ohmyz.sh))
* [Scripting OS X](https://scriptingosx.com/)