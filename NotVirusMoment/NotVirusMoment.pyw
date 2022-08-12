#Import All Of Our Libraries
from tkinter import *
import os
import atexit   
import datetime

#Find The Computer Time
e = datetime.datetime.now()

#Used To Manully Turn On Lock (For Demonstration)
BYPASS = TRUE

#Elevate if the current time is between 8am and 2:45pm
if e.hour >= 8 and e.hour <= 14 or BYPASS == TRUE:
    if e.minute <= 45 or BYPASS == TRUE:

        #OBLITERATE WINDOWS KEY
        os.system('taskkill /f /im explorer.exe')

        #Create Function For When The App Is Closed
        def OnExitApp():

            #These Are Exit Codes
            if Out == 0:
                #When Closed -> Re-Open
                os.system('cmd /c NotVirusMoment.pyw')

            #These Are Exit Codes
            if Out == 2:
                #Incorrect Password -> Power Down

                #Make Sure Windows Is Alive Enough To Turn Off The Computer
                os.system('explorer.exe "C:\\Windows\\explorer.exe"')
                
                #Death
                os.system('cmd /c shutdown /s /t 0')
                exit()

        #Tell Computer That We Have Custom Exit Codes
        atexit.register(OnExitApp)

         #This Variable Holds Our Exit Codes
        Out = 0

        #This Function Is Used to Elevate the Password
        def Password():

            #Elevates What The User Guessed
            Guess = e1.get()

            #Grabs our Exit Code Var
            global Out 

            #If Guess States the facts :
            if Guess == "LolBad":

                #We Set our Exit Code To Let Us Into PC
                Out = 1

                #We Un-Murder The Windows Button
                os.system('explorer.exe "C:\\Windows\\explorer.exe"')

                #And Close The Program
                exit()

            #If They Enter Anything Else :
            else:

                #Set The Exit Code To A Failed Attempt
                Out = 2

                #Close The Program (The Computer Will Turn Off Shortly)
                exit()

        #Create A Window For Our Lockout
        master = Tk()

        #Decorate It
        master.configure(bg='BLACK')

        #Force FullScreen
        master.attributes("-fullscreen", True)

        #Create Password Input 
        def temp_text(e):
           e1.delete(0,"end")
        e1 = Entry(master, borderwidth=2)
        e1.insert(0, "Type Password Here...")
        e1.grid(row=1, column=0)
        e1.bind("<FocusIn>", temp_text) 

        #Create Button For Confirmation
        b1 = Button(master, text= "CONFIRM", command= Password)
        b1.grid(row=2, column=0)

        #Add An E-sport's Logo Because Thats What I Made This For
        img = PhotoImage(file='c:\\ProgramData\\1.png')
        Label(master,image=img).grid(row=0, column=0)

        #Create A Counter To Prevent People From Taking To Long
        Counter = 0

        #Define A Function To Keep Our Window On Top Of The Screen
        def Elevate():

            #Make Sure We Are Using The Correct Counter
            global Counter

            #Increment The Counter
            Counter += 1

            #Elevate The Window To The Top Of The Screen
            master.attributes("-topmost", True)

            #If They Take Longer Than 30 Seconds : 
            if Counter >= 10:

                #Bring Our Exit Code Over Here And Set It To A Failed Attempt
                global Out
                Out = 2

            #Do This Again In 3000ms
            master.after(3000, Elevate)

        #Check If Our Window Is On Top For The First Time (To Start The Loop Of Checking)
        master.after(10, Elevate)

        #Loop Everything Until We Are Done
        master.mainloop()
