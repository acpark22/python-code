import csv
filename= 'stck_perf_2020.csv'
with open(filename) as f:
    reader= csv.reader(f)
    header_row= next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

