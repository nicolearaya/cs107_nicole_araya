#!/bin/bash
grep [0-9] apollo13.txt | wc -l > apollo_out.txt
grep --help | grep "\-c, \-\-count"
ls *.py|wc -l
ls -laR | grep "^\-......\-\-."|wc -l
ls -la | grep "^[d,\-]......\-\-."|wc -l
