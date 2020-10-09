import csv
import copy

def donate():
    print("donated")
    int
    int(input("Enter no. og units you want to donate"))


def request():
    print("requested")


def logout():
    return

def customer():
    id =""+input("please enter your userid to login : ")
    current_user=None


    with open('UserData.csv')as s:
        reader = csv.DictReader(s)
        for row in reader:
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
        func()






if __name__=="__main__":
    customer()

