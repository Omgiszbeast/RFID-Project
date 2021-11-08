#This program is designed to display information from a sql data base and set a "classroom" with students
#The program is specifically designed for the RFID scanner used in software engineering fall 2021
#JohnPaul Flores is the sole author of this code as of 10/21/21
#Software Engineering
#JohnPaul Flores CID: 81340848
#Last Edited: Date 10/21/21

##
# To use the "generic" widgets
import tkinter as tk
# To use the stylized, "look-and-feel" widgets
from tkinter import ttk
# To display any error or warnings for mistakes, and to make sure the user wants to enter the info
from tkinter import messagebox
# sublibrary to ask for any info the program needs from the user 
from tkinter import simpledialog
# sublibrary to 

#Imports a function to give you the list from a RFID Tag
from dataBaseCode import returnsKeyIDPeopleTableFromRFIDTag

TrueUser = False
TruePassword = False
CurrentFailedAttempt = False
hasBeenCreated = False
recentClassSize = 0
seats = {}


def main():
    RecentClassSize = 0
    #creating program
    program = RFIDDisplay()
    #starting event loop
    program.window.mainloop()

class RFIDDisplay:

    def __init__(self):
        #Making the application window
        self.window = tk.Tk()
        self.create_widgets()
        
    
    #isAdmin sends what the user input for logging in. This will be the log in page for the UI and
    #if the username and password are correct then it will provide access to the classroom state and 
    #modifying priveliges to the classroom as well
    def isAdmin(self, event, accounts):
        #taking data entered into the entry and chcecking it for authentification
        enteredName = self.my_entry.get()
        
        #if whatever information is true then 
        for users in accounts:
            if users == enteredName:
                return True
        return False





    #validPassword takes what the user entered into the passwd box and sees if the password 
    #and username match the ones in the data base
    def validLogin (self, event):
        passwd = self.password_entry.get()
        user = self.name_entry.get()
        
        #a variable that is present to check if the username is registered in the data base
        
        if passwd == "Hello":
            TruePassword = True
        else:
            TruePassword = False
            
        if user == "GoodBye":
            TrueUser = True
        else:
            TrueUser = False
        
        if TrueUser == False or TruePassword == False:
            self.display = ttk.Label(self.window, text="Invalid Login LOL")
            self.display.grid(row=4, column=0, sticky=tk.W, pady=5)
            CurrentFailedAttempt = True
        else:
            self.show_admin_powers()
            self.login_button.destroy()
            
    def show_admin_powers(self):
        if CurrentFailedAttempt == True:
            self.display.delete(0, END)
            
        self.classroom = ttk.Entry(self.window, width=100)
        self.classroom.grid(row=4, column=0, sticky=tk.W, pady=5)
        self.classroom.insert(tk.END, "Enter the class size you want (Perfect Square)")
        self.classroom.bind("<Return>", self.create_class)
        
    #Create class is meant to make the classroom on the UI by making empty seats.
    def create_class(self, event):
        classSize = self.classroom.get()
        classSize = int(classSize)
        global seats
        global recentClassSize
        if recentClassSize != 0:
            for i in range(recentClassSize):
                for j in range(2, recentClassSize + 2):
                    seats[(i, j + 2)].destroy()
        #for i in range(RecentClassSize):
            #for j in range(2, RecentClassSize + 2):
                #self.b = ttk.Label(self.window, text="")
                #self.b.grid(row=i, column=j, pady=5)
            
        for i in range(classSize):
            for j in range(2, classSize + 2):
                b = ttk.Label(self.window, text="RFID COVID-19 Tracker")
                b.grid(row=i, column=j, pady=5)
                seats[(i, j + 2)] = b
        
        recentClassSize = classSize

        
                
        
    #(Comments written 10/21/21. This is only the outline of what the UI needs to do)
    #The UI needs to display the classroom and the positions of the users
    def create_widgets(self):
    #creating the user interface
        self.title = ttk.Label(self.window, text="RFID COVID-19 Tracker")
        self.title.grid(row=0, column=0)

        #setting up when the user can enter a username
        self.name_entry = ttk.Entry(self.window, width=100)
        self.name_entry.grid(row=1, column=0, sticky=tk.W, pady=5)
        #self.name_entry.insert(tk.END, "Enter User Name")
        self.name_entry.insert(tk.END, "GoodBye")
        self.name_entry.bind("<Return>", self.isAdmin)
        
        #setting up when the user can enter a password
        self.password_entry = ttk.Entry(self.window, width=100)
        self.password_entry.grid(row=2, column=0, sticky=tk.W, pady=5)
        #self.password_entry.insert(tk.END, "Enter Password")
        self.password_entry.insert(tk.END, "Hello")
        
        #creating a button to login to the application
        self.login_button = tk.Button(self.window, text="Log in")
        self.login_button.grid(row=3, column=0, sticky=tk.W, pady=5)
        self.login_button.bind("<Button>", self.validLogin)
        
        #making an entry to create a class
        if TrueUser == True and TruePassword == True:
            self.classroom = ttk.Entry(self.window, width=100)
            self.classroom.grid(row=4, column=0, sticky=tk.W, pady=5)
            self.classroom.insert(tk.END, "Enter the class size you want (Perfect Square)")
            self.classroom.bind("<Return>", self.create_class)
            RecentClassSize = self.classroom.get()
            
        #creating a label for most recent log in
        self.recentTag = ttk.Label(self.window, text="This is the most Recent login")
        self.recentTag.grid(row=5, column=0,sticky=tk.W, pady=20)
        
        #The Following code is for the display of seats. The seats are represented by brackets and can be empty
        
if __name__ == "__main__":
    main()