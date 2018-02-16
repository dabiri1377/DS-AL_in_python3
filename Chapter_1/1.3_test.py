# Expression, Operation and Precedence

# Logical Operation
# for boolean value
bool_f = False
bool_t = True
# not
print("not bool_f =", end='')
print(not bool_f, end='\n\n')

print("not bool_t =", end='')
print(not bool_t, end='\n\n')

# and
print("bool_f and bool_f = ", end='')
print(bool_f and bool_f, end='\n\n')

print("bool_f and bool_t = ", end='')
print(bool_f and bool_t, end='\n\n')

print("bool_t and bool_f = ", end='')
print(bool_t and bool_f, end='\n\n')

print("bool_t and bool_t = ", end='')
print(bool_t and bool_t, end='\n\n')

# or
print("bool_f or bool_f = ", end='')
print(bool_f or bool_f, end='\n\n')

print("bool_f or bool_t = ", end='')
print(bool_f or bool_t, end='\n\n')

print("bool_t or bool_f = ", end='')
print(bool_t or bool_f, end='\n\n')

print("bool_t or bool_t = ", end='')
print(bool_t or bool_t, end='\n\n')

####
# Equality Operation
bool_t = True
bool_f = False
int_1 = int(1)
int_0 = int(0)

# is
print("bool_t \'is\' bool_t? ", end='')
print(bool_t is bool_t, end='\n\n')

print("bool_t \'is\' int_1 ? ", end='')
print(bool_t is int_1, end='\n\n')

# is not => not is

# ==
print("bool_t \'==\' bool_t ? ", end='')
print(bool_t == bool_t, end='\n\n')

print("bool_t \'==\' int_1 ? ", end='')
print(bool_t == int_1, end='\n\n')

# != => not ==

####
# Comparison Operation
# < less than
# > larger than
# <= less then or equal to
# >= larger than or equal to


####
# Arithmetic Operation
# + add
# - subtraction
# * multiplication
# / true division
# // int division(9//2 == 4)
# % mod (9%2 == 1)

####
# Bitwise Operation
# ~  bitwise complement
# &  bitwise and(different with normal and)
# |  bitwise or(different with normal or)
# ^  bitwise XOR
# << shift bits left, filling in whit zero
# >> shift bits right, filling in with 'sing bit'

####
# Sequence Operation
s = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k')
t = ('123', '456')

# s[j] => element at index j
print("index 3 of s is s[2] : ", end='')
print(s[2], end='\n\n')

# s[start:stop] => slice including indices
print("s[2:6] is :", end='')
print(s[2:6], end='\n\n')  # print => ('c', 'd', 'e', 'f')

# s[start:stop:step] => slice including indices +step
print("s[1:9:2] is :", end='')
print(s[1:9:2], end='\n\n')  # print => ('b', 'd', 'f', 'h')

# s+t => concatenation of sequence
print("s+t is : ", end='')
print(s + t, end='\n\n')  # print => ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', '123', '456')

# k(number)*s => shorted for s+s+s+..+s (k time)
print("3*t is : ", end='')
print(3 * t, end='\n\n')  # print => ('123', '456', '123', '456', '123', '456')

# val 'in' s => containment check
print("check if 'c' in s : ", end='')
print('c' in s, end='\n\n')  # print => True

print("check if 'z' in s : ", end='')
print('z' in s, end='\n\n')  # print => False

# val 'not in' s => not val 'in' s
