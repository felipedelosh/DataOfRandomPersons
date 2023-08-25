"""
FelipedelosH

Genererate a sample data of people
"""
from PersonModel import Person
from tkinter import *
from tkinter import ttk
from datetime import date
from datetime import datetime
import random


class Software:
    def __init__(self):
        #Charge dataset
        self._lastNames = []
        self._namesWomen = []
        self._namesMen = []
        self._output = [] # Here save a person data
        self._openSampleData()
        #Views
        self.screen = Tk()
        self.canvas = Canvas(self.screen, width=640, height=480, bg="black")
        self.lblMainMessage = Label(self.canvas, bg="black", fg="red", text="To generate a data persons select atributes then the output file and press generate.")
        self.lblQtyPersons = Label(self.canvas, bg="black", fg="red", text="1 -> Insert number of data to generate:") 
        self.txtQtyPersons = Entry(self.canvas, bg="black", fg="red", width=10)
        self.lblSexPersons = Label(self.canvas, bg="black", fg="red", text="2 -> Select a sex to persons:")
        self._cmbxSex = StringVar()
        self.cmbxSex = ttk.Combobox(self.canvas, state='readonly', textvariable=self._cmbxSex)
        self.cmbxSex['values'] = ["MALE", "FEMALE", "RND"]
        self.cmbxSex.current(0)
        self.lblOutput = Label(self.canvas, bg="black", fg="red", text="3 -> Select a output type:")
        self._typeOfOutput = StringVar()
        self.cmbxtypeOfOutput = ttk.Combobox(self.canvas, state='readonly', textvariable=self._typeOfOutput)
        self.cmbxtypeOfOutput['values'] = ["SQLScript", "Excel", "Json", ".CSV"]
        self.cmbxtypeOfOutput.current(0)
        self.btnGenerateData = Button(self.canvas, bg="green", text="GENERATE", command=self.generateData)

        #show
        self.initView()

    def initView(self):
        self.screen.title("Fake data of People Generator")
        self.screen.geometry("640x300")
        self.canvas.place(x=0, y=0)

        self.lblMainMessage.place(x=80, y=20)
        self.canvas.create_line(20, 60, 620, 60, fill="red")
        self.lblQtyPersons.place(x=40, y=80)
        self.txtQtyPersons.place(x=250, y=80)
        self.lblSexPersons.place(x=60, y=120)
        self.cmbxSex.place(x=220, y=120)
        self.lblOutput.place(x=70, y=160)
        self.cmbxtypeOfOutput.place(x=220, y=160)

        self.btnGenerateData.place(x=260, y=250)


        self.screen.mainloop()


    def generateData(self):
        if self._validatesQty():
            self._output = [] # Reset
            # Generate data
            for i in range(1, int(self.txtQtyPersons.get())+1):
                if self._cmbxSex.get() == "RND":
                    _k = random.randint(0, 1)
                    if _k == 0:
                        self._generateMan()
                    else:
                        self._generateWoman()
                else:
                    if self._cmbxSex.get() == "MALE":
                        self._generateMan()

                    if self._cmbxSex.get() == "FEMALE":
                        self._generateWoman()
            # Save data
            self._saveData()
        else:
            self._outputWindow("Error", "Insert Valid Number")



    def _generateMan(self):
        """

        """
        id = len(self._output) + 1
        _name = self._namesMen[random.randint(0, len(self._namesMen)-1)]
        _lastname = self._lastNames[random.randint(0, len(self._lastNames)-1)] + " " + self._lastNames[random.randint(0, len(self._lastNames)-1)]
        
        _p = Person(id, "M", _name, _lastname, self._getBirthDate())
        self._output.append(_p)


    def _generateWoman(self):
        """
        
        """
        id = len(self._output) + 1
        _name = self._namesWomen[random.randint(0, len(self._namesWomen)-1)]
        _lastname = self._lastNames[random.randint(0, len(self._lastNames)-1)] + " " + self._lastNames[random.randint(0, len(self._lastNames)-1)]

        _p = Person(id, "F", _name, _lastname, self._getBirthDate())
        self._output.append(_p)


    def _getBirthDate(self):
        """
        Return a rnd date in str: YYYY-MM-DD
        """
        _now = date.today()
        _now = str(_now).split("-")
        _YYYY = int(_now[0])
        _MM = int(_now[1])
        _DD = int(_now[2])
        _age = random.randint(0, 99)
        _age = 0
        _person_birth_YYYY_date = 0
        _person_birth_MM_date = 0
        _person_birth_DD_date = 0

        if _age == 0:
            _person_birth_YYYY_date = _YYYY
            if _MM == 1:
                _person_birth_MM_date = 1
                if _DD == 1:
                    _person_birth_DD_date = 1
                else:
                    _person_birth_DD_date = 0
            else:
                _person_birth_MM_date = random.randint(1, _MM-1)
                if _person_birth_MM_date == 2:
                    _person_birth_DD_date = random.randint(1, 29)
                elif _person_birth_MM_date == 4 or _person_birth_MM_date == 6 or _person_birth_MM_date == 9 or _person_birth_MM_date == 11:
                    _person_birth_DD_date = random.randint(1, 31)
                else:
                    _person_birth_DD_date = random.randint(1, 32)
        else:
            _person_birth_YYYY_date = _YYYY - _age # Get year
            _person_birth_MM_date = random.randint(1, 13)
            if _person_birth_MM_date == 2:
                _person_birth_DD_date = random.randint(1, 29)
            elif _person_birth_MM_date == 4 or _person_birth_MM_date == 6 or _person_birth_MM_date == 9 or _person_birth_MM_date == 11:
                _person_birth_DD_date = random.randint(1, 31)
            else:
                _person_birth_DD_date = random.randint(1, 32)

        _pBirthDate = f"{_person_birth_YYYY_date}-{_person_birth_MM_date}-{_person_birth_DD_date}"

        return _pBirthDate


    def _validatesQty(self):
        try:
            return int(self.txtQtyPersons.get()) > 0
        except:
            return False
        

    def _openSampleData(self):
        try:
            with open("dataset\dbLASTNAME.txt", "r", encoding="UTF-8") as f:
                for i in f.read().split("\n"):
                    self._lastNames.append(i)

            with open("dataset\dbNAMEFEMALE.txt", "r", encoding="UTF-8") as f:
                for i in f.read().split("\n"):
                    self._namesWomen.append(i)


            with open("dataset\dbNAMEMALE.txt", "r", encoding="UTF-8") as f:
                for i in f.read().split("\n"):
                    self._namesMen.append(i)

        except:
            self._outputWindow("Error", "NOT FIND SAMPLE DATA")

    def _saveData(self):
        if self._typeOfOutput.get() == "SQLScript":
            self._saveSQL()
        elif self._typeOfOutput.get() == "Excel":
            self._saveEXCEL()
        elif self._typeOfOutput.get() == "Json":
            self._saveJSON()
        elif self._typeOfOutput.get() == ".CSV":
            self._saveCSV()

    def _saveSQL(self):
        _filedata = ""
        for i in self._output:
            _filedata = _filedata + i.getSQLInsert() + "\n"

        with open("output\sql.sql", "w", encoding="UTF-8") as f:
            f.write(_filedata)

    def _saveEXCEL(self):
        _filedata = ""
        for i in self._output:
            _filedata = _filedata + i.getCSVdelimitatesToPipeline() + "\n"

        with open("output\excel.xlsx", "w", encoding="UTF-8") as f:
            f.write(_filedata)  

    def _saveJSON(self):
        _filedata = ""
        output = ""
        for i in self._output:
            _filedata = _filedata + i.getJson() + ","

        # erase last comma
        _filedata = _filedata[:-1]

        _metadata = "\"metadata\": " + "{\n\t\"version\":\"1.0\",\n\t\"timestamp\":\"" + str(date.today()) + "\",\n\t\"author\":\"felipedelosh\",\n\t\"length\":" + str(len(self._output)) +  "\n}"
        output = "{\n" + "\"data\":[" + _filedata + "],\n" + _metadata +"\n}"

        with open("output\json.json", "w", encoding="UTF-8") as f:
            f.write(output)  

    def _saveCSV(self):
        _filedata = ""
        for i in self._output:
            _filedata = _filedata + i.getCSVdelimitatesToComma() + "\n"

        with open("output\csv.csv", "w", encoding="UTF-8") as f:
            f.write(_filedata)  


    def _outputWindow(self, title, text):
        top = Toplevel()
        top.title(title)
        top.geometry("500x300")
        canvas = Canvas(top, height=300, width=500, bg="black")
        canvas.place(x=0, y=0)
        msg = Text(canvas, width=55, height=13, bg="black", fg="red")
        msg.insert(END, text)
        msg.place(x=25, y=20)
        button = Button(canvas, text="Aceptar", bg="green", command=top.destroy)
        button.place(x=222, y=260)


#Launch
s = Software()
