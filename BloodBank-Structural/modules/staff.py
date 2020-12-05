import csv
import copy
from modules import AcceptBlood


def staff():
    id = input("Please enter your Employee ID: ")
    employees = []
    current_staff = None
    with open("database/StaffData.csv") as e:
        reader = csv.DictReader(e)
        for row in reader:
            employees.append(copy.deepcopy(row))
            if row["ID"] == id:
                current_staff = copy.deepcopy(row)

    if current_staff is None:
        print("User doesn't exist!!\nEnter a valid user ID or Contact Admin.")
        return

    print("Welcome {}".format(current_staff["NAME"]))

    while True:
        switcher = {
            1: AcceptBlood.acceptBlood,
        }
        inp = int(input("What do you want to do :\n\t1. Test Blood\n\t0. Logout\n"
                        "Make your choice: "))
        if inp == 0:
            return

        func = switcher.get(inp, lambda: "enter valid input")
        func(current_staff)
        for i in range(len(employees)):
            if current_staff["ID"] == employees[i]["ID"]:
                employees[i] = copy.deepcopy(current_staff)

        with open('database/StaffData.csv', 'w') as s:
            fieldnames = ["ID", "NAME", "ACCEPTED_UNITS", "REJECTED_UNITS"]
            writer = csv.DictWriter(s, fieldnames=fieldnames)
            writer.writeheader()
            for j in employees:
                writer.writerow(j)


if __name__ == '__main__':
    staff()

