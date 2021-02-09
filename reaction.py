import time
import random
import os
import threading
import msvcrt
import keyboard
import colorama

colorama.init(autoreset=True)

symbol_numbers = {
    "0": """
            ░█████╗░
            ██╔══██╗ 
            ██║░░██║ 
            ██║░░██║ 
            ╚█████╔╝ 
            ░╚════╝░""",
    "1": """ 
            ░░███╗░░
            ░████║░░ 
            ██╔██║░░ 
            ╚═╝██║░░ 
            ███████╗ 
            ╚══════╝ """,
    "2": """ 
            ██████╗░
            ╚════██╗ 
            ░░███╔═╝ 
            ██╔══╝░░ 
            ███████╗ 
            ╚══════╝ """,
    "3": """ 
            ██████╗░
            ╚════██╗ 
            ░█████╔╝ 
            ░╚═══██╗ 
            ██████╔╝ 
            ╚═════╝░ """,
    "4": """ 
            ░░██╗██╗
            ░██╔╝██║ 
            ██╔╝░██║ 
            ███████║ 
            ╚════██║ 
            ░░░░░╚═╝""",
    "5": """ 
            ███████╗
            ██╔════╝ 
            ██████╗░ 
            ╚════██╗ 
            ██████╔╝ 
            ╚═════╝░ """,
    "6": """ 
            ░█████╗░
            ██╔═══╝░ 
            ██████╗░ 
            ██╔══██╗ 
            ╚█████╔╝ 
            ░╚════╝░ """,
    "7": """ 
            ███████╗
            ╚════██║
            ░░░░██╔╝
            ░░░██╔╝░
            ░░██╔╝░░
            ░░╚═╝░░░""",
    "8": """ 
            ░█████╗░
            ██╔══██╗
            ╚█████╔╝
            ██╔══██╗
            ╚█████╔╝
            ░╚════╝░""",
    "9": """
            ░█████╗░
            ██╔══██╗
            ╚██████║
            ░╚═══██║
            ░█████╔╝
            ░╚════╝░""",
    ":": """
            ██╗
            ╚═╝
            ░░░
            ░░░
            ██╗
            ╚═╝"""
}


def display_clear():
    os.system("CLS || clear")


def show(text, color=colorama.Fore.YELLOW):
    lines = ['' for _ in range(7)]
    for c in text:
        symbol = symbol_numbers[c].split('\n')
        for i, line in enumerate(symbol):
            lines[i] += color + line.strip() + ' '

    print(*lines, sep='\n')


warnings = 0


def quantum_of_mercy():
    global warnings
    while True:
        time.sleep(900)
        if warnings != 0:
            warnings -= 1


threading.Thread(target=quantum_of_mercy, daemon=True).start()

results = [1000000000000000]

colors = [i for i in colorama.Fore.__dict__.values() if i != "\x1b[30m"]

instruction = input("\nAre you need instruction for use this program?(Y, N): ")

if instruction.upper() in ["Y", "Д", "Д"]:
    display_clear()
    print("\nYou was start to training your reaction, with each step your reaction will be better and better.")
    time.sleep(2)

    print("\nYou must press 'Enter' when message will be on the display and after program will watch you result of "
          "your reaction.")
    time.sleep(2)

    print("\nThere are warnings in case you want to press the button before the specified time. "
          "\nBut! One warning will be deleted every fifteen minutes, so be careful.")
    time.sleep(2)

    print("\n- If you want to exit the program - in the point of pressing the 'Enter' button, enter - 'Exit'.")
    time.sleep(2)

    print("\n- If you want to clear the result, write 'clear'.")

    none = input("\nPress Enter to continue: ")

elif instruction.upper() in ["N", "Н", "Н"]:
    print("\nYou know what you're going for! :)")

else:
    while True:
        display_clear()
        instruction = input("Try again enter: ").upper()
        if instruction in ["Y", "Д", "Д", "N", "Н", "Н"]:
            break

