import time
import random


# done
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


def random_repeated_list_analyzer(len_of_list, min_value, max_value, file_name):
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

    pool = tuple(random_list)
    n = len(pool)
    indices = list(range(n))
    cycles = list(range(n, 0, -1))

    # time_spend_for_smallest is usually 0
    temp_list_1 = list(pool[i] for i in indices[:n])
    time_spend_for_smallest = time_calculator_for_insertion_sort(temp_list_1)

    # I don't know how this work. but work good
    while n:
        for i in reversed(range(n)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i + 1:] + indices[i:i + 1]
                cycles[i] = n - i
            else:
                # I don't have any fucking idea how this work
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]

                # usually time_spend = 0
                temp_list_2 = list(pool[i] for i in indices[:n])
                time_spend = time_calculator_for_insertion_sort(temp_list_2)

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


random_repeated_list_analyzer(10, 1, 500, "test5")
