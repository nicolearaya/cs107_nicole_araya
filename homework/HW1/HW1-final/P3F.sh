#!/bin/bash

for OUTPUT in *
do
   if [ -f $OUTPUT ]; then
	echo "$OUTPUT `cat $OUTPUT|wc -l`"
   fi
done
