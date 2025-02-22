class Mammal:
    def Mammal_info(self):
        print("Mammals can give direct birth")
class wingedAnimal:
    def winged_Animal_info(self):
        print("Winged Animals can fly")
class Bat(Mammal,wingedAnimal):
    pass
b1=Bat()
b1.Mammal_info()
b1.winged_Animal_info()
