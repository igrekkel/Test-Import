# GPIO Sample Code

import Tkinter as tk
import RPi.GPIO as GPIO
from time import sleep
import threading
import sys

GPIO21 = 21
GPIO20 = 20
GPIO16 = 16
GPIO12 = 12

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(GPIO21, GPIO.OUT)
GPIO.setup(GPIO20, GPIO.OUT)
GPIO.setup(GPIO16, GPIO.OUT)
GPIO.setup(GPIO12, GPIO.IN, pull_up_down=GPIO.PUD_UP)

master = tk.Tk()
master.title("GPIO Control")
master.geometry("500x200")

GPIO21_state = True
GPIO20_State = True
GPIO16_State = False

def GPIO21button():
	global GPIO21_state
	if GPIO21_state == True:
		GPIO.output(GPIO21, GPIO21_state)
		GPIO21_state = False
		ONlabel = tk.Label(master, text="Turned ON", fg="green")
		ONlabel.grid(row=0, column=1)
	else:
		GPIO.output(GPIO21, GPIO21_state)
		GPIO21_state = True
		ONlabel = tk.Label(master, text="Turned OFF", fg="red")
		ONlabel.grid(row=0, column=1)


def GPIO20button():
	global GPIO20_State
	if GPIO20_State == True:
		GPIO.output(GPIO20, GPIO20_State)
		GPIO20_State = False
		OFFlabel = tk.Label(master, text="Turned ON", fg="green")
		OFFlabel.grid(row=1, column=1)
	else:
		GPIO.output(GPIO20, GPIO20_State)
		GPIO20_State = True
		OFFlabel = tk.Label(master, text="Turned OFF", fg="red")
		OFFlabel.grid(row=1, column=1)

def GPIO16button():
	global GPIO16_State
	if GPIO16_State == True:
		GPIO.output(GPIO16, GPIO16_State)
		GPIO16_State = False
		OFFlabel = tk.Label(master, text="Buzzer ON", fg="green")
		OFFlabel.grid(row=2, column=1)
	else:
		GPIO.output(GPIO16, GPIO16_State)
		GPIO16_State = True
		OFFlabel = tk.Label(master, text="Buzzer OFF", fg="red")
		OFFlabel.grid(row=2, column=1)


def Start():
	e.set()

def Stop():
	e.clear()
	
def Run():
	while (1):
		if (GPIO16_State == True):	
			if (GPIO.input(GPIO12) == True):
				GPIO.output(GPIO16, 0)
			else:
				GPIO.output(GPIO16, 1)
			
		while e.isSet():
			GPIO.output(GPIO20, 0)
			GPIO.output(GPIO21, 1)
			GPIO.output(GPIO16, 1)
			sleep(0.1)		
			GPIO.output(GPIO20, 1)
			GPIO.output(GPIO21, 0)
			GPIO.output(GPIO16, 0)
			sleep(0.1)

def Exit():
	GPIO.cleanup()
	master.quit()
	master.destroy()	
	sys.exit()

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

x = threading.Thread(target=Run)

e = threading.Event()

x.start()

master.mainloop()