ready = input("Are you ready?(Y, N): ")
if ready.upper() in ["Y", "Д", "Д"]:
    while True:
        enter = None
        seconds = random.randint(2, 12)


        def print_numbers(second):
            for counter in range(1, second):
                display_clear()
                print("\n" * 7)

                show(str(random.randint(0, 10000000)), random.choice(colors))
                time.sleep(0.5)

            display_clear()
            print("\n" * 7)

            print(colorama.Fore.GREEN + """
                        ███████╗███╗░░██╗████████╗███████╗██████╗░██╗
                        ██╔════╝████╗░██║╚══██╔══╝██╔════╝██╔══██╗██║
                        █████╗░░██╔██╗██║░░░██║░░░█████╗░░██████╔╝██║
                        ██╔══╝░░██║╚████║░░░██║░░░██╔══╝░░██╔══██╗╚═╝
                        ███████╗██║░╚███║░░░██║░░░███████╗██║░░██║██╗
                        ╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝""")


        threading.Thread(target=print_numbers, args=[seconds, ]).start()

        time_res = time.time() + seconds / 2

        bad_kid = False

        """def press_f10(second):
            time.sleep(second)
            keyboard.press("f10")


        threading.Thread(target=press_f10, args=[seconds / 2, ], daemon=True).start()
"""
        while time.time() <= time_res:
            key = ord(msvcrt.getch())
            if key == 13:
                bad_kid = True

        tic = time.perf_counter()
        enter = input()
        toc = time.perf_counter()

        if bad_kid:
            display_clear()

            warnings += 1

            print(colorama.Fore.RED +
                  "\t\t██████╗░░█████╗░██████╗░░░████████╗██╗░░██╗██╗███╗░░██╗░██████╗░██╗\n"
                  "\t\t██╔══██╗██╔══██╗██╔══██╗░░╚══██╔══╝██║░░██║██║████╗░██║██╔════╝░██║\n"
                  "\t\t██████╦╝███████║██║░░██║░░░░░██║░░░███████║██║██╔██╗██║██║░░██╗░██║\n"
                  "\t\t██╔══██╗██╔══██║██║░░██║░░░░░██║░░░██╔══██║██║██║╚████║██║░░╚██╗╚═╝\n"
                  "\t\t██████╦╝██║░░██║██████╔╝░░░░░██║░░░██║░░██║██║██║░╚███║╚██████╔╝██╗\n"
                  "\t\t╚═════╝░╚═╝░░╚═╝╚═════╝░░░░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝\n")

            time.sleep(3)

            print("Warnings:", colorama.Fore.RED + str(warnings), "/", colorama.Fore.LIGHTRED_EX + "3")

            time.sleep(2)

            print("\nWe will not pretend to be a good cop and a bad cop and disclose whether it was intentional "
                  "or accidental. "
                  "\nJust be careful. :)")

            ok = input("\nOkay? Press Enter: ")

        else:
            results.append(toc - tic)
            if min(results) > toc - tic:
                display_clear()
                print("\n" * 7)
                record_list = ["██████╗░███████╗░█████╗░░█████╗░██████╗░██████╗░██╗",
                               "██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║",
                               "██████╔╝█████╗░░██║░░╚═╝██║░░██║██████╔╝██║░░██║██║",
                               "██╔══██╗██╔══╝░░██║░░██╗██║░░██║██╔══██╗██║░░██║╚═╝",
                               "██║░░██║███████╗╚█████╔╝╚█████╔╝██║░░██║██████╔╝██╗",
                               "╚═╝░░╚═╝╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝\n"]

                for part in record_list:
                    print("\t" * 3 + colorama.Fore.YELLOW + part)
                    time.sleep(0.4)

                time.sleep(2)

            results = [min(results)]

            print(f"Your reaction time is {toc - tic} seconds!")
            print(f"Your best result is {min(results)} seconds!")
            none = input("Press Enter to continue: ")

            if none.lower() == "exit":
                display_clear()
                print("\n" * 7)
                print(colorama.Fore.YELLOW +
                      '\t\t██╗░░██╗░█████╗░██╗░░░██╗███████╗░░░█████╗░░░░██████╗░░█████╗░░█████╗░██████╗░\n'
                      '\t\t██║░░██║██╔══██╗██║░░░██║██╔════╝░░██╔══██╗░░██╔════╝░██╔══██╗██╔══██╗██╔══██╗\n'
                      '\t\t███████║███████║╚██╗░██╔╝█████╗░░░░███████║░░██║░░██╗░██║░░██║██║░░██║██║░░██║\n'
                      '\t\t██╔══██║██╔══██║░╚████╔╝░██╔══╝░░░░██╔══██║░░██║░░╚██╗██║░░██║██║░░██║██║░░██║\n'
                      '\t\t██║░░██║██║░░██║░░╚██╔╝░░███████╗░░██║░░██║░░╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝\n'
                      '\t\t╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝░░╚═╝░░╚═╝░░░╚═════╝░░╚════╝░░╚════╝░╚═════╝░\n',

                      colorama.Fore.YELLOW + '\t\t\t\t\t████████╗██╗███╗░░░███╗███████╗██╗\n'
                                             '\t\t\t\t\t╚══██╔══╝██║████╗░████║██╔════╝██║\n'
                                             '\t\t\t\t\t░░░██║░░░██║██╔████╔██║█████╗░░██║\n'
                                             '\t\t\t\t\t░░░██║░░░██║██║╚██╔╝██║██╔══╝░░╚═╝\n'
                                             '\t\t\t\t\t░░░██║░░░██║██║░╚═╝░██║███████╗██╗\n'
                                             '\t\t\t\t\t░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝\n')

                time.sleep(2)
                display_clear()
                break

            elif none.lower() == "clear":
                results.clear()
                print("\nThe result was cleared successfully!")
                time.sleep(2)



