# Para usar um metodo da classe sem ter de instanciar procurei aqui
# https://www.geeksforgeeks.org/python/how-to-call-a-method-on-a-class-without-instantiating-it-in-python/

# Podemos usar 3 formas diferentes
# staticmethod -> Deixa que usemos metodos sem termos de instanciar a classe,
# não necessita do self
# classmethod -> Retorna um variavel da classe sem a termos de instanciar,
# usa a classe (cls) em vez do objeto da classe (self)

# metaclass -> Uma classe que cria outra classe


class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Compute and print the dot product of two vectors.

        Args:
            V1 (list[float]): First vector.
            V2 (list[float]): Second vector.

        Returns:
            None
        """
        dot = [a * b for a, b in zip(V1, V2)]
        res = 0
        for v in dot:
            res += v
        print(f"Dot product is: {res}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Compute and print the element-wise addition of two vectors.

        Args:
            V1 (list[float]): First vector.
            V2 (list[float]): Second vector.

        Returns:
            None
        """
        res = [float(a + b) for a, b in zip(V1, V2)]
        print(f"Add Vector is : {res}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Compute and print the element-wise subtraction of two vectors.

        Args:
            V1 (list[float]): First vector.
            V2 (list[float]): Second vector.

        Returns:
            None
        """
        res = [float(a - b) for a, b in zip(V1, V2)]
        print(f"Sous Vector is: {res}")


def main():
    print()


if __name__ == "__main__":
    main()
