def return_smaller_root_seq(int_number):
    sum_temp = 0
    for i in range(int_number, 0, -1):
        sum_temp += i ** 2
    return sum_temp


print(return_smaller_root_seq(3))
