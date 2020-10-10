import BloodTester as BT
import csv
import copy


def acceptBlood(curr_staff):
    BT.testBlood()

    BloodUnits = []
    error_units = []
    Users = []
    i = 0
    with open("UserData.csv") as ud:
        reader = csv.DictReader(ud)
        for row in reader:
            Users.append(copy.deepcopy(row))

    with open("BloodUnits.csv") as bu:
        reader = csv.DictReader(bu)
        for row in reader:
            i += 1
            # BloodUnits.append(copy.deepcopy(row))
            if row["TESTED"] == "TRUE":
                if row["STATUS"] == "accepted":
                    userFound = False
                    for u in Users:
                        if u["ID"] == row["DONOR_ID"]:
                            userFound = True
                            u["DONATED_UNITS"] = "{}".format(int(u["DONATED_UNITS"]) + int(row["UNIT_COUNT"]))
                            curr_staff["ACCEPTED_UNITS"] = "{}".format(int(curr_staff["ACCEPTED_UNITS"]) + 1)
                            break
                    if not userFound:
                        error_units.append(i)
                        print("Donor_id mismatch!\n"
                              "The Donor ID {} mapped to the blood units was not found in the user DB.".format(
                            row["DONOR_ID"]))
                else:
                    userFound = False
                    for u in Users:
                        if u["ID"] == row["DONOR_ID"]:
                            userFound = True
                            if row["STATUS"] == "rejected":
                                u["STATUS"] = "inactive"
                            elif row["STATUS"] == "blacklisted":
                                u["STATUS"] = "blacklisted"
                            else:
                                error_units.append(i)
                                print("Unknown Status of Blood unit detected!\nPlease rectify the status of Blood "
                                      "unit in DB.")
                                row["TESTED"] = "FALSE"
                                break
                            curr_staff["REJECTED_UNITS"] = "{}".format(int(curr_staff["REJECTED_UNITS"]) + 1)
                            break
                    if not userFound:
                        error_units.append(i)
                        print("Donor_id mismatch!\n"
                              "The Donor ID {} mapped to the blood units was not found in the user DB.".format(
                            row["DONOR_ID"]))
            BloodUnits.append(copy.deepcopy(row))

    with open('UserData.csv', 'w') as s:
        fieldnames = ["ID", "NAME", "DONATED_UNITS", "REQUESTED_UNITS", "STATUS"]
        writer = csv.DictWriter(s, fieldnames=fieldnames)
        writer.writeheader()
        for j in Users:
            # print(i)
            writer.writerow(j)

    i = 0
    with open('BloodUnits.csv', 'w') as s:
        fieldnames = ["DONOR_ID", "BLOOD_GROUP", "UNIT_COUNT", "TESTED", "STATUS"]
        writer = csv.DictWriter(s, fieldnames=fieldnames)
        writer.writeheader()
        for j in BloodUnits:
            i += 1
            if i in error_units or j["TESTED"] == "FALSE":
                writer.writerow(j)


if __name__ == '__main__':
    currStaff = {
        "ID": "1",
        "NAME": "Nishkarsh",
        "ACCEPTED_UNITS": "4",
        "REJECTED_UNITS": "2"
    }
    acceptBlood(currStaff)

