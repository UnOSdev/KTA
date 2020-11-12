import keyboard as kb
import subprocess as sbp
import time
import os
from difflib import get_close_matches

def main(id):
    try:
        time.sleep(0.5)
        press = input()
        if press == '!home':
            sbp.getoutput("adb -s "+id+" shell input keyevent HOME")
            main(id)
        elif press == '!back':
            sbp.getoutput("adb -s "+id+" shell input keyevent BACK")
            main(id)
        elif press == '!power':
            sbp.getoutput("adb -s "+id+" shell input keyevent POWER")
            main(id)
        elif press == '!enter':
            sbp.getoutput("adb -s "+id+" shell input keyevent ENTER")
            main(id)
        elif press == '!vup':
            sbp.getoutput("adb -s "+id+" shell input keyevent VOLUME_UP")
            main(id)
        elif press == '!vdown':
            sbp.getoutput("adb -s "+id+" shell input keyevent VOLUME_DOWN")
            main(id)
        elif press == '!help':
            sbp.run('clear',shell=True)
            sbp.run('cls',shell=True)
            print("!help = This list\n!home = Simulate HOME button\n!back = Simulate BACK button\n!power = Simulate POWER button\n!enter = Simulate ENTER button or break line\n!vup = Simulate VOLUME UP button\n!vdown = Simulate VOLUME DOWN button\n!fakeboot = Running infinity boot animation, CTRL + C to stop(can not work on new androids)\nCTRL + C to exit the program ")
        elif press == '!fakeboot':
            try:
                print('Fake boot is can not working on last android versions, also this function needs root on device(CTRL + C for exit)')
                sbp.run("adb -s "+id+" shell su ",shell=True,stdout=sbp.DEVNULL,stderr=sbp.DEVNULL)
                main(id)
            except KeyboardInterrupt:
                print("OK")
                main(id)
        elif press == '':
            print("Value error")
            main(id)
        else:
            pass
        press = press.split()
        wordsWithSpace = ''
        for x in press:
            wordsWithSpace+= "%s"+x
        checkError = sbp.getoutput("adb -s "+id+" shell input text '"+ wordsWithSpace +"'")
        checkError = checkError.split().pop()
        if checkError == 'found':
            print("Device serial number error, check cable!")
            sbp.run('exit',shell=True)
            quit()
        else:
            main(id)
    except KeyboardInterrupt:
        print('\nBye bye')
        quit()
    except:
        main(id)
def connect():
    try:
        os.system('clear')
        device = os.popen("adb devices").read().split('\n', 1)[1].split("device")[0].strip()
        cheaker = list(device)
        if cheaker == []:
            print("No device detected")
            b = input("Restart program?(y/n): ")
            if b == 'y':
                connect()
            elif b == 'n':
                quit()
            else:
                print("Error you may not writed 'y' or 'n', aborting program.")
        a = get_close_matches('emulator', [device])
        if a != []:
            print("Detected emulator,continue...")
            print("...")
            time.sleep(0.5)
            print("...")
            main(device)
        else:
            print("Detected " + device + " device, continue... ")
            print("...")
            time.sleep(0.5)
            print("...")
            print("Do not forget to turn on USB DEBUGGING in your phone")
            main(device)
    except IndexError:
        print("ADB module not found, are you sure that you installed it?\n If you are in Windows just copy the .py(this) file to adb, and run it.")
        input()
        quit()

if __name__ == "__main__":
    connect()
