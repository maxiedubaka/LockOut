MaxieLogger = True
#Import All Of Our Libraries
if MaxieLogger == True:
    print("[MaxieLogger] : Import All Of Our Libraries")
from glob import glob
from tkinter import *
import os
import atexit   
import datetime

#Find The Computer Time
if MaxieLogger == True:
    print("[MaxieLogger] : Find The Computer Time")
e = datetime.datetime.now()

#Used To Manully Turn On Lock (For Demonstration)
if MaxieLogger == True:
    print("[MaxieLogger] : Used To Manully Turn On Lock (For Demonstration)")
BYPASS = TRUE

#Elevate if the current time is between 8am and 2:45pm
if MaxieLogger == True:
    print("[MaxieLogger] : Elevate if the current time is between 8am and 2:45pm")
if e.hour >= 8 and e.hour <= 14 or BYPASS == TRUE:
    if e.minute <= 45 or BYPASS == TRUE:

        #Ensure The Windows Key Is Real
        if MaxieLogger == True:
            print("[MaxieLogger] : Ensure The Windows Key Is Real")
        os.system('explorer.exe "C:\\Windows\\explorer.exe"')

        #OBLITERATE THAT FUCKIN WINDOWS KEY
        if MaxieLogger == True:
            print("[MaxieLogger] : OBLITERATE THAT FUCKIN WINDOWS KEY")
        os.system('taskkill /f /im explorer.exe')


        #This Variable Holds Our Exit Codes
        if MaxieLogger == True:
            print("[MaxieLogger] : This Variable Holds Our Exit Codes")
        Out = 0

        #Create Function For When The App Is Closed
        if MaxieLogger == True:
            print("[MaxieLogger] : Create Function For When The App Is Closed")
        def OnExitApp():

            #Make Sure We Are Using The Correct Exit Codes
            if MaxieLogger == True:
                print("[MaxieLogger] : Make Sure We Are Using The Correct Exit Codes")
            global Out

            #These Are Exit Codes
            if MaxieLogger == True:
                print("[MaxieLogger] : These Are Exit Codes")
            if Out == 0:
                #When Closed -> Re-Open
                if MaxieLogger == True:
                    print("[MaxieLogger] : When Closed -> Re-Open")
                os.system('cmd /c NotVirusMoment.pyw')

            #These Are Exit Codes 2
            if MaxieLogger == True:
                print("[MaxieLogger] : These Are Exit Codes 2")
            if Out == 2:
                #Incorrect Password -> Power Down
                if MaxieLogger == True:
                    print("[MaxieLogger] : Incorrect Password -> Power Down")

                #Make Sure Windows Is Alive Enough To Turn Off The Computer
                if MaxieLogger == True:
                    print("[MaxieLogger] : Make Sure Windows Is Alive Enough To Turn Off The Computer")
                os.system('explorer.exe "C:\\Windows\\explorer.exe"')

                #Death
                if MaxieLogger == True:
                    print("[MaxieLogger] : Death")
                os.system('cmd /c shutdown /s /t 0')

                #Reset Exit Code First For Saftey 
                if MaxieLogger == True:
                    print("[MaxieLogger] : Reset Exit Code First For Saftey ")
                Out = 0

                #Close Program
                if MaxieLogger == True:
                    print("[MaxieLogger] : Close Program")
                exit()

        #Tell Computer That We Have Custom Exit Codes
        if MaxieLogger == True:
            print("[MaxieLogger] : Tell Computer That We Have Custom Exit Codes")
        atexit.register(OnExitApp)

        #This Function Is Used to Elevate the Password
        if MaxieLogger == True:
            print("[MaxieLogger] : This Function Is Used to Elevate the Password")
        def Password():

            #Elevates What The User Guessed
            if MaxieLogger == True:
                print("[MaxieLogger] : Elevates What The User Guessed")
            Guess = e1.get()

            #Grabs our Exit Code Var
            if MaxieLogger == True:
                print("[MaxieLogger] : Grabs our Exit Code Var")
            global Out 

            #If Guess States the facts :
            if MaxieLogger == True:
                print("[MaxieLogger] : If Guess States the facts :")
            if Guess == "LolBad":

                #We Set our Exit Code To Let Us Into PC
                if MaxieLogger == True:
                    print("[MaxieLogger] : We Set our Exit Code To Let Us Into PC")
                Out = 1

                #We Un-Murder The Windows Button
                if MaxieLogger == True:
                    print("[MaxieLogger] : We Un-Murder The Windows Button")
                os.system('explorer.exe "C:\\Windows\\explorer.exe"')

                #And Close The Program
                if MaxieLogger == True:
                    print("[MaxieLogger] : And Close The Program")
                exit()

            #If They Enter Anything Else :
            
            else:
                if MaxieLogger == True:
                    print("[MaxieLogger] : If They Enter Anything Else :")
                #Set The Exit Code To A Failed Attempt
                if MaxieLogger == True:
                    print("[MaxieLogger] : Set The Exit Code To A Failed Attempt")
                Out = 2

                #Close The Program (The Computer Will Turn Off Shortly)
                if MaxieLogger == True:
                    print("[MaxieLogger] : Close The Program (The Computer Will Turn Off Shortly)")
                exit()

        #Create A Window For Our Lockout
        if MaxieLogger == True:
            print("[MaxieLogger] : Create A Window For Our Lockout")
        master = Tk()
        #Decorate It
        if MaxieLogger == True:
            print("[MaxieLogger] : Decorate It")
        master.configure(bg='BLACK')

        #Force FullScreen
        if MaxieLogger == True:
            print("[MaxieLogger] : Force FullScreen")
        master.attributes("-fullscreen", True)

        #Disable alt + F4
        if MaxieLogger == True:
            print("[MaxieLogger] : Disable alt + F4")

        #Kill Them If They Dare Press Alt
        def MURDER(e):
            os.system('cmd /c shutdown /s /t 0')

        #Killer Queen Has Already Touched Both Alt Keys
        master.bind('<Alt_L>', MURDER)
        master.bind('<Alt_R>', MURDER)
        
        #Create Password Input 
        if MaxieLogger == True:
            print("[MaxieLogger] : Create Password Input ")
        def temp_text(e):
           e1.delete(0,"end")
        e1 = Entry(master)
        e1.insert(0, "Type Password Here...")
        e1.grid(row=1, column=0)
        e1.bind("<FocusIn>", temp_text) 

        #Create Button For Confirmation
        if MaxieLogger == True:
            print("[MaxieLogger] : Create Button For Confirmation")
        b1 = Button(master, text= "CONFIRM", command= Password)
        b1.grid(row=2, column=0)

        #Add An E-sport's Logo Because Thats What I Made This For
        if MaxieLogger == True:
            print("[MaxieLogger] : Add An E-sport's Logo Because Thats What I Made This For")
        img = PhotoImage(file='c:\\ProgramData\\1.png')
        Label(master,image=img).grid(row=0, column=0)

        #Create A Counter To Prevent People From Taking To Long
        if MaxieLogger == True:
            print("[MaxieLogger] : Create A Counter To Prevent People From Taking To Long")
        Counter = 0

        #Define A Function To Keep Our Window On Top Of The Screen
        if MaxieLogger == True:
            print("[MaxieLogger] : Define A Function To Keep Our Window On Top Of The Screen")
        def Elevate():

            #Make Sure We Are Using The Correct Counter
            if MaxieLogger == True:
                print("[MaxieLogger] : Make Sure We Are Using The Correct Counter")
            global Counter

            #Increment The Counter
            if MaxieLogger == True:
                print("[MaxieLogger] : Increment The Counter")
            Counter += 1

            #Elevate The Window To The Top Of The Screen
            if MaxieLogger == True:
                print("[MaxieLogger] : Elevate The Window To The Top Of The Screen")
            master.attributes("-topmost", True)

            #If They Take Longer Than 1 Minute : 
            if MaxieLogger == True:
                print("[MaxieLogger] : If They Take Longer Than 30 Seconds : ")
            if Counter >= 20:

                #Bring Our Exit Code Over Here And Set It To A Failed Attempt
                if MaxieLogger == True:
                    print("[MaxieLogger] : Bring Our Exit Code Over Here And Set It To A Failed Attempt")
                global Out
                Out = 2
                exit()

            #Do This Again In 3000ms
            if MaxieLogger == True:
                print("[MaxieLogger] : Do This Again In 3000ms")
            master.after(3000, Elevate)

        #Check If Our Window Is On Top For The First Time (To Start The Loop Of Checking)
        if MaxieLogger == True:
            print("[MaxieLogger] : Check If Our Window Is On Top For The First Time (To Start The Loop Of Checking)")
        master.after(10, Elevate)

        #Loop Everything Until We Are Done
        if MaxieLogger == True:
            print("[MaxieLogger] : Loop Everything Until We Are Done")
        master.mainloop()