import sys
import os
import csv
from collections import defaultdict

filename = 'monthly_csv.csv'
if not os.path.exists(filename):
    print(f'There is no file named {filename} in the working directory, giving up...')
    sys.exit()

source = input('Enter the source (GCAG or GISTEMP): ')
year_or_range_of_years = input('Enter a year or a range of years in the form XXXX -- XXXX: ')
month = input('Enter a month: ')
average = 0
years_above_average = []

## REPLACE THIS COMMENT WITH YOUR CODE


range_years = year_or_range_of_years.split(' -- ')
range_years = []
for y in rangeyears:
    range_years.append(int(y))
range_years.sort()
print(range_years)
monthdict = {'January': '1', 'February': '2', 'March': '3', 'April': '4', 'May': '5', 'June': '6', 'July': '7',
             'August': '8', 'September': '9', 'October': '10', 'November': '11', 'December': '12'}
print(monthdict[month])

needlist = defaultdict(list)
with open(filename) as file:
    csv_file = csv.reader(file)
    for Source, Date, Mean in csv_file:
        Datenew = Date.split('-')
        if Source == source and int(Datenew[1]) == int(monthdict[month]) and range_years[0] <= int(Datenew[0]) <= \
                range_years[1]:

            needlist[Datenew[0]].append(Mean)
        else:
            continue

print(f'The average anomaly for {month} in this range of years is: {average:.2f}.')
print('The list of years when the temperature anomaly was above average is:')
print(years_above_average)
