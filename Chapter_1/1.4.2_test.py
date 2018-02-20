# Control flow

####
# Loops

# while loops:
# while condition:
#   body
i = 7
while 0 < i:
    print(i)
    i -= 1

print("end of while")

# for loops:
# for element in iterable:
#   body
for i in range(5):
    print(i)

print("end of for #1")

# a list for test
list_1 = [10, 20, 30, 40, 50, 60, 70, 80]

# scan every member of list_1 and put it into var j and print it
for j in list_1:
    print(j)

print("end of for #2")

# counter for list
len_of_list_1 = 0

# this for scan every member of list_1, but not keep any member \
# in var
for _ in list_1:
    len_of_list_1 += 1

print(len_of_list_1)

print("end of for #3")

# example of book for scan a list and find max
data = [2, 56, 234, -23, 56, 23, 77, 0]
big_index = 0
for k in range(len(data)):
    if data[k] > data[big_index]:
        big_index = k
print("biggest index of 'data' is:", data[big_index])

# Break
# a break statement immediately terminate a while or for loop \
# when executed within its body.
list_1 = [10, 20, 30, 40, 50, 60, 70, 80]
for counter_of_list_1 in list_1:
    if counter_of_list_1 > 40:
        print("there is number larger than 40 in list")
        break

# Continue
# TODO: add example and command for this
