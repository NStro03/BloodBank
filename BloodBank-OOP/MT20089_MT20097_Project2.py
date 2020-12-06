import csv
import copy

#TODO blood tester(staff)
class User:

    __name = None

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name


class Customer(User):
    __customerID = None
    __dUnits = None
    __rUnits = None
    __Status = None

    def __init__(self, cid, name, status="None"):
        super().__init__(name)
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
        # print("du",dunits,"selfdu:",self.__dUnits)

    def getPastRequestedunits(self):
        return self.__rUnits

    def setCurrentRequestedUnits(self, runits):
        self.__rUnits = runits
        # print("du", runits, "selfdu:", self.__rUnits)

    def getEligibleFreeUnitsCount(self):
        # print("R:{0} D:{1}".format(self.__rUnits, self.__dUnits))
        if self.__dUnits > self.__rUnits:
            return self.__dUnits - self.__rUnits
        else:
            return 0

    def getStatus(self):
        return self.__Status

    def setStatus(self, s):
        self.__Status = s


class Staff(User):
    __staffID = None
    __acSample = None
    __rjSample = None

    def __init__(self, staffid, name):
        super().__init__(name)
        self.__staffID = staffid
        self.__acSample = 0
        self.__rjSample = 0

    def getStaffID(self):
        return self.__staffID

    def setStaffID(self, sid):
        self.__staffID = sid

    def getAcceptedSampleCount(self):
        return self.__acSample

    def setAcceptedSampleCount(self, accCount):
        self.__acSample = accCount

    def incrementAcceptedSampleCount(self):
        self.__acSample = self.__acSample + 1

    def getRejectedSampleCount(self):
        return self.__rjSample

    def setRejectedSampleCount(self, rejCount):
        self.__rjSample = rejCount

    def incrementRejectedSampleCount(self):
        self.__rjSample = self.__rjSample + 1


class Requester(Customer):

    __reqBloodGroup = None
    __reqUnits = None
    __sm = None

    def __init__(self, cid, name, reqbgrp, requ, smobj):
        super().__init__(cid, name)
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
    __donUnits = None

    def __init__(self, cid, name,  donbgrp, donu):
        super().__init__(cid, name)
        self.__donUnits = donu
        self.__donBloodGroup = donbgrp

    def getDonUnits(self):
        return self.__donUnits

    def setDonUnits(self,donu):
        self.__donUnits=donu

    def getDonBloodGroup(self):
        return self.__donBloodGroup

    def setDonBloodGroup(self, bgrp):
        self.__donBloodGroup = bgrp

    def donate(self):

        if self.getStatus() == "blacklisted":
            print(
                "Due to an incurable disease in your blood, you have been barred from donating blood\n You may continue "
                "to request blood from our blood bank in the future.")
            return
        # temp = int(input("Enter no. of units you want to donate : "))
        # blood_group = input("Enter your blood group : ")
        acceptableBGroups = []
        with open('database/AcceptableBloodGroups.csv')as s:
            bgs = list(csv.reader(s))
            # print("bgs: ", bgs)
            for bg in bgs[0]:
                acceptableBGroups.append(bg)

        # print(acceptableBGroups)
        if not self.getDonBloodGroup() in acceptableBGroups:
            print("This Blood Group is currently not being accepted by human race .\nWhen the aliens arrive"
                  " we will let you know")
            return
        bu = BloodUnit(self.getCustomerId(), self.__donBloodGroup, self.__donUnits)
        return bu
        # Donated_blood = {
        #     'DONOR_ID': current_user["ID"],
        #     'BLOOD_GROUP': blood_group,
        #     'UNIT_COUNT': temp,
        #     'TESTED': "FALSE",
        #     'STATUS': "None"
        # }
        # with open("database/BloodUnits.csv") as bu:
        #     reader = csv.DictReader(bu)
        #     BloodUnits = []
        #     for row in reader:
        #         BloodUnits.append(copy.deepcopy(row))
        #
        # BloodUnits.append(Donated_blood)
        #
        # with open('database/BloodUnits.csv', 'w') as s:
        #     fieldnames = ["DONOR_ID", "BLOOD_GROUP", "UNIT_COUNT", "TESTED", "STATUS"]
        #     writer = csv.DictWriter(s, fieldnames=fieldnames)
        #     writer.writeheader()
        #     for i in BloodUnits:
        #         # print(i)
        #         writer.writerow(i)
        #
        # print("Your sample has been collected,once the blood test is done if accepted then reflect in your account")


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


class BloodUnit:
    __donorID = None
    __bloodGroup = None
    __unitCount = None
    __tested = None
    __status = None

    def __init__(self, did, bgrp, ucount):
        self.__donorID = did
        self.__bloodGroup = bgrp
        self.__unitCount = ucount
        self.__tested = False

    def getBloodGroup(self):
        return self.__bloodGroup

    def setBloodGroup(self, bgrp):
        self.__bloodGroup = bgrp

    def getDonorID(self):
        return self.__donorID

    def setDonorID(self, id):
        self.__donorID = id

    def getUnitCount(self):
        return self.__unitCount

    def setUnitCount(self, uc):
        self.__unitCount = uc

    def getTested(self):
        return self.__tested

    def setTested(self, tested):
        self.__tested = tested

    def getStatus(self):
        return self.__status

    def setStatus(self, st):
        self.__status = st


class UserManagement:
    __CustList = []
    __StaffList = []

    def __init__(self):
        self.loadcustomerList()
        self.loadstafflist()

    def loadstafflist(self):
        with open('database/StaffData.csv')as s:
            reader = csv.DictReader(s)
            for row in reader:
                temp = Staff(int(row["ID"]), row["NAME"])
                temp.setAcceptedSampleCount(int(row["ACCEPTED_UNITS"]))
                temp.setRejectedSampleCount(int(row["REJECTED_UNITS"]))
                self.addStaffToList(temp)

    def loadcustomerList(self):
        with open('database/CustomerData.csv')as s:
            reader = csv.DictReader(s)
            for row in reader:
                trow = copy.deepcopy(row)
                temp = Customer(int(trow["ID"]), trow["NAME"])
                temp.setDonatedUnits(int(trow["DONATED_UNITS"]))
                # print(int(trow["DONATED_UNITS"]))
                temp.setCurrentRequestedUnits(int(trow["REQUESTED_UNITS"]))
                temp.setStatus(trow["STATUS"])
                self.addCustomerToList(temp)
                # self.__CustList.append(temp)
                # print(len(self.__CustList))

            # for i in self.__CustList:
            #     print("I:{0} N:{1} D:{2} R:{3} S:{4}".format(i.getCustomerId(), i.getName(), i.getDonatedUnits(),
            #                                                  i.getPastRequestedunits(), i.getStatus()))

    def getCustomerList(self):
        return self.__CustList

    def addCustomerToList(self, cust):
        self.__CustList.append(cust)

    def removeCustomerFromList(self, cust):
        if cust in self.__CustList:
            self.__CustList.remove(cust)

    def getStaffList(self):
        return self.__StaffList

    def addStaffToList(self, staff):
        self.__StaffList.append(staff)

    def removeStaffFromList(self, staff):
        if staff in self.__StaffList:
            self.__StaffList.remove(staff)

    def login(self, usrRole, usrID):
        if usrRole == "Customer":
            for c in self.__CustList:
                if c.getCustomerId() == usrID:
                    return c
        else:
            for s in self.__StaffList:
                if s.getStaffID() == usrID:
                    return s

        print("User doesn't exist!!\n Enter a valid user id or Please register ")

    def register(self, name):

        cid = len(self.__CustList) + 1
        c = Customer(cid, name)
        self.addCustomerToList(c)
        print(
            "Hi {0}, You have been succesfully registered to our Blood Bank. Please use the below user ID to login to "
            "our system.\n\tUser ID: {1}".format(name, cid))

        return

    # def __del__(self):
    #     with open('database/CustomerData.csv', 'w') as s:
    #         fieldnames = ["ID", "NAME", "DONATED_UNITS", "REQUESTED_UNITS", "STATUS"]
    #         writer = csv.writer(s)
    #         writer.writerow(fieldnames)
    #
    #         for j in self.__CustList:
    #             # print(i)
    #             writer.writerow(j.getCustomerId(),j.getName(),j.getDonatedUnits(),j.getPastRequestedunits(),j.getStatus())
    #
    #     with open('database/StaffData.csv', 'w') as s:
    #         fieldnames = ["ID", "NAME", "ACCEPTED_UNITS", "REJECTED_UNITS"]
    #         writer = csv.writer(s)
    #         writer.writerow(fieldnames)
    #
    #         for j in self.__StaffList:
    #             # print(i)
    #             writer.writerow(j.getStaffId(),j.getName() ,j.getAcceptedSampleCount(),j.getRejectedSampleCount())


class BloodBank:
    Stk = None
    user = None
    bloodUnits = []
    currentUser = None

    def __init__(self):
        self.Stk = StockManagement()
        self.user = UserManagement()
        with open('database/BloodUnits.csv') as s:
            reader = csv.DictReader(s)
            for row in reader:
                trow = copy.deepcopy(row)
                temp = BloodUnit(int(trow["DONOR_ID"]), trow["BLOOD_GROUP"], trow["UNIT_COUNT"])
                temp.setTested(int(trow["TESTED"]))
                temp.setStatus(int(trow["STATUS"]))
                self.bloodUnits.append(temp)

    def requestBlood(self):
        reqbg = input("Which Blood group are you looking for?\n")
        bgcount = int(input("How many units of {} do you require?".format(reqbg)))
        rq = Requester(self.currentUser.getCustomerId(), self.currentUser.getName(), reqbg, bgcount, self.Stk)
        rq.setCurrentRequestedUnits(self.currentUser.getPastRequestedunits())
        rq.setDonatedUnits(self.currentUser.getDonatedUnits())
        rq.request()
        self.currentUser.setCurrentRequestedUnits(rq.getPastRequestedunits())

    def donateBlood(self):
        donbg = input("Which Blood group do you want to donate?\n")
        bgcount = int(input("How many units of {} do you wish to donate?".format(donbg)))
        dn = Donor(self.currentUser.getCustomerId(), self.currentUser.getName(), donbg, bgcount)
        dn.setCurrentRequestedUnits(self.currentUser.getPastRequestedunits())
        dn.setDonatedUnits(self.currentUser.getDonatedUnits())
        donatedBU = dn.donate()
        self.bloodUnits.append(donatedBU)
        self.currentUser.setDonatedUnits(dn.getDonatedUnits())

    def login(self):
        print("SALUTATION TO MY LORD!!")

        inp = int(input("Are you \n\t1. Customer\n\t2. Staff\n"
                        "Make your choice: "))

        if inp == 1:
            inp2 = int(input("Please Enter your id :"))
            self.currentUser = self.user.login("Customer", inp2)
        elif inp == 2:
            inp2 = int(input("Please Enter your id :"))
            self.currentUser = self.user.login("Staff", inp2)
        else:
            print("Please Login again and Enter a valid Role")
            return None

        print("Welcome {}".format(self.currentUser.getName()))
        # print("D: ", self.currentUser.getDonatedUnits(), "\tR: ", self.currentUser.getPastRequestedunits())

        while True:
            if inp == 1:
                switcher = {
                    1: self.donateBlood,
                    2: self.requestBlood
                }
                cinp = int(input("What do you want to do :\n\t1. Donate Blood\n\t2. Request Blood\n\t0. Logout\n"
                                "Make your choice: "))
                if cinp == 0:
                    break

                func = switcher.get(cinp, lambda: "Enter valid input")
                func()
            # else:
        self.saveAndExit()

    def saveAndExit(self):
        # TODO Save and Exit fr BloodUnits and Staff flow.
        print(self.user.getCustomerList())
        with open('database/CustomerData.csv', 'w') as s:
            fieldnames = ["ID", "NAME", "DONATED_UNITS", "REQUESTED_UNITS", "STATUS"]

            custTemplate = {
                "ID": None,
                "NAME": None,
                "DONATED_UNITS": None,
                "REQUESTED_UNITS": None,
                "STATUS": None
            }
            writer = csv.DictWriter(s, fieldnames=fieldnames)
            writer.writeheader()
            # print(self.user.getCustomerList())
            for j in self.user.getCustomerList():
                temp = copy.deepcopy(custTemplate)
                temp["ID"] = j.getCustomerId()
                temp["NAME"] = j.getName()
                temp["DONATED_UNITS"] = j.getDonatedUnits()
                temp["REQUESTED_UNITS"] = j.getPastRequestedunits()
                temp["STATUS"] = j.getStatus()
                writer.writerow(temp)

        with open('database/StaffData.csv', 'w') as s:
            fieldnames = ["ID", "NAME", "ACCEPTED_UNITS", "REJECTED_UNITS"]

            stfTemplate = {
                "ID": None,
                "NAME": None,
                "ACCEPTED_UNITS": None,
                "REJECTED_UNITS": None
            }
            writer = csv.DictWriter(s, fieldnames=fieldnames)
            writer.writeheader()
            # print(self.user.getCustomerList())
            for j in self.user.getStaffList():
                temp = copy.deepcopy(stfTemplate)
                temp["ID"] = j.getStaffID()
                temp["NAME"] = j.getName()
                temp["ACCEPTED_UNITS"] = j.getAcceptedSampleCount()
                temp["REJECTED_UNITS"] = j.getRejectedSampleCount()
                writer.writerow(temp)

    def register(self):

        print("Noob DETECTED!!")
        name = input("Please enter your name: ")
        self.user.register(name)

    def printStockDetails(self):
        stockdet = self.Stk.stockDetails()
        print(stockdet)

    def printCustomerList(self):
        custList = self.user.getCustomerList()
        print(custList)

    def printStafflist(self):
        stafflist = self.user.getStaffList()
        print(stafflist)




if __name__ == "__main__":
    bb = BloodBank()

    def exitSystem():
        print("Thank you for visiting our Blood Bank,  Keep Donating!\nKyunki...\n"
              "Boond boond se hi Sagar banta hai!")
        exit(0)


    print("########################################################################################"
          "\n\t\t\t\t\t!Welcome to S&N's International Blood Bank!\n"
          "########################################################################################")
    while True:
        switcher = {
            1: bb.login,
            2: bb.register,
            0: exitSystem
        }
        inp = int(input("Are you...\n\t1. Existing User\n\t2. New User\n\t0. Exit"
                        "\nMake your Choice: "))
        func = switcher.get(inp, lambda: "enter valid input")
        func()
        # print(u.getCustomerId())


