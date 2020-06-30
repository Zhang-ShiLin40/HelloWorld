import csv

# 读取csv

with open('../test1.csv', 'r') as f:
    reader = csv.reader(f)
    for i in reader:
        print(i[0]+','+i[1])
