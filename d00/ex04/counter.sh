#!/bin/sh

INPUT='../ex03/hh_positions.csv'
OUTPUT='hh_uniq_positions.csv'

echo '"name","count"' > $OUTPUT

tail -20 $INPUT | \
awk '
BEGIN {
  FS="\","; 
  OFS="\",";
  JC=0
  MC=0
  SC=0
}
{
  IDX = index($3, "Junior")
  if (IDX > 0) {
    JC++;
  }

  IDX = index($3, "Middle")
  if (IDX > 0) {
    MC++;
  }

  IDX = index($3, "Senior")
  if (IDX > 0) {
    SC++;
  }

  if (TMP == "")
    TMP = "-"

}
END {
  print "\"Junior\"," JC
  print "\"Middle\"," MC
  print "\"Senior\"," SC
}' | sort -t ',' -r -k 2,2 >> $OUTPUT; 