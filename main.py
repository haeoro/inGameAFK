# Universal anti kick script. | Created by haeoro

import os
import pydirectinput
import time
import banners


def afk():
    start = time.localtime()
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
        os.system("cls")
        end = time.localtime()
        elapsed_time = [end[3] - start[3], end[4] - start[4], end[5] - start[5]]
        print("""   Time spent AFK
        
        Hours: {}
        Minutes: {}
        Seconds: {}
        
        """.format(elapsed_time[0], elapsed_time[1], elapsed_time[2]))
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
