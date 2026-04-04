class Sim:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.happiness = 100

    def celebrate_birthday(self):
        self.age += 1
        self.happiness += 10
        print(f"{self.name} святкує день народження! Тепер йому {self.age} років.")

    def lose_happiness(self, amount):
        self.happiness -= amount
        if self.happiness < 0:
            self.happiness = 0
        print(
            f"{self.name} втратив {amount} щастя. Тепер його щастя: {self.happiness}.")


class House:
    def __init__(self, address):
        self.address = address
        self.residents = []

    def add_resident(self, sim):
        self.residents.append(sim)
        print(f"{sim.name} переїхав до {self.address}.")

    def show_residents(self):
        print(f"Жителі будинку за адресою {self.address}:")
        for resident in self.residents:
            print(
                f"- {resident.name}, {resident.age} років, щастя: {resident.happiness}.")


sim1 = Sim("Аліса", 25)
sim2 = Sim("Боб", 30)

house = House("вул. Сімейна, 10")
house.add_resident(sim1)
house.add_resident(sim2)

house.show_residents()

sim1.celebrate_birthday()
sim2.lose_happiness(20)
