#!/bin/bash

mkdir logs/

for file in *.log
do
	echo $file
	tail -n 13 $file > logs/$file.tail.log
done
