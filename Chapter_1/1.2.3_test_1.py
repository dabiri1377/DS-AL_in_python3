def print_type_value(datatype, name_of_var):
    # print type of 'datatype'
    print("type of " + str(name_of_var) + " = ", end='')
    print(type(datatype))
    # print value of datatype
    print("value of " + str(name_of_var) + " =", end='')
    print(datatype, end='\n\n')


# ali is an id for bool class
ali = bool()
print_type_value(ali, "ali")

# ali is id for True, in the bool class
ali = True
print_type_value(ali, "ali")

# ali_2 is ID for True
ali_2 = True
print_type_value(ali_2, "ali_2")

# ali_3 is ID for string
ali_3 = "sdfsadf"
print_type_value(ali_3, "ali_3")

# moh is an int
moh = 12
print_type_value(moh, "moh")

# moh_2 is an int
moh_2 = 12000000000000000000000020022
print_type_value(moh_2, "moh_2")

# moh_3 is an int, but Hex
moh_3 = 0x23
print_type_value(moh_3, "moh_3")

#####
# in int:
# for Hex   => 0x
# for Oct   => 0o
# for Bin   => 0b
# for base 10 just type it

# moh_4 is a float
moh_4 = 3.4343e20
print_type_value(moh_4, "moh_4")

######
# list
# list is array base

# list_1 is a list
list_1 = list()
print_type_value(list_1, "list_1")

# list_2 is a list
list_2 = ['red', 54, 3.43e23]
print_type_value(list_2, "list_2")

#####
# tuple
# tuple is immutable version of sequence

# tuple_1 is a tuple
tuple_1 = (3, 4, 3)
print_type_value(tuple_1, "tuple_1")

# tuple_2 is a tuple
tuple_2 = (3,)
print_type_value(tuple_2, "tuple_2")
