"""
FelipedelosH
"""
import json

class Person(object):
    def __init__(self, id, sex, name, lastname, birthdate) -> None:
        self.id = id
        self.sex = sex
        self.name = name
        self.lastname = lastname
        self.birthdate = birthdate

    def getSQLInsert(self):
        """Return a SQL query to insert"""
        tablename = "_TABLENAME_"
        values = "name, lastname, sex, birthdate"
        insertvalues = f"'{self.name}', '{self.lastname}', '{self.sex}', '{self.birthdate}'"
        return f"insert into {tablename}({values}) values({insertvalues});"
    
    def getCSVdelimitatesToPipeline(self):
        """Return a x|y|z text"""
        return f"{self.name}|{self.lastname}|{self.sex}|{self.birthdate}"
    
    def getCSVdelimitatesToComma(self):
        """Return a x;y;z; text"""
        return f"{self.name};{self.lastname};{self.sex};{self.birthdate};"
    
    def getJson(self):
        """Return a Json model"""
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4, ensure_ascii=False)


    def __str__(self) -> str:
        return f"{self.id}: {self.name} {self.lastname}"
    