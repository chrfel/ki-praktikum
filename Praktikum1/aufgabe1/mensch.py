from re import U


class Mensch:
    
    def __init__(self, groesse, name) -> None:
        self.groesse = groesse
        self.name = name

    def __str__(self) -> str:
        self.__test()
        return f"{self.name} {self.groesse}"

    def __test(self):
        print("Hallo")

class SteinzeitMensch(Mensch):

    def __str__(self) -> str:
        return f"Ugabuga"

if __name__ == "__main__": 
    peter = Mensch(200, "Peter")
    ulli = SteinzeitMensch(150, "Ulli")
    print(peter)
    print(ulli)
    # peter.__test()