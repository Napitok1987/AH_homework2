import csv

inp_file = open('output_1.csv', 'r')
out_file = open('output_3.csv', 'w')

reader = csv.reader(inp_file)
writer = csv.writer(out_file)

rows_count = 0

for row in reader:
    name = row[0]
    surname = row[1]
    email = row[2]
    position = row[3]
    social_profile = row[4]
    if 'github.com' in social_profile:
        writer.writerow([name, surname, email, position, social_profile])
        rows_count = rows_count + 1

if rows_count in range(2, 4):
    i = 'и'
elif rows_count == 1:
    i = "а"
else:
    i = ''

print('Данные отфильтрованы. Результат ({count} строк{ending}) записан в output_3.csv'.format(ending=i, count=rows_count))
