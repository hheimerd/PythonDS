#!/bin/sh

INPUT='../ex02/hh_sorted.csv'
OUTPUT='hh_positions.csv'

head -1 $INPUT > $OUTPUT
tail -20 $INPUT | \
awk '
BEGIN{FS="\","; OFS="\","}
{
  TMP = ""

  IDX = index($3, "Junior")
  if (IDX > 0) {
    TMP = TMP"Junior / "
  }

  IDX = index($3, "Middle")
  if (IDX > 0) {
    TMP = TMP"Middle / "
  }

  IDX = index($3, "Senior")
  if (IDX > 0) {
    TMP = TMP"Senior"
  }

  if (TMP == "")
    TMP = "-"

  gsub(/[\/ ]*$/, "", TMP)


  $3="\""TMP
  print
}
 ' \
 >> $OUTPUT; 