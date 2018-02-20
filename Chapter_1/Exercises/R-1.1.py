def is_multiply(n, m):
    n = int(n)
    m = int(m)
    if n // m == n / m:
        return True
    else:
        return False


# __main__
a, b = input("enter n and m:").split()
print(is_multiply(a, b))
