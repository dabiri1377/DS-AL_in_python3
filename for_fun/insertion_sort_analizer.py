import xlwt
import time
import itertools
import random


def insertion_sort(input_list):
    """
    Insertion sort algorithm.

    :param input_list:
     List for sort
    :return:
     Sorted input_list
    """
    for index in range(1, len(input_list)):

        current_value = input_list[index]
        position = index

        while position > 0 and input_list[position - 1] > current_value:
            input_list[position] = input_list[position - 1]
            position = position - 1

        input_list[position] = current_value
    return input_list


def random_list_generator(len_of_list):
    pass


# done
def time_calculator_for_insertion_sort(input_list_for_insertion_sort):
    first_millis = int(round(time.time() * 1000))
    insertion_sort(input_list_for_insertion_sort)
    last_millis = int(round(time.time() * 1000))
    return last_millis - first_millis


def random_repeated_list_analyzer(len_of_list, min_value, max_value):
    # Generate a empty list for fill with random number \
    # between min_value to max_value
    random_list = []

    # Create len_of_list value and put them into random_list
    for i in range(len_of_list):
        # Generate a random number between min_value and max_value \
        # and put it into random_list
        random_list.append(random.randint(min_value, max_value))

    # sort for show time Lo to Hi
    random_list.sort()


    """    
    print("test")
    # TODO: optimize this
    pool = tuple(random_list)
    n = len(pool)
    for indices in itertools.product(range(n), repeat=n):
        print("test3")
        if len(set(indices)) == n:
            print("test4")
            permutations_one_by_one = list(pool[i] for i in indices)
            copy_of = permutations_one_by_one.copy()
            # call Insertion sort
            time_spend = time_calculator_for_insertion_sort(permutations_one_by_one)
            if time_spend != 0:
                # for_debug
                print("tuple =:", copy_of)
                print("time spend", time_spend)

"""

    pool = tuple(random_list)
    n = len(pool)
    indices = list(range(n))
    cycles = list(range(n, 0, -1))
    # TODO: add time_calculator_for_insertion_sort
    print(tuple(pool[i] for i in indices[:n]))

    while n:
        for i in reversed(range(n)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i + 1:] + indices[i:i + 1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                # TODO: add time_calculator_for_insertion_sort
                print(tuple(pool[i] for i in indices[:n]))

                break
        else:
            break

    print("final test")
    pass


def random_list_analyzer(len_of_list):
    pass


# __main__

# for test
# test_list = [x for x in range(5000, 0, -1)]
# print(time_calculator_for_insertion_sort(test_list))


random_repeated_list_analyzer(4, 10, 50)
