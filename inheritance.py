class Superclass:
    def super_method(self):
        print("Superclass method called")
class DerivedClass1(Superclass):
    def derived1_method(self):
        print("Derived class1 method called")
class DerivedClass2(DerivedClass1):
    def Derived2_method(self):
        print("Derived class2 method called")
d2=DerivedClass2()
d2.super_method()
d2.derived1_method()
d2.Derived2_method()
