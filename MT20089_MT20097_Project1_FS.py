import User as u


def exitSystem():
    print("Thank you for visiting our Blood Bank,  Keep Donating!\nKyunki...\n"
          "Boond boond se hi Sagar banta hai!")
    exit(0)


def BloodBank():
    print("########################################################################################"
          "\n\t\t\t\t\t!Welcome to S&N's International Blood Bank!\n"
          "########################################################################################")
    while True:
        switcher = {
            1: u.existingUser,
            2: u.newUser,
            0: exitSystem
        }
        inp = int(input("Are you...\n\t1. Existing User\n\t2. New User\n\t0. Exit"
                        "\nMake your Choice: "))
        func = switcher.get(inp, lambda: "enter valid input")
        func()


if __name__ == '__main__':
    BloodBank()

