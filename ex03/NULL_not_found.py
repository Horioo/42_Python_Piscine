# Verificar os diferentes tipos de NULL, como nao podemos usar funcoes externas temos de verificar se o object é diferente do objecto para ver se é NaN
# Com funcoes externas dava para usar o Math.isnan() para verificar mais facilmente
# Pelo convenção do IEEE NaN é diferente de NaN, por isso fazer Object != Object dá True neste caso

def NULL_not_found(object: any) -> int:
	if isinstance(object, float) and object != object:
		print("Cheese:", object, type(object))

	elif isinstance(object, bool) and object is False:
		print("Fake: ", object,  type(object))

	elif isinstance(object, int) and object == 0:
		print("Zero:",object, type(object))

	elif isinstance(object, str) and object == "":
		print("Empty:", object,  type(object))

	elif object is None:
		print("Nothing:", object, type(object))

	else:
		print("Type not Found")
		return 1
	return 0
