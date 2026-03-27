# field - Serve para configurar atributos da dataclass
# init=False - Nao entra no construtor - Da raise a um TypeError
# se tentarmos inserir
# default_factory - Atribui a um atributo da classe o retorno de uma funcao
# repr=False - Nao aparece no print
# compare=False - Ignorado no ==

# dataclass -> Forma automatica de criar uma classe que vai ser para
# principalmente guardar dados
# Cria ja 3 metodos (__init__, __repr__, __eq__), o construtor o repr que
# faz com que o print(class) fique "bonito" e o eq que permite fazer
# comparacoes entre objectos da classe

# __post_init__ -> E feito depois do init da classe e e usado para criar o
# login e o id

import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        self.login = self.name[0] + self.surname
        self.id = generate_id()
