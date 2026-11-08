import string
import json
with open("isdcodes.json") as file:
    isdcodes = json.load(file)
country_codes = isdcodes["isdcodes"]

def get_phone_info(mesgdcrt):
    while True:
        target = ""
        cc = input(mesgdcrt.CommandMessage(
            "Enter your country code (Without +): "))
        cc = ''.join([n for n in cc if n in string.digits]).strip()
        if not country_codes.get(cc, False):
            mesgdcrt.WarningMessage(
                "The country code ({cc}) that you have entered"
                " is invalid or unsupported".format(cc=cc))
            continue
        target = input(mesgdcrt.CommandMessage(
            "Enter the target number: +" + cc + " "))
        target = ''.join([n for n in target if n in string.digits]).strip()
        if ((len(target) <= 6) or (len(target) >= 12)):
            mesgdcrt.WarningMessage(
                "The phone number ({target})".format(target=target) +
                "that you have entered is invalid")
            continue
        return (cc, target)