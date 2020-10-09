import csv
import copy

# TotalBloodCount = 2
# BloodDataTemplate={
#     "donorID": None,
#     "group": None,
#     "tested": False,
#     "status": None
# }
#
# BloodUnits = [
#     {
#         "donorID":"1",
#         "group":"B+",
#         "tested": False,
#         "status": None
#     },
#     {
#         "donorID":"3",
#         "group": "O+",
#         "tested": False,
#         "status": None
#     }
# ]

def TestBlood():
    with open("BloodUnits.csv") as bu:
        reader = csv.DictReader(bu)
        i = 0
        BloodUnits = []
        for row in reader:
            BloodUnits.append(copy.deepcopy(row))

    found = False
    for i in BloodUnits:
        if i["TESTED"]=="FALSE":
            found = True
            print("Blood Test in progress...\n")
            i["STATUS"] = input("Please enter the result of blood test (accepted/rejected/blacklisted): ")
            i["TESTED"] = "TRUE"
            break

    if not found:
        print("No Blood units left to test. Enjoy your day in cafeteria!")
        return
    with open('BloodUnits.csv', 'w') as s:
        fieldnames = ["DONOR_ID", "BLOOD_GROUP", "TESTED", "STATUS"]
        writer = csv.DictWriter(s, fieldnames=fieldnames)
        writer.writeheader()
        for i in BloodUnits:
            # print(i)
            writer.writerow(i)
    return



if __name__ == "__main__":
    TestBlood()
    # print(BloodUnits[0]["tested"])

