from keyboard import write
import pyautogui
from features import *

def codder():
    cmd=take_command()
    if "call" in cmd:
        talk("function name?")
        fun = take_command().replace(" ","_")
        write(f"{fun}()")
        pyautogui.hotkey('shift', "enter")
    elif "function" in cmd:
        talk("What did you want to call the function sir?")
        name=take_command().replace(" ","_")
        write(f"def {name} ():")
        pyautogui.press('enter')
        write("pass")

    if "input" in cmd:
        talk("mention your input type")
        intype=take_command()
        talk("Variable name?")
        var = take_command().replace(" ","_")
        if intype=="string":
            write(f"{var}=input(type your input: )")
        elif intype=="integer":
            write(f"{var}=int(input(type your input: ))")
        elif intype=="integer array":
            write(f"{var}=list(map(int, input('Type number with space: ').split()))")
        elif intype=="list":
            write(f"{var}=list(map(input('Type items with space: ').split()))")
        pyautogui.press('enter')

    elif "print variable" in cmd:
        talk("variable name")
        var=take_command().replace(" ","_")
        write(f"print({var})")
        pyautogui.press('enter')
    elif "print " in cmd:
        write(f"print('{cmd.replace('print','')[1:]}')")
        pyautogui.press('enter')
    elif "for" in cmd:
        talk("mention the name of the list")
        var=take_command().replace(" ","_")
        write(f"for number in {var}:")
        pyautogui.press('enter')
    elif"odd or even" in cmd:
        talk("variable name?")
        var=take_command()
        write(f"if int({var})%2==0:")
        pyautogui.press('enter')
        write(f"print({var})")
        pyautogui.press('enter')



    elif"stop" in cmd:
        False


    else:
        while True:
            codder()

