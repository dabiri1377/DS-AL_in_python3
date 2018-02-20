def is_even(k):
    if k | 1 == k:
        return False
    else:
        return True

print(is_even(int(input("enter number:"))))
