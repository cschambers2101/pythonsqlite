class Person:
    def __init__(self, firstname, surname, age) -> None:
        self.firstName = firstname
        self.surname = surname
        self.age = age

    def __str__(self) -> str:
        return f'{self.firstname} {self.surname}'