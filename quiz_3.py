# Uses Global Temperature Time Series, avalaible at
# http://data.okfn.org/data/core/global-temp, stored in the file monthly_csv.csv,
# assumed to be stored in the working directory.
# Prompts the user for the source, a year or a range of years, and a month.
# - The source is either GCAG or GISTEMP.
# - The range of years is of the form xxxx -- xxxx (with any number of spaces,
#   possibly none, around --) and both years can be the same,
#   or the first year can be anterior to the second year,
#   or the first year can be posterior to the first year.
# We assume that the input is correct and the data for the requested month
# exist for all years in the requested range.
# Then outputs:
# - The average of the values for that source, for this month, for those years.
# - The list of years (in increasing order) for which the value is larger than that average.
# 
# Written by *** and Eric Martin for COMP9021


import sys
import os
import csv
from pathlib import Path

filename = 'monthly_csv.csv'
if not os.path.exists(filename):
    print(f'There is no file named {filename} in the working directory, giving up...')
    sys.exit()

source = 'GCAG'
year_or_range_of_years = '2016   -  -  2016'
month = 'June'
average = 0
years_above_average = []

# REPLACE THIS COMMENT WITH YOUR CODE
file_path = Path(filename)
years = year_or_range_of_years.split('-')
year1 = int(years[0])
year2 = int(years[-1])
if year2 < year1:
    year1, year2 = year2, year1
dict_month = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8,
              'september': 9, 'october': 10, 'november': 11, 'december': 12}
dict_year = dict()
list_year = []
int_month = dict_month[month.lower()]
total = 0
num = 0
with open(file_path) as csv_file:
    for line in csv_file.readlines()[1:]:
        t_source, date, t_mean = line.split(',')
        t_year, t_month, _ = date.split('-')
        if t_source == source and int(t_month) == int_month:
            t_year = int(t_year)
            if year1 <= t_year and t_year <= year2:
                t_mean = float(t_mean.strip('\n'))
                list_year.append((t_year, t_mean))
                total = total + t_mean
                num += 1
if num != 0:
    average = total / num
list_year_sorted = sorted(list_year, key=lambda x: x[1], reverse=True)
print(average)
for i in list_year_sorted:
    if i[1] <= average:
        break
    years_above_average.append(i[0])
years_above_average.sort()

print(f'The average anomaly for {month} in this range of years is: {average:.2f}.')
print('The list of years when the temperature anomaly was above average is:')
print(years_above_average)
