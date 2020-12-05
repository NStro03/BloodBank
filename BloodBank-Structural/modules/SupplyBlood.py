from modules import Payment as pt, StockManagement as st


def supply(blood_grp, requested, current_user):
    Instock = st.stockDetails()

    if int(Instock[blood_grp]) < requested:
        print("We currently have {0} units of {1} available with us so we cannot fulfill your request".format(
            Instock[blood_grp], blood_grp))
        return

    free_units = int(current_user["DONATED_UNITS"]) - int(current_user["REQUESTED_UNITS"])

    if requested <= free_units:
        st.DebitUnits(blood_grp, requested)
        x = (int(current_user["REQUESTED_UNITS"]) + requested)
        current_user["REQUESTED_UNITS"] = str(x)
        print("Due to your previous donations to the bank,the requested blood units have been allotted to you for free")
    else:
        y_n = input("Would you like to purchase the blood units ? Y/N\n")
        if y_n == 'Y' or y_n == 'y':
            payable_units = requested - free_units
            pay_status = pt.makePayment(payable_units, blood_grp)
            if not pay_status:
                print("payment unsuccessful.\nPlease make request again")
                return
            x = (int(current_user["REQUESTED_UNITS"]) + free_units)
            current_user["REQUESTED_UNITS"] = str(x)
            print("Payment success")
            st.DebitUnits(blood_grp, requested)
        else:
            print("bye bye.\nBring money next time")


if __name__ == '__main__':
    curr_user = {
        # TODO fill dummy values
        }
    bgrp = "A+"
    req = 10
    supply(bgrp, req, curr_user)

