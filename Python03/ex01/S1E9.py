from abc import ABC, abstractmethod


class Character(ABC):
    """First Abstract Class"""
    def __init__(self, name, is_alive=True):
        """Constructor for Class"""
        self.first_name = name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Method Die, It changes the is_alive to False"""
        self.is_alive = False


class Stark(Character):
    """We Love Game of Thrones"""
    def die(self):
        """Method Die, It changes the is_alive to False"""
        self.is_alive = False


def main():
    print()


if __name__ == "__main__":
    main()
