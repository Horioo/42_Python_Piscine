from S1E9 import Character

# O que significa __str__ e __repr__
# __str__: É um metodo especial que define o que aparece quando chamas
# o print do teu objeto

# __repr__: É um metodo especial que é usado para mostrar a forma
# Oficial do objeto, usada para debugs e internamente na area de programação

# decoratos: é uma funcao que modifica outra funcao mas que nao mudar
# o codigo da original

# classmethod: Permite criar objectos de forma controlada
# É tambem um metodo que pertence a class e nao a um objecto especifico


class Baratheon(Character):
    """Representing the Baratheon Family"""
    def __init__(self, name, is_alive=True):
        self.first_name = name
        self.is_alive = is_alive
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self):
        """
        Return a user-friendly string representation of the object.

        Returns:
            str: Readable string describing the object.
        """
        return ''

    def __repr__(self):
        """
        Return an unambiguous string representation of the object.

        Returns:
            str:Technical representation including family name, eyes,and hairs.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """
        Set the character's life status to False.

        Returns:
            None
        """
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
        """
        Return a user-friendly string representation of the object.

        Returns:
            str: Readable string describing the object.
        """
        return ''

    def __repr__(self):
        """
        Return an unambiguous string representation of the object.

        Returns:
            str:Technical representation including family name, eyes,and hairs.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """
        Set the character's life status to False.

        Returns:
            None
        """
        self.is_alive = False

    @classmethod
    def create_lannister(cls, name, is_alive):
        """
        Create a new Lannister instance.

        Args:
            cls (type): The class used to create the instance.
            name (str): Name of the character.
            is_alive (bool): Life status of the character.

        Returns:
            Character: A new instance of the class.
        """
        return cls(name, is_alive)


def main():
    print()


if __name__ == "__name__":
    main()
