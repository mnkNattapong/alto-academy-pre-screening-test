#!/bin/bash

# create a new user account
sudo useradd -m johndoe

# set a password for the new user
sudo passwd johndoe password123

# assign the user account to the group "developers"
sudo usermod -aG developers johndoe

# verify that the user account exists and is a member of the group "developers"
id johndoe

# change the permissions of a file named "file.txt"
sudo chmod 744 file.txt

# create a folder named "backup"
mkdir backup

# copy a file named "file1.txt" to the "backup" directory
cp file1.txt backup/
