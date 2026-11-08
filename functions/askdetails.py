from functions.workernode import workernode
from functions.phoneinfo import get_phone_info
from functions.banner import bann_text
import os

def askdetails(mesgdcrt):
    try:
        os.system("clear")
        bann_text()
        cc, target = get_phone_info(mesgdcrt)
        while True:
            try:
                count = int(input(mesgdcrt.CommandMessage("Enter number of sms to send: ")).strip())
                delay = float(input(mesgdcrt.CommandMessage("Enter delay time (in seconds): ")).strip())
                max_thread_limit = (count//10) if (count//10) > 0 else 1
                max_threads = int(input(mesgdcrt.CommandMessage("Enter Number of Thread (Recommended: {max_limit}): ".format(max_limit=max_thread_limit))).strip())
                if (count < 0 or delay < 0):
                    raise Exception
                break
            except Exception:
                mesgdcrt.FailureMessage("Read Instructions Carefully !!!")
                print()
        workernode(mesgdcrt, cc, target, count, delay, max_threads)
    except KeyboardInterrupt:
        mesgdcrt.WarningMessage("Received INTR call - Exiting...")