
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

    def __init__(self, cid, name, age, phno, gender, bgrp):
        super().__init__(name, age, phno, gender, bgrp)
        self.__customerID = cid
        self.__dUnits = 0
        self.__rUnits = 0

    def getCustomerId(self):
        return self.__customerID

    def setCustomerId(self, customerid):
        self.__customerID = customerid

    def getDonatedUnits(self):
        return self.__dUnits

    def setDonatedUnits(self, dunits):
        self.__dUnits = dunits

    def getRequestedunits(self):
        return self.__rUnits

    def setRequestedUnits(self, runits):
        self.__rUnits = runits

    def getElligibleFreeUnitsCount(self):
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



