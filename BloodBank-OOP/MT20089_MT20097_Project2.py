
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


# class Customer(User):

