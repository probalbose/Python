# If the first and last element of a list is equal or if the list is empty call it 'beautiful'


def iterUnpacking(a):

    # res = [i for i in a] #list comprehension
    res = a[:]
    while res and res[0] != res[-1]:
        first, *res, last = res  # iterable unpacking
    print("Beautiful list: ", res)


a = [3, 5, 6, 8, 6, 9, 7]
iterUnpacking(a)
