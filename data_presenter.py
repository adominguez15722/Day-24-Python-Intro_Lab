from fileinput import close
from functools import total_ordering


open_file = open("CupcakeInvoices.csv")

full_total = []
for row in open_file:
    # print(row)
    
    # row = row.split(',')
    # print(row[2])
    
    # row = row.split(',')
    # amount = int(row[3])
    # price = float(row[4])
    # print(amount * price)

    row = row.split(',')
    amount = int(row[3])
    price = round(float(row[4]), 2)
    total = round((amount * price), 2)
    full_total.append(total)


print (round(sum(full_total)))

open_file.close()

