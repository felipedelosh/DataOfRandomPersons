"""
FelipedelosH
"""

class Person(object):
    def __init__(self, id, sex, name, lastname) -> None:
        self.id = id
        self.sex = sex
        self.name = name
        self.lastname = lastname

    def __str__(self) -> str:
        return f"{self.id}: {self.name} {self.lastname}"
