from tkinter import *
import tkinter.font
import Rpi.GPIO
Rpi.GPIO.setmode(RPi.GPIO.BCM)

## hardware 


## GUI definitions
win = Tk()
win.title("Febris Action Main Menu")
win.geometry("1920x1080")
myFont = tkinter.font.Font(family = "Times", size = 12, weight = bold)
frame = tkinter.Frame(win, bg='baige') 
ReceivedData = tkinter.Label(frame, text = lineox, bg = white, font = myfont, height = 2, width = 20) ## delete later

## Event Functions Conditions
bpOn = [0, 1]
bpOn = 0
bpmOn = [0, 1]
bpmOn = 0
oxOn = [0, 1]
oxOn = 0
thmOn = [0, 1]
thmOn = 0

## Event Functions
def close():            ## closes window
  RPi.GPIO.cleanup()
  win.destroy

def bpExec():           ## tells arduino to run the blood pressure machine
  print ("Blood Pressure Machine Hold-In-Place") ## delete this later if following code doesn't work
  label = tk.Label(text="Measuring Blood Pressure", foreground = 'dark gray', background = 'white', font = myFont)
  bpOn == 1  

def bpmExec():          ## tells arduino to run the ecg
  print ("Blood Pulse Hold-In-Place")
  label = tk.Label(text="Measuring Blood Rate", foreground = 'dark gray', background = 'white', font = myFont)
  hrOn == 1

def oxExec():           ## tells arduino to run the oximeter
  print ("Oxygen Hold-In-Place") 
  label = tk.Label(text="Measuring Blood Oxygen Level", foreground = 'dark gray', background = 'white', font = myFont)
  oxOn == 1 

def thmExec():          ## tells arduino to run the thermometer
  print ("Temperarture Hold-In-Place")
  label = tk.Label(text="Measuring Temperature", foreground = 'dark gray', background = 'white', font = myFont)
  thmOn == 1 

## Widgets
bpButton = Button(frame, text = 'Check Blood Pressure', font = myFont, command = bpExec, bg = 'green')
bpButton.grid(row=0,column=1)

hrButton = Button(frame, text = 'Check Blood', font = myFont, command = hrExec, bg = 'green')
hrButton.grid(row=0,column=2)

oxButton = Button(frame, text = 'Check Blood Oxygen Level', font = myFont, command = oxExec, bg = 'green')
oxButton.grid(row=1,column=1)

thmButton = Button(frame, text = 'Check Temperature', font = myFont, command = thmExec, bg = 'green')
thmButton.grid(row=1,column=2)
 
exitButton = Button(frame, text = 'Power Off', font = myFont, command = close, bg = 'red')
exitButton.grid(row=2,column=1)

win.protocal("WM_Delete_Window", close) 
win.mainloop()

## Arduino Communication
#!/usr/bin/env python3
import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
read_serial = ser.readline()
ser.flushInput() ## clears the serial input to make sure its clean to read and send new info later  
ser.flushOutput()
if bpOn == 1: 
    ser.write ("#")
    linebp = ser.readline() ## linebp is reffering the line that comes from this option being chosen, in this case being blood pressure
    tkinter.Label(frame, text = linebp, bg = white, font = myfont, height = 2, width = 20)
if hrOn == 1:
    ser.write ("!")
    linehr = ser.readline()
    tkinter.Label(frame, text = linehr, bg = white, font = myfont, height = 2, width = 20)
if oxOn == 1:
    ser.write ("&")
    lineox = ser.readline()
    tkinter.Label(frame, text = lineox, bg = white, font = myfont, height = 2, width = 20)
if thmOn == 1: 
    ser.write ("$")
    linethm = ser.readline()
    tkinter.Label(frame, text = linethm, bg = white, font = myfont, height = 2, width = 20)



## Process Arduino information
import numpy
