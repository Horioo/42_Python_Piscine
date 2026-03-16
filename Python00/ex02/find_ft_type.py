# Ao usar list() no case ele verifica se o object é uma instancia da list, funciona igual para os outros casos
# Equivalente a isinstance(object, list)

def all_thing_is_obj(object: any) -> int:
	match object:
		case list():
			print("List :", type(object))
		case tuple():
			print("Tuple :", type(object))
		case set():
			print("Set :", type(object))
		case dict():
			print("Dict :", type(object))
		case str():
			print(object, "is in the kitchen :", type(object))
		case _:
			print("Type not Found")
	return 42