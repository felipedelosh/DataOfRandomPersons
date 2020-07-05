"""
Felipedelosh 7/5/2020

Genererate a data persons
"""

from tkinter import *
import random
import os

class Software:
    def __init__(self):
        #Views
        self.screen = Tk()
        self.canvas = Canvas(self.screen, width=640, height=480, bg="snow")
        #Values
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
            f = open(self.dir+"\data\dbNAMEMALE.txt", 'r')
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
            f = open(self.dir+"\data\dbNAMEFEMALE.txt", "r")
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
            # Error i'm only read 2 .txt?
            f = open(self.dir+"\data\dbLASTNAME.txt", "r")
            
        
            self.controlInfoUpload = self.controlInfoUpload and True
        except:
            self.controlInfoUpload = self.controlInfoUpload and False
            print('Error in last names')


    def initView(self):
        self.screen.title("Persons by loko")
        self.screen.geometry("640x480")

        self.canvas.place(x=0, y=0)



        self.screen.mainloop()


#Launch
s = Software()