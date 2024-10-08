import pickle
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    WHITE = 4
    BLACK = 5


class OverCapacityError(Exception):
    """
    Business Exception
    OverCapacityError is an Exception
    OverCapacityError: subclass/derived class
    Exception: super class/base class
    Raised when an over-capacity error is encountered.
    """

    def __init__(self, message: str, over_weight: float):
        super().__init__()
        self.message = message
        self.__over_weight = over_weight

    @property
    def over_weight(self):
        return self.__over_weight

    def __str__(self) -> str:
        return f'OverCapacityError [{self.message}]: {self.over_weight}'


class vehicle:
    """
            members:
            1. attributes         -> licence_plate, capacity, load, color
            2. (business) methods -> load, unload, constructor (__init__) -> create object
                                     getter/setter
                                     __str__: def __str__ object -> str
    """

    def __init__(self, licence_plate: str, capacity: float = 3_000, color: Color = Color.BLACK):
        self.__licence_plate = licence_plate
        self.__capacity = capacity
        self.__color = color
        self.__load = 0

    @property
    def capacity(self):
        return self.__capacity

    @property
    def license_plate(self):
        return self.__licence_plate

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: Color):
        self.__color = color

    @property
    def current_load(self):
        return self.__load

    def load(self, weight: float) -> float:
        if weight <= 0.0:
            raise ValueError('weight must be greater than zero')
        if weight + self.__load > self.__capacity:
            raise OverCapacityError(f"{self.__load} and {weight} exceeds the capacity {self.__capacity}",
                                    self.__load + weight - self.__capacity)
        self.__load += weight
        return self.__load

    def unload(self, weight: float) -> float:
        print(f"unloading the weight ({weight}) from the vehicle ({self.__licence_plate})")
        if weight <= 0.0:
            raise ValueError('weight must be greater than zero')
        if weight > self.__load:
            raise ValueError('weight must be less than or equal to load')
        self.__load -= weight
        return self.__load

    def __str__(self):
        return f"vehicle[license_plate={self.__licence_plate}, color= {self.__color}, current load= {self.current_load}, capacity={self.__capacity}]"


vehicle1 = vehicle("34abc42", 5_000, Color.RED)

with open("vehicle.pkl", "wb") as file:
    pickle.dump(vehicle1, file)
