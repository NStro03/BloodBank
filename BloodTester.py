import csv

TotalBloodCount = 2
BloodDataTemplate={
    "donorID": None,
    "group": None,
    "tested": False,
    "status": None
}

BloodUnits = [
    {
        "donorID":"1",
        "group":"B+",
        "tested": False,
        "status": None
    },
    {
        "donorID":"3",
        "group": "O+",
        "tested": False,
        "status": None
    }
]

def TestBlood():
    with open("BloodUnits.csv") as bu:
        reader = csv.DictReader(bu)

    for i in BloodUnits:
        if i["TESTED"]=="FALSE":
            i["STATUS"] = input("Please enter the result of blood test (accepted/rejected/blacklisted): ")
            i["TESTED"] = "TRUE"
            return
    print("No more Blood unit test pending. Enjoy your Day!\n")


if __name__ == "__main__":
    TestBlood()
    print(BloodUnits[0]["tested"])

