# Universal anti kick script. | Created by haeoro

import os
import pydirectinput
import time
import banners


def afk():
    start = time.strftime("%H:%M:%S")
    try:
        print("\n\n    Press CTRL-C to quit. ")

        while True:
            pydirectinput.press("w")
            time.sleep(1)
            pydirectinput.press("a")
            time.sleep(1)
            pydirectinput.press("s")
            time.sleep(1)
            pydirectinput.press("d")
    except KeyboardInterrupt:
        end = time.strftime("%H:%M:%S")
        os.system("cls")
        print("\n    From start to finish: ")
        print("\n\n    Start time: {}".format(start))
        print("    Finish time: {}".format(end))
        time.sleep(5)


def countdown():
    os.system("cls")
    timer = 5
    banners.header()
    while timer != -1:
        time.sleep(1)
        print("    Time until AFK: {}".format(timer), end="\r")
        timer = timer - 1


def main():
    countdown()
    afk()
    

if __name__ == "__main__":
    main()

'''
        to-do 

    ~ get total time elapsed since starting the afk program (also account for the seconds where the main process is sleeping.)
    
'''
