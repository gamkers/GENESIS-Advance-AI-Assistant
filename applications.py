from os import startfile
from time import sleep
from keyboard import write
from pyautogui import click
from features import talk
import operator
from features import  sounds
from features import take_command
import smtplib
def mind_game():
    talk("yes sir, choose a number between 1-9")
    talk("got it?")
    talk("multiply your number by 9 sir")
    talk("have your time")
    talk(".")
    talk(".")
    talk("you got a two digit number sir?")
    talk("if you got ,  add the both number sir")
    talk("for example if you got 13, add 1 and 3 and made it 4")
    talk("done?")
    talk("minus 6 from your number sir")
    talk("now fix a alphabet to your number, like a for 1, b for 2, c for 3, d for 4, like that")
    talk("choose a country and a pet animal with your alphabet")
    talk("got it?")
    talk("now look at me")
    talk("the country u chosen is canada and cat as a pet and finally your number is 3")
    talk("how is it sir?")

def calc(my_string):
    print(my_string)

    def get_operator_fn(op):
        return {
            '+': operator.add,
            '-': operator.sub,
            'x': operator.mul,
            'divided': operator.__truediv__,
        }[op]

    def eval_binary_expr(op1, oper, op2):
        op1, op2 = int(op1), int(op2)
        return get_operator_fn(oper)(op1, op2)

    talk("Your result is")
    talk(eval_binary_expr(*(my_string.split())))

def mail():
    talk("to whom you want to send a mail sir")
    receiver = input("type the mail: ")
    talk("what message do you want to send sir ")
    message = take_command()
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("gamkerac3@gmail.com", "Qawsed@123")
    server.sendmail("gamkerac3@gmail.com", "receiver", message)
    print("sending message to the" + receiver)
    sounds()
    talk("sending mail")
    talk("message sent")

def WhatsappMsg(name, message):
    sounds()
    startfile('C:\\Users\\idmak\\AppData\\Local\\WhatsApp\\WhatsApp.exe')
    sleep(4)
    click(x=260, y=130)
    sleep(3)
    write(name)
    sleep(3)
    click(x=230, y=290)
    sleep(3)
    click(x=800, y=1050)
    sleep(3)
    write(message)

def WhatsappCall(name):
    sounds()
    talk("connecting")
    startfile('C:\\Users\\idmak\\AppData\\Local\\WhatsApp\\WhatsApp.exe')
    sleep(2)
    click(x=260, y=130)
    sleep(1)
    write(name)
    sleep(1)
    click(230, y=290)
    sleep(1)
    click(x=1730, y=90)

def WhatsappChat(name):
    startfile('C:\\Users\\idmak\\AppData\\Local\\WhatsApp\\WhatsApp.exe')
    sleep(10)
    click(x=260, y=130)
    sleep(1)
    write(name)
    sleep(1)
    click(230, y=290)
    sleep(1)
    click(x=1660, y=90)
    sleep(1)

