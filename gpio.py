# GPIO Sample Code

import Tkinter as tk
import RPi.GPIO as GPIO
from time import sleep
import threading

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
master.geometry("500x200")

GPIO21_State = True
GPIO20_State = True
GPIO16_State = False

def GPIO21button():
	global GPIO21_State
	if GPIO21_State == True:
		GPIO21_State = False
		GPIO.output(GPIO21, GPIO21_State)
		ONlabel = tk.Label(master, text="Turned OFF", fg="green")
		ONlabel.grid(row=0, column=1)
	else:
		GPIO21_State = True
		GPIO.output(GPIO21, GPIO21_State)
		ONlabel = tk.Label(master, text="Turned ON", fg="red")
		ONlabel.grid(row=0, column=1)


def GPIO20button():
	global GPIO20_State
	if GPIO20_State == True:
		GPIO20_State = False
		GPIO.output(GPIO20, GPIO20_State)
		OFFlabel = tk.Label(master, text="Turned OFF", fg="green")
		OFFlabel.grid(row=1, column=1)
	else:
		GPIO20_State = True
		GPIO.output(GPIO20, GPIO20_State)
		OFFlabel = tk.Label(master, text="Turned ON", fg="red")
		OFFlabel.grid(row=1, column=1)

def GPIO16button():
	global GPIO16_State
	if GPIO16_State == True:
		GPIO.output(GPIO16, GPIO16_State)
		GPIO16_State = False
		OFFlabel = tk.Label(master, text="Buzzer OFF", fg="green")
		OFFlabel.grid(row=2, column=1)
	else:
		GPIO.output(GPIO16, GPIO16_State)
		GPIO16_State = True
		OFFlabel = tk.Label(master, text="Buzzer ON", fg="red")
		OFFlabel.grid(row=2, column=1)

def Start():
	run.set()

def Stop():
	run.clear()
	
def Run():
	while loop.isSet():
		if ((GPIO.input(GPIO12) == True) & (not GPIO16_State)):
			GPIO.output(GPIO16, False)
		else:
			GPIO.output(GPIO16, True)
			
		while run.isSet():
			GPIO.output(GPIO20, False)
			GPIO.output(GPIO21, True)
			GPIO.output(GPIO16, True)
			sleep(0.2)		
			GPIO.output(GPIO20, True)
			GPIO.output(GPIO21, False)
			GPIO.output(GPIO16, False)
			sleep(0.1)

def Exit():
	GPIO.output(GPIO20, False)
	GPIO.output(GPIO21, False)
	GPIO.output(GPIO16, False)
	loop.clear()
	master.destroy()	

BlueLEDbutton = tk.Button(master, text="Blue", bg="blue", width=10, justify="left", command=GPIO21button)
BlueLEDbutton.grid(row=0, column=0)

RedLEDbutton = tk.Button(master, text="Red",bg="red", width=10, justify="left" , command=GPIO20button)
RedLEDbutton.grid(row=1, column=0)

Buzzerbutton = tk.Button(master, text="Buzzer",bg="yellow", width=10, justify="left" , command=GPIO16button)
Buzzerbutton.grid(row=2, column=0)

Startbutton = tk.Button(master, text="Start",bg="green", width=10, justify="left" , command=Start)
Startbutton.grid(row=3, column=0)

Stopbutton = tk.Button(master, text="Stop",bg="red", width=10, justify="left" , command=Stop)
Stopbutton.grid(row=4, column=0)

Exitbutton = tk.Button(master, text="Exit",bg="white", width=10, justify="left", command=Exit)
Exitbutton.grid(row=5, column=0)

GPIO.output(GPIO20, GPIO20_State)
GPIO.output(GPIO21, GPIO21_State)
GPIO.output(GPIO16, GPIO16_State)

x = threading.Thread(target=Run)

run = threading.Event()
run.clear()
loop = threading.Event()
loop.set()

x.start()

master.mainloop()


