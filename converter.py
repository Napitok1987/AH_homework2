import csv

inp_file = open('input.csv', 'r')
out_file = open('output_1.csv', 'w')

reader = csv.reader(inp_file)
writer = csv.writer(out_file)

rows_count = 0

for row in reader:
    email = row[0]
    name = row[1]
    surname = row[2]
    company = row[3]
    position = row[4]
    social_profile = row[5]
    writer.writerow([name, surname, email, position, social_profile])
    rows_count = rows_count + 1

if rows_count in range(2, 4):
    i = 'и'
elif rows_count == 1:
    i = "а"
else:
    i = ''

print('Программа выполнена успешна. Результат ({count} строк{ending}) записан в output_1.csv'.format(ending=i,
                                                                                                     count=rows_count))
