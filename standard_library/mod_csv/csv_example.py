import csv

with open('data_science/data_files/prem_stats.csv', 'r') as f:
    lines = csv.reader(f, delimiter=',')

    # Verify it works by printing each line
    for line in lines:
        print(line)
