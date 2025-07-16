#!/usr/bin/env python
import sys
import csv


    
reader = csv.reader(sys.stdin)

header = next(reader, None)

for row in reader:
    try:

        id_value = row[0]
        company = row[1]
        total_comp = row[3]

        print(f"{id_value}\t{company},{total_comp}")
    except Exception as e:

        continue
