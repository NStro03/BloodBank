import csv
import copy
from modules import customer, staff


def newUser():
    print("Noob DETECTED!!")
    name = input("Please enter your name: ")
    userTemplate = {
        "ID": "",
        "NAME": "",
        "DONATED_UNITS": "0",
        "REQUESTED_UNITS": "0",
        "STATUS": "None"
    }
    with open("database/UserData.csv") as ud:
        reader = csv.DictReader(ud)
        i = 0
        Users = []
        for row in reader:
            Users.append(copy.deepcopy(row))
            i += 1

    userTemplate["NAME"] = name
    userTemplate["ID"] = i+1

    Users.append(userTemplate)

    with open('database/UserData.csv', 'w') as s:
        fieldnames = ["ID", "NAME", "DONATED_UNITS", "REQUESTED_UNITS", "STATUS"]
        writer = csv.DictWriter(s, fieldnames=fieldnames)
        writer.writeheader()
        for j in Users:
            # print(i)
            writer.writerow(j)

    print("Hi {0}, You have been succesfully registered to our Blood Bank. Please use the below user ID to login to "
          "our system.\n\tUser ID: {1}".format(name, userTemplate["ID"]))


def existingUser():
    print("SALUTATION TO MY LORD!!")
    switcher = {
        1: customer.customer,
        2: staff.staff
    }
    inp = int(input("Are you \n\t1. Customer\n\t2. Staff\n"
                    "Make your choice: "))
    func = switcher.get(inp, lambda: "enter valid input")
    func()


if __name__ == '__main__':
    # newUser()
    existingUser()

