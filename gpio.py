# GPIO Sample Code

import Tkinter as tk
import RPi.GPIO as GPIO
import threading

from time import sleep
from random import seed
from random import randint

GPIO21 = 21
GPIO20 = 20
GPIO16 = 16
GPIO12 = 12

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(GPIO21, GPIO.OUT)                          # BLUE
GPIO.setup(GPIO20, GPIO.OUT)                          # RED
GPIO.setup(GPIO16, GPIO.OUT)                          # BUZZER
GPIO.setup(GPIO12, GPIO.IN, pull_up_down=GPIO.PUD_UP) # BUTTON

master = tk.Tk()
master.title("GPIO Control")
# master.geometry("500x200")

GPIO21_State = True
GPIO20_State = True
GPIO16_State = False

def OnBlueButton():
	global GPIO21_State
	if GPIO21_State == True:
		GPIO21_State = False
		GPIO.output(GPIO21, GPIO21_State)
	else:
		GPIO21_State = True
		GPIO.output(GPIO21, GPIO21_State)


def OnRedButton():
	global GPIO20_State
	if GPIO20_State == True:
		GPIO20_State = False
		GPIO.output(GPIO20, GPIO20_State)
	else:
		GPIO20_State = True
		GPIO.output(GPIO20, GPIO20_State)

def OnBuzzerButton():
	global GPIO16_State
	if GPIO16_State == True:
		GPIO.output(GPIO16, GPIO16_State)
		GPIO16_State = False
	else:
		GPIO.output(GPIO16, GPIO16_State)
		GPIO16_State = True

def OnStartButton():
	run.set()

def OnStopButton():
	run.clear()
	
def DoBackgroundTask():
	seed(1)
	while loop.isSet():
		sleep(0.1)
		if ((GPIO.input(GPIO12) == True) & (not GPIO16_State)):
			GPIO.output(GPIO16, False)
		else:
			GPIO.output(GPIO16, True)
			
		while run.isSet():
			GPIO.output(GPIO20, False)
			GPIO.output(GPIO21, True)
			GPIO.output(GPIO16, True)
			sleep(0.05)
			GPIO.output(GPIO20, True)
			GPIO.output(GPIO21, False)
			GPIO.output(GPIO16, False)
			sleep(0.05)

def OnExitButton():
	GPIO.output(GPIO20, False)
	GPIO.output(GPIO21, False)
	GPIO.output(GPIO16, False)
	loop.clear()
	master.destroy()	

BlueLEDButton = tk.Button(master, text="Blue", bg="blue", width=25, justify="left", command=OnBlueButton)
BlueLEDButton.grid(row=0, column=0)

RedLEDButton = tk.Button(master, text="Red",bg="red", width=25, justify="left" , command=OnRedButton)
RedLEDButton.grid(row=1, column=0)

BuzzerButton = tk.Button(master, text="Buzzer",bg="yellow", width=25, justify="left" , command=OnBuzzerButton)
BuzzerButton.grid(row=2, column=0)

StartButton = tk.Button(master, text="Start",bg="green", width=25, justify="left" , command=OnStartButton)
StartButton.grid(row=3, column=0)

StopButton = tk.Button(master, text="Stop",bg="red", width=25, justify="left" , command=OnStopButton)
StopButton.grid(row=4, column=0)

ExitButton = tk.Button(master, text="Exit",bg="white", width=25, justify="left", command=OnExitButton)
ExitButton.grid(row=5, column=0)

GPIO.output(GPIO20, GPIO20_State)
GPIO.output(GPIO21, GPIO21_State)
GPIO.output(GPIO16, GPIO16_State)

BackgroundTask = threading.Thread(target=DoBackgroundTask)

run = threading.Event()
run.clear()
loop = threading.Event()
loop.set()

BackgroundTask.start()

master.mainloop()


