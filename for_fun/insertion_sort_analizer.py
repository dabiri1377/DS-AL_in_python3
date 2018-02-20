import time

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


def time_calculator_for_insertion_sort(input_list_for_insertion_sort):

    first_millis = int(round(time.time() * 1000))
    insertion_sort(input_list_for_insertion_sort)
    last_millis = int(round(time.time() * 1000))
    time_pass = last_millis - first_millis
    return time_pass


def all_list_analyzer(len_of_list):
    pass


def random_list_analyzer(len_of_list):
    pass


# __main__

