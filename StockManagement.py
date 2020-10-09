import copy
import csv
import numpy as np
import pandas as pd



def stockDetails():
    with open('stock_management.csv')as s:
        reader = csv.DictReader(s)
        for row in reader:
            temp = copy.deepcopy(row)
            # for k, v in row.items():
            #     print(k, v)
        return temp


def creditUnits(blood, x):
    current_stock=stockDetails()
    t=int(current_stock[blood])+x
    current_stock[blood]="{}".format(t)
    with open('stock_management.csv', 'w')as s:
        fieldnames=['A+','B+','AB+','O+','A-','B-','AB-','O-']
        writer = csv.DictWriter(s,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(current_stock)

def DebitUnits(blood,x):
    current_data=stockDetails()

    if(int(current_data[blood])<x):
        print("stock is less than the demanded")
        return
    t = int(current_data[blood]) - x
    current_data[blood] = "{}".format(t)
    with open('stock_management.csv', 'w')as s:
        fieldnames = ['A+', 'B+', 'AB+', 'O+', 'A-', 'B-', 'AB-', 'O-']
        writer = csv.DictWriter(s, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(current_data)


if __name__=="__main__":
    print(stockDetails())

    creditUnits('A+',10)
    print(stockDetails())

    DebitUnits('B+',5)
    print(stockDetails())
