ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# Classic List Access
ft_list[1] = "World!"

# Since Tuples are unchangeables we have to make it a list and then change the value we want and change it back
tmp = list(ft_tuple)
tmp[1] = "Portugal!"
ft_tuple = tuple(tmp)

# Sets are also unchangeables and dont allow Duplicates, so we removed the last element and added another one
ft_set.discard("tutu!")
ft_set.add("Lisbon!")

# Dictionaries allow direct Access via Key:value Pair
ft_dict["Hello"] = "42Lisboa!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)