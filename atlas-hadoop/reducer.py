#!/usr/bin/env python3
"""No idea if this is correct"""
import sys
import re


top_salaries = []

for i, line in enumerate(sys.stdin):
    line = line.strip()
    words = re.split('\t|,', line)
    _id, company, salary = words

    try:
        if i <= 10:
            top_salaries.append([int(_id), float(salary), company])

        if i == 10:
            top_salaries.sort(key=lambda x: x[1], reverse=True)

        if i > 10:
            if int(salary) > top_salaries[-1][1]:
                top_salaries.pop(-1)
                top_salaries.append([int(_id), float(salary), company])
                top_salaries.sort(key=lambda x: x[1], reverse=True)

    except Exception as e:
        # print('Error: {}'.format(e))
        continue

print('id\tSalary\tcompany')
for line in top_salaries:
    print('{}\t{}\t{}'.format(line[0], line[1], line[2]))
