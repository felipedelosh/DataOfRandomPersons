"""
FelipedelosH
"""

class Person(object):
    def __init__(self, id, sex, name, lastname, birthdate) -> None:
        self.id = id
        self.sex = sex
        self.name = name
        self.lastname = lastname
        self.birthdate = birthdate

    def getSQLInsert(self):
        tablename = "_TABLENAME_"
        values = "name, lastname, sex, birthdate"
        insertvalues = f"'{self.name}', '{self.lastname}', '{self.sex}', '{self.birthdate}'"
        return f"insert into {tablename}({values}) values({insertvalues});"

    def __str__(self) -> str:
        return f"{self.id}: {self.name} {self.lastname}"
