#!/bin/sh

INPUT='../ex03/hh_positions.csv'

get_date() {
  local str="$1";
  local index=$(expr index "$str" ',')

  index=$((index+2))
  echo $( echo $str |  awk -v var=$index '{
    print  substr($0, var, 10);
  }');
}

PREV_DATE=''
CURRENT_DATE=''
HEADER=$(head -1 < $INPUT)

tail -20 < $INPUT | \
while read line; do
  CURRENT_DATE=$(get_date $line)
  if [ "$CURRENT_DATE" != "$PREV_DATE" ]; then
      echo $HEADER > $CURRENT_DATE".csv"
      PREV_DATE="$CURRENT_DATE"
  fi
  echo $line >> $CURRENT_DATE".csv"
done
