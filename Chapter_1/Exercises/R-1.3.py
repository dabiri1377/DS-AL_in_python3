def minmax(data):
    temp_min = data[0]
    temp_max = data[0]
    for i in range(1, len(data)):
        if data[i] < temp_min:
            temp_min = data[i]
        if data[i] > temp_max:
            temp_max = data[i]
    temp = (temp_min, temp_max)
    return temp


x = [2, 4, 5, 7, 3, 2, 1, 0, 5, 20]
print(minmax(x))
