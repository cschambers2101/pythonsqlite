class Person:
    def __init__(self, firstname, surname, age) -> None:
        self.first_name = firstname
        self.surname = surname
        self.age = age

    def __str__(self) -> str:
        return f'{self.first_name} {self.surname}'

    def test():
        pass

