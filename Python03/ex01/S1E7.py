from S1E9 import Character

# O que significa __str__ e __repr__


class Baratheon(Character):
    """Representing the Baratheon Family"""
    def __init__(self, name, is_alive=True):
        self.first_name = name
        self.is_alive = is_alive
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self):
        return ''

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister Family"""
    def __init__(self, name, is_alive=True):
        self.first_name = name
        self.is_alive = is_alive
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def __str__(self):
        return ''

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        self.is_alive = False

    def create_lannister(name, is_alive):
        return Lannister(name, is_alive)


def main():
    print()


if __name__ == "__name__":
    main()
