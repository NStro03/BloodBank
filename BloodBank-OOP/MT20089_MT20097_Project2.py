import csv
import copy

#TODO blood tester(staff),login,start of project,bloodunits
class User:

    __name = None
    __age = None
    __phoneNumber = None
    __gender = None
    __bloodGroup = None

    def __init__(self, name, age, phno, gender, bgrp):
        self.__name = name
        self.__age = age
        self.__phoneNumber = phno
        self.__gender = gender
        self.__bloodGroup = bgrp

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age

    def getPhNumber(self):
        return self.__phoneNumber

    def setPhNumber(self, phno):
        self.__phoneNumber = phno

    def GetGender(self):
        return self.__gender

    def SetGender(self, gender):
        self.__gender = gender

    def getBloodGroup(self):
        return self.__bloodGroup

    def setBloodGroup(self, bgrp):
        self.__bloodGroup = bgrp


class Customer(User):
    __customerID = None
    __dUnits = None
    __rUnits = None
    __Status = None

    def __init__(self, cid, name, age, phno, gender, bgrp,status="None"):
        super().__init__(name, age, phno, gender, bgrp)
        self.__customerID = cid
        self.__dUnits = 0
        self.__rUnits = 0
        self.__Status = status

    def getCustomerId(self):
        return self.__customerID

    def setCustomerId(self, customerid):
        self.__customerID = customerid

    def getDonatedUnits(self):
        return self.__dUnits

    def setDonatedUnits(self, dunits):
        self.__dUnits = dunits

    def getPastRequestedunits(self):
        return self.__rUnits

    def setCurrentRequestedUnits(self, runits):
        self.__rUnits = runits

    def getEligibleFreeUnitsCount(self):
        if self.__dUnits > self.__rUnits:
            return self.__dUnits - self.__rUnits
        else:
            return 0


class Staff(User):
    __staffID = None
    __acSample = None
    __rjSample = None

    def __init__(self, staffid, name, age, phno, gender, bgrp):
        super().__init__(name, age, phno, gender, bgrp)
        self.__staffID = staffid
        self.__acSample = 0
        self.__rjSample = 0

    def getStaffID(self):
        return self.__staffID

    def setStaffID(self, sid):
        self.__staffID = sid

    def getAcceptedSampleCount(self):
        return self.__acSample

    def incrementAcceptedSampleCount(self):
        self.__acSample = self.__acSample + 1

    def getRejectedSampleCount(self):
        return self.__rjSample

    def incrementRejectedSampleCount(self):
        self.__rjSample = self.__rjSample + 1


class Requester(Customer):

    __reqBloodGroup = None
    __reqUnits = None
    __sm = None

    def __init__(self, cid, name, age, phno, gender, bgrp,reqbgrp,requ,smobj):
        super().__init__(cid, name, age, phno, gender, bgrp)
        self.__reqUnits = requ
        self.__reqBloodGroup = reqbgrp
        self.__sm = smobj

    def getrequestedUnits(self):
        return self.__reqUnits

    def setrequestedUnits(self,requ):
        self.__reqUnits = requ

    def getReqBloodGroup(self):
        return self.__reqBloodGroup

    def setReqBloodGroup(self, bgrp):
        self.__reqBloodGroup = bgrp

    def request(self):
        Instock = self.__sm.stockDetails()

        if int(Instock[self.__reqBloodGroup]) < self.__reqUnits:
            print("We currently have {0} units of {1} available with us so we cannot fulfill your request".format(
                Instock[self.__reqBloodGroup], self.__reqBloodGroup))
            return

        free_units = self.getEligibleFreeUnitsCount()

        if self.__reqUnits <= free_units:
            self.__sm.DebitUnits(self.__reqBloodGroup, self.__reqUnits)
            x = (int(self.getPastRequestedunits()) + self.__reqUnits)
            self.setCurrentRequestedUnits(x)
            print(
                "Due to your previous donations to the bank,the requested blood units have been allotted to you for free")
        else:
            y_n = input("Would you like to purchase the blood units ? Y/N\n")
            if y_n == 'Y' or y_n == 'y':
                payable_units = self.__reqUnits - free_units
                pt=Payment()
                pay_status = pt.makePayment(payable_units, self.__reqBloodGroup)
                if not pay_status:
                    print("payment unsuccessful.\nPlease make request again")
                    return
                x = (int(self.getPastRequestedunits()) + self.__reqUnits)
                self.setCurrentRequestedUnits(x)
                print("Payment success")
                self.__sm.DebitUnits(self.__reqBloodGroup, self.__reqUnits)
            else:
                print("bye bye.\nBring money next time")


