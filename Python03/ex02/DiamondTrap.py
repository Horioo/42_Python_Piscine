from S1E7 import Baratheon, Lannister

# Heranca Diamante acontece quando uma classe herda de 2 classes que herdam
# da mesma classe mae

# Python usa MRO (Method Resolution Order), que decreta uma ordem de Herança
# O que impede que o __init__ do Character seja chamado apenas 1 vez
# Se usares o King.mro() vai mostrar qual a ordem da herança


class King(Baratheon, Lannister):
    def __init__(self, name, is_alive=True):
        "Constructor of King Class"
        super().__init__(name, is_alive)

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

    def set_eyes(self, color):
        """
        Set the eye color of the character.

        Args:
            color (str): New eye color.

        Returns:
        None
        """
        self.eyes = color

    def set_hairs(self, color):
        """
        Set the hair color of the character.

        Args:
            color (str): New hair color.

        Returns:
            None
        """
        self.hairs = color

    def get_eyes(self):
        """
        Get the eye color of the character.

        Returns:
            str: Eye color.
        """
        return self.eyes

    def get_hairs(self):
        """
        Get the hair color of the character.

        Returns:
            str: Hair color.
        """
        return self.hairs


def main():
    print()


if __name__ == "__main__":
    main()
