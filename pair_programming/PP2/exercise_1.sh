#!/bin/bash

#prompt user for file

read -r -p 'file to commit:' userfile

git add $userfile
echo "`git status $userfile`"
read -r -p 'Do you wish to continue? (Y or N)' userAnswer
echo $userAnswer

if [ "$userAnswer" = "N" ]; then
    exit 1
elif [ "$userAnswer" = "Y" ]; then
    read -r -p 'Message to include in your commit:' userMessage
else
    exit 1
fi

git commit -m "$userMessage"
echo "`git status $userfile`"

read -r -p 'Do you wish to continue? (Y or N)' userContinue
if [ $userContinue == "Y" ]; then
    git push
else
    exit 1
fi