class Donor(Customer):

    __donBloodGroup = None
    __donUnits=None

    def __init__(self, cid, name, age, phno, gender, bgrp,donbgrp,donu):
        super().__init__(cid, name, age, phno, gender, bgrp)
        self.__donUnits=donu
        self.__donBloodGroup=donbgrp

    def getDonUnits(self):
        return self.__donUnits

    def setDonUnits(self,donu):
        self.__donUnits=donu

    def getDonBloodGroup(self):
        return self.__donBloodGroup

    def setDonBloodGroup(self, bgrp):
        self.__donBloodGroup = bgrp

    def donate(self):
        BT.testBlood()

        BloodUnits = []
        error_units = []
        Users = []
        i = 0
        with open("database/UserData.csv") as ud:
            reader = csv.DictReader(ud)
            for row in reader:
                Users.append(copy.deepcopy(row))

        with open("database/BloodUnits.csv") as bu:
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

        with open('database/UserData.csv', 'w') as s:
            fieldnames = ["ID", "NAME", "DONATED_UNITS", "REQUESTED_UNITS", "STATUS"]
            writer = csv.DictWriter(s, fieldnames=fieldnames)
            writer.writeheader()
            for j in Users:
                writer.writerow(j)

        i = 0
        with open('database/BloodUnits.csv', 'w') as s:
            fieldnames = ["DONOR_ID", "BLOOD_GROUP", "UNIT_COUNT", "TESTED", "STATUS"]
            writer = csv.DictWriter(s, fieldnames=fieldnames)
            writer.writeheader()
            for j in BloodUnits:
                i += 1
                if i in error_units or j["TESTED"] == "FALSE":
                    writer.writerow(j)


# class BloodTester(Staff):
#
#     __bloodUnitsToTest=[]
#     __UpdatedCustomerStatus=None
#     __userObjects=[]
#
#     def __init__(self,staffid, name, age, phno, gender, bgrp,):


class StockManagement:

    __Stock = {}

    def __init__(self):
        self.__Stock = self.stockDetails()

    def stockDetails(self):
        with open('database/stock_management.csv')as s:
            reader = csv.DictReader(s)
            for row in reader:
                temp = copy.deepcopy(row)
                # for k, v in row.items():
                #     print(k, v)
            return temp

    def creditUnits(self,blood, x):
        current_stock = self.stockDetails()
        t = int(current_stock[blood]) + x
        current_stock[blood] = "{}".format(t)
        with open('database/stock_management.csv', 'w')as s:
            fieldnames = ['A+', 'B+', 'AB+', 'O+', 'A-', 'B-', 'AB-', 'O-']
            writer = csv.DictWriter(s, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(current_stock)

    def DebitUnits(self,blood, x):
        current_data = self.stockDetails()

        if (int(current_data[blood]) < x):
            print("stock is less than the demanded")
            return
        t = int(current_data[blood]) - x
        current_data[blood] = "{}".format(t)
        with open('database/stock_management.csv', 'w')as s:
            fieldnames = ['A+', 'B+', 'AB+', 'O+', 'A-', 'B-', 'AB-', 'O-']
            writer = csv.DictWriter(s, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(current_data)


class Payment:

    __rate_card={}

    def __init__(self):
        self.__rate_card =self.BloodRate()


    def BloodRate(self):
        with open('database/Ratecard.csv')as s:
            reader = csv.DictReader(s)
            for row in reader:
                temp = copy.deepcopy(row)
                # for k, v in row.items():
                #     print(k, v)
            return temp


    def makePayment(self,units, bGrp):
        amount = int(self.__rate_card[bGrp]) * units
        print("For {0} units of {1} blood, you need to pay\n\tRs. {2}".format(units, bGrp, amount))
        paid = int(input("To pay, please type-in the amount that you are paying: "))
        paymentSuccess = False
        if paid < amount:
            print("There is no Bargaining in the matters of BLOOD!\n")
        elif paid == amount:
            paymentSuccess = True
            print("Your payment is successful!")
        else:
            print("Your generous donation along with the cost is most welcome!!")
            paymentSuccess = True

        return paymentSuccess


class BloodBank:

    def __init__(self):
        self.Stk = StockManagement()
        self.Stk.creditUnits('AB-',10)

    def requestBlood(self):

        Rq=Requester(23,"Nishkarsh",26,9876543210,"Male","A+","O-",2,self.Stk)
        Rq.request()



if __name__=="__main__":
    bb=BloodBank()
    # print(bb.Stk.stockDetails())
    bb.requestBlood()