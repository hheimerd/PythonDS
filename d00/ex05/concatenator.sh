#!/bin/sh

INPUT='./20*.csv'
OUTPUT='all.csv'


IS_FIRST_FILE=1;

ls -f $INPUT | while read -r file; do 
  if [ $IS_FIRST_FILE -eq 1 ]; then
    IS_FIRST_FILE=0
    head -1 < $file > $OUTPUT;
  fi;

  IS_FIRST_LINE=1
  while read line; do
     if [ $IS_FIRST_LINE -eq 1 ]; then
      IS_FIRST_LINE=0
      continue;
    fi;
      echo $line >> $OUTPUT;

  done < $file;

done;
