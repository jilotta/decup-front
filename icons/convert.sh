#!/bin/sh

for i in $(ls svg | cut -f1 -d'.'); do
  inkscape svg/$i.svg -o png/$i.png -w 96 -h 96
  echo "$i.svg -> $i.png done"
done
