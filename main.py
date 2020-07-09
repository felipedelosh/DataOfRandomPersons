"""
Felipedelosh 7/5/2020

Genererate a data persons

07 09 2020 > Try to open .txt files
07 09 2020 > Create Generate person
"""

from tkinter import *
import random
import os
from datetime import date

class Software:
    def __init__(self):
        #Views
        self.screen = Tk()
        self.canvas = Canvas(self.screen, width=640, height=480, bg="snow")
        self.btnGeneratePerson = Button(self.canvas, text="Generate Person", command=self.generatePerson)
        #Values
        self.data = ""
        self.ID = 0
        self.firtName = ""
        self.secondName = ""
        self.lastName = ""
        self.sex = 0
        self.birdDateDD = 0
        self.birdDateMM = 0
        self.birdDateYY = 0
        self.phone = 0

        # Charge dbinfo
        self.dir = os.path.dirname(os.path.abspath(__file__))
        self.dbLastName = None
        self.dbNameMale = None
        self.dbNameFemale = None
        self.controlInfoUpload = False
        self.chargeInfoDB()
        

        #I want to see the window
        self.initView()

    def chargeInfoDB(self):
        # Try to open fist name of men
        try:
            f = open(self.dir+"\data\dbNAMEMALE.txt", 'r', encoding="UTF-8")
            self.dbNameMale = f.read()
            self.dbNameMale = self.dbNameMale.strip()
            self.dbNameMale = self.dbNameMale.split('\n')
            self.controlInfoUpload = True
            f.close()
            f = None
        except:
            self.controlInfoUpload = False
            print('Error in male names')


        # Try to open first name of women
        try:
            f = open(self.dir+"\data\dbNAMEFEMALE.txt", "r", encoding="UTF-8")
            self.dbNameFemale = f.read()
            self.dbNameFemale = self.dbNameFemale.strip()
            self.dbNameFemale = self.dbNameFemale.split("\n")
            self.controlInfoUpload = self.controlInfoUpload and True
            
            f.close()
            f = None
            self.controlInfoUpload = self.controlInfoUpload and True
        except:
            self.controlInfoUpload = self.controlInfoUpload and False
            print('Error in female names')


        # Try to open lastnames
        try:
            f = open(self.dir+"\\data\\dbLASTNAME.txt", "r", encoding="UTF-8")
            self.dbLastName = f.read()
            self.dbLastName = self.dbLastName.strip()
            self.dbLastName = self.dbLastName.split("\n")
            f.close()
            self.controlInfoUpload = self.controlInfoUpload and True
        except:
            self.controlInfoUpload = self.controlInfoUpload and False
            print('Error in last names')


    def initView(self):
        self.screen.title("Persons by loko")
        self.screen.geometry("640x480")

        self.canvas.place(x=0, y=0)

        self.btnGeneratePerson.place(x=10, y=20)

        self.screen.mainloop()

    """
    Person : 
    ID
    Last names
    Firt name
    Second name
    sex
    birth date
    Tel
    """
    def generatePerson(self):
        # sex
        self.sex = random.randint(0,1)

        # Age
        age = random.randint(0, 100)
        today = str(date.today())

        self.birdDateMM = random.randint(1, 12)

        # Days if feb
        # Some people programe MM ends to 30 and 31
        # No time for it
        if self.birdDateMM == 2:
            self.birdDateDD = random.randint(1, 28)
        else:
            self.birdDateDD = random.randint(1, 30)

        # Year
        # i need to cacth year and YY - age to put in birth date

        print(self.birdDateDD, self.birdDateMM)





        # Generate last names
        # Somepersons hast 1 last name
        if(random.randint(0,9)<2):
            self.lastName = str(self.dbLastName[random.randint(0,len(self.dbLastName)-1)])
        else:
            self.lastName = str(self.dbLastName[random.randint(0,len(self.dbLastName)-1)]) + " " + str(self.dbLastName[random.randint(0,len(self.dbLastName)-1)])



#Launch
s = Software()