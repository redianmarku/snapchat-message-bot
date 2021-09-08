import pyautogui as pag
import keyboard, time, pyperclip

yourMessage = input("What message do you want to send in the chats?: ")

while yourMessage == "":
    print("Please put your message!")
    yourMessage = input("What message do you want to send in the chats?: ")

howMany = int(input('How many chats you want to send message?: '))

print("\nNow open Snapchat in your emulator and place the mouse in one of your chats, then press enter on here...")
while True:
    if keyboard.read_key() == "enter":
        print("Starting bot...")
        time.sleep(3)
        break
    else:
        continue

def moveDown(px, time=0.5):
    now = pag.position()
    pag.moveTo(now[0], now[1]+px, time)

def moveUp(px, time=0.5):
    now = pag.position()
    pag.moveTo(now[0], now[1]-px, time)

def moveRight(px, time=0.5):
    now = pag.position()
    pag.moveTo(now[0]+px, now[1], time)

def moveLeft(px, time=0.2):
    now = pag.position()
    pag.moveTo(now[0]-px, now[2], time)

def dragLeft(px, time=0.5):
    now = pag.position()
    pag.dragTo(now[0]-px, now[1], time, button='left')

def dragUp(px, time=0.5):
    now = pag.position()
    pag.dragTo(now[0], now[1]-px, time, button='left')

pyperclip.copy(yourMessage)

for i in range(howMany):
    pag.click()
    time.sleep(1.5)
    pag.hotkey('ctrl', 'v')
    time.sleep(0.3)
    pag.press('enter')
    time.sleep(0.3)
    postBeforeDrag = pag.position()
    dragLeft(300, time=0.5)
    pag.moveTo(postBeforeDrag[0], postBeforeDrag[1])
    time.sleep(1)
    time.sleep(2)
    postBeforeDrag = pag.position()
    dragUp(150, time=0.5)
    pag.moveTo(postBeforeDrag[0], postBeforeDrag[1])

def doRefresh():
    moveUp(45, 0.2)
    moveLeft(280, 0.2)
    pag.click()
    moveRight(250, 0.2)
    pag.click()
