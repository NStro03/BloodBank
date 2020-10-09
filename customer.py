import csv
import copy
import StockManagement as st
import Payment as pt

Blood_groups=['A+','B+','AB+','O+','A-','B-','AB-','O-']
def donate(current_user): #TODO implement blacklist condition
    print("donated")
    temp=int(input("Enter no. of units you want to donate : "))
    blood_group=input("Enter your blood group : ")
    if not blood_group in Blood_groups:
        print("This Blood Group is currently not being accepted by human race .\nWhen the aliens arrive"
              " we will let you know")
        return
    Donated_blood={
                   'DONOR_ID':current_user["ID"],
                   'BLOOD_GROUP':blood_group,
                   'UNIT_COUNT':temp,
                   'TESTED':"FALSE",
                   'STATUS':"None"
                   }
    with open("BloodUnits.csv") as bu:
        reader = csv.DictReader(bu)
        i = 0
        BloodUnits = []
        for row in reader:
            BloodUnits.append(copy.deepcopy(row))

    BloodUnits.append(Donated_blood)

    with open('BloodUnits.csv', 'w') as s:
        fieldnames = ["DONOR_ID", "BLOOD_GROUP", "UNIT_COUNT", "TESTED", "STATUS"]
        writer = csv.DictWriter(s, fieldnames=fieldnames)
        writer.writeheader()
        for i in BloodUnits:
            # print(i)
            writer.writerow(i)

    current_user["DONATED_UNITS"]=str((int(current_user["DONATED_UNITS"]))+temp)
    print("Your sample has been collected,once the blood test is done if accepted then reflect in your account")

def request(current_user):
    print("requested")
    blood_grp=input("Which blood group you want ? ")

    if not blood_grp in Blood_groups:
        print("This Blood Group is currently not in stock .\nAs the aliens  have not arrived yet")
        return

    requested = int(input("Enter no. of blood units you wanted : "))
    Instock=st.stockDetails()

    if int(Instock[blood_grp]) < requested:
        print("We currently have {0} units of {1} available with us so we cannot fulfill your request".format(Instock[blood_grp],blood_grp))
        return

    free_units=int(current_user["DONATED_UNITS"])-int(current_user["REQUESTED_UNITS"])

    if requested <= free_units:
        st.DebitUnits(blood_grp,requested)
        x=(int(current_user["REQUESTED_UNITS"])+requested)
        current_user["REQUESTED_UNITS"]=str(x)
        print("Due to your previous donations to the bank,the requested blood units have been allotted to you for free")
    else:
        y_n=input("Would you like to purchase the blood units ? Y/N\n")
        if y_n=='Y' or y_n=='y':
            payable_units=requested-free_units
            pay_status=pt.makePayment(payable_units,blood_grp)
            if  not pay_status:
                print("payment unsuccessful.\nPlease make request again")
                return
            x = (int(current_user["REQUESTED_UNITS"]) + free_units)
            current_user["REQUESTED_UNITS"] = str(x)
            print("Payment success")
            st.DebitUnits(blood_grp,requested)
        else:
            print("bye bye.\nBring money next time")


def logout():
    return

def customer():
    id =""+input("please enter your userid to login : ")
    current_user=None

    users=[]
    with open('UserData.csv')as s:
        reader = csv.DictReader(s)
        for row in reader:
            users.append(copy.deepcopy(row))
            if row["ID"]==id:
                current_user=copy.deepcopy(row)
                break

    if current_user is None:
        print("User doesn't exist!!\n Enter a valid user id or Please register ")
        return

    print("Welcome {}".format(current_user["NAME"]))
    while (True):
        switcher = {
            1: donate,
            2: request
        }
        inp = int(input("What do you want to do :\n\t1. Donate Blood\n\t2. Request Blood\n\t0. Logout\n"
                        "Make your choice: "))
        if inp==0:
            return

        func=switcher.get(inp,lambda : "enter valid input")
        func(current_user)
        for i in range(len(users)):
            if current_user["ID"]==users[i]["ID"]:
                users[i]=copy.deepcopy(current_user)

        with open('UserData.csv', 'w') as s:
            fieldnames = ["ID", "NAME", "DONATED_UNITS", "REQUESTED_UNITS", "STATUS"]
            writer = csv.DictWriter(s, fieldnames=fieldnames)
            writer.writeheader()
            for j in users:
                # print(i)
                writer.writerow(j)







if __name__=="__main__":
    customer()

