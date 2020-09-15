#!/bin/bash

# Coder: Bianca
# Listener: Will
# Sharer: Nicole

#ls -la | grep "^\-..x......"

# the above command works to find files executable by user
# but hints say to use a for loop

#echo "$( ls )"

# $( ls -a )

for file in *
do
    if [ -x $file ]; then
        echo $file 
    fi
done