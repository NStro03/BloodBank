rate_card = {
    "O+": 2000,
    "A+": 3000,
    "B+": 5000,
    "O-": 6000,
    "A-": 7000,
    "AB+": 10000,
    "B-": 12000,
    "AB-": 15000
}

def makePayment(units, bGrp):
    amount = rate_card[bGrp] * units
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


if __name__ == '__main__':
    makePayment(3, "A-")

