import string

def get_phone_info(mesgdcrt):
    while True:
        target = input(mesgdcrt.CommandMessage("Enter the target number: +91" + " "))
        if (len(target) != 10 or not target.isdigit()):
            mesgdcrt.WarningMessage("The phone number ({target}) that you have entered is invalid".format(target=target))
            continue
        return target