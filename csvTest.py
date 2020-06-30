import csv


with open("./test1.csv", "a") as fw:
    writer = csv.writer(fw)
    writer.writerow(["a", "b", "c"])
    i = 0
    while True:
        i += 1
        writer.writerow([i, chr(ord('a')+i), "abc"])
        if i == 10:
            break
