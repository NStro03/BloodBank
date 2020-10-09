import csv
import copy


def newUser(name):
    print("Noob DETECTED!!")
    userTemplate = {
        "ID": "",
        "NAME": "",
        "DONATED_UNITS": "0",
        "REQUESTED_UNITS": "0",
        "STATUS": "None"
    }
    with open("UserData.csv") as ud:
        reader = csv.DictReader(ud)
        i = 0
        Users = []
        for row in reader:
            Users.append(copy.deepcopy(row))
            i += 1

    userTemplate["NAME"] = name
    userTemplate["ID"] = i+1

    Users.append(userTemplate)

    with open('UserData.csv', 'w') as s:
        fieldnames = ["ID", "NAME", "DONATED_UNITS", "REQUESTED_UNITS", "STATUS"]
        writer = csv.DictWriter(s, fieldnames=fieldnames)
        writer.writeheader()
        for j in Users:
            # print(i)
            writer.writerow(j)

    print("Hi {0}, You have been succesfully registered to our Blood Bank. Please use the below user ID to login to "
          "our system.\n\tUser ID: {1}".format(name, userTemplate["ID"]))


def existingUser(id):
    print("RESPECT THE LORD!!")
    while(True):
        inp = int(input("What do you want to do :\n\t1. Donate Blood\n\t2. Request Blood\n\t0. Logout\n"
                        "Make your choice: "))


def staff():
    while(True):
        inp = int(
            input("What do you want to do :\n\t1. Test Blood\n\t0. Logout\nMake your choice: "))


if __name__ == '__main__':
    newUser("Sudeep")

