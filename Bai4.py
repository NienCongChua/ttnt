def ttong():
    tong = 0
    for i in range(1, 101, 2):
        tong += i
    return tong


print("Tong = {}".format(ttong()))