elif ready.upper() in ["N", "Н", "Н"]:
    timer = input("Can I set a timer for waiting?(Y, N): ")
    if timer.upper().startswith("Y"):
        while True:
            while True:
                try:
                    times = int(input("\nEnter the number of seconds for how many I need to set the timer: "))
                    break
                except TypeError:
                    pass

            print("\nIf you want to stop the timer, press button 'S'.")

            time.sleep(2)

            event = threading.Event()
            event.set()


            def stop_timer():
                def pressed_keys(e):
                    if e.name in ["s", "ы", "і"]:
                        event.clear()

                keyboard.hook(pressed_keys)
                keyboard.wait()


            hours = times // 3600
            minutes = (times - hours * 3600) // 60
            seconds = times - (hours * 3600) - (minutes * 60)

            seconds_start = seconds
            times_counter = 0

            display_clear()
            show(f"{str(hours).rjust(2, '0')}:{str(minutes).rjust(2, '0')}:{str(seconds).rjust(2, '0')}")
            time.sleep(1)

            while times_counter != times:
                for i in range(1, seconds_start + 1):
                    if event.is_set():
                        seconds = seconds_start
                        seconds -= i
                        times_counter += 1

                        display_clear()
                        show(f"{str(hours).rjust(2, '0')}:{str(minutes).rjust(2, '0')}:{str(seconds).rjust(2, '0')}")

                        time.sleep(1)

                if minutes == 0 or str(minutes)[0] == "-" and times >= 3600:
                    hours -= 1
                    minutes = 60

                minutes -= 1
                seconds_start = 60

            else:
                while True:
                    continue_or_again = input("Do you want continue?(Y, N): ").upper()
                    if continue_or_again in ["Y", "Д", "Д"]:
                        event.set()
                        continue
                    elif continue_or_again in ["N", "Н", "Н"]:
                        break
