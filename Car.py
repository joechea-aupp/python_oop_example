from abc import ABC, abstractclassmethod

class Car(ABC):
    def __init__(self, name):
        self.name = name
        # Encapsulation example,
        # We are using __color as private variable 
        self.__color = ""

    # and can only be access using getter and setter
    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color
    
    # example of polymorphism
    # where method can be overriden by child class
    def make_noise(self):
        print("Vroom Vroom")

    # exmaple of abstract method
    # where child class must implement this method
    # parent method has no idea of how it will be implemented
    # it is up to child class to implement it
    @abstractclassmethod
    def start(self):
        pass

    @abstractclassmethod
    def stop(self):
        pass


# inheritance example, EVCar and GasCar are child class of Car
class EVCar(Car):
    def __init__(self, name):
        # inherit __color and its setter, getter method from parent class
        # EVCar can access this method without defining in itself
        super().__init__(name)
        self.battery = 100

    # having their own start and stop class, which required by parent class CAR
    def start(self):
        print("Click start button")

    def stop(self):
        print("Click stop button")

    def charge(self):
        self.battery = 100
        print("Charging the car")

    # morph the make_noise method, make it into iself
    def make_noise(self):
        print("Psssssssss")


class GasCar(Car):
    def __init__(self, name):
        super().__init__(name)
        self.fuel = 100

    def start(self):
        print("Turning the key to start the car")

    def stop(self):
        print("Turing the key to stop the car")
    
    def refuel(self):
        self.fuel = 100
        print("Refueling the car")

    def make_noise(self):
        print("Proom Proom")