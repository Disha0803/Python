from abc import*
class Vehicle(ABC):
    @abstractmethod
    def noOfWheels(self):
        pass
    @abstractmethod
    def noOfSeats(self):
        pass
class car(Vehicle):
    def noOfWheels(self):
        print("4")
    def noOfSeats(self):
        print("4")
class bike(Vehicle):
    def noOfWheels(self):
        print("2")
    def noOfSeats(self):
        print("4")

b=bike()
b.noOfWheels()
