import csv


with open('museum.csv', newline='') as csvfile:
    art_reader = csv.reader(csvfile, delimiter='|')
    rows = list(art_reader)
    for row in rows[:2]:
        print(', '.join(row))
print(f'\n***********************************')
print('***********************************\n')
with open('museum.csv', newline='') as csvfile:
    art_reader = csv.DictReader(csvfile, delimiter='|')
    rows = list(art_reader)
    for row in rows[1:3]:
        print(row['model'])
print(f'\n***********************************')
print('***********************************\n')
