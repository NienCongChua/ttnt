sodo = {
    "A": ["C", "D", "E"],
    "E": [],
    "C": ["F"],
    "F": ["M", "H"],
    "M": [],
    "H": [],
    "D": ["I", "G"],
    "I": [],
    "G": ["R", "K"],
    "R": [],
    "K": []
}


def timkiem(mohinh, batdau, dich):
    Mo = [batdau]
    tmp = []
    Dong = []
    while Mo:
        Dinh = Mo.pop(0)
        if Dinh == dich:
            print(dich, "-> La dich -> dung tim kiem")
            break
        if Dinh not in Dong:
            Dong.append(Dinh)
            print(Dinh, end=" ")
            for Dinhke in mohinh[Dinh]:
                tmp.insert(0, Dinhke)
            while tmp:
                Mo.insert(0, tmp.pop(0))


timkiem(sodo, "A", "I")
