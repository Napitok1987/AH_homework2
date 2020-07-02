import csv

inp_file = open('output_1.csv', 'r')
out_file = open('output_2.csv', 'w')

reader = csv.reader(inp_file)
writer = csv.writer(out_file)

rows_count = 0

for row in reader:
    name = row[0]
    surname = row[1]
    email = row[2]
    position = str.lower((row[3]))
    social_profile = row[4]
    if 'developer' in position:
        writer.writerow([name, surname, email, position, social_profile])
        rows_count = rows_count + 1
    elif 'engineer' in position:
        writer.writerow([name, surname, email, position, social_profile])
        rows_count = rows_count + 1
if rows_count in range(2, 4):
    i = 'и'
elif rows_count == 1:
    i = "а"
else:
    i = ''

print('Данные отфильтрованы. Результат ({count} строк{ending}) записан в output_2.csv'.format(ending=i, count=rows_count))
