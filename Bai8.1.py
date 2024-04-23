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


def chacon(mohinh, con):
    for i in mohinh:
        if con in mohinh[i]:
            return i
    return []    


def timkiem(mohinh, batdau, dich):
    Mo = [batdau]
    tmp = []
    Dong = []
    dichh = dich
    while Mo:
        Dinh = Mo.pop(0)
        if Dinh == dich:
            print(dich, "--> la dich --> dung tim kiem")
            Mo = []
        else:
            if Dinh not in Dong:
                Dong.append(Dinh)
                print(Dinh, end=' ')
                for Dinhke in (mohinh[Dinh]):
                    tmp.insert(0, Dinhke)
                while tmp:
                    Mo.insert(0, tmp.pop(0))
    while dich != batdau:
        duongdi = [dich]
        print(f"Cha cua {dich} la {chacon(mohinh, dich)}")
        duongdi.insert(0, chacon(mohinh, dich))
        dich = chacon(mohinh, dich)
        duongdi.append(dichh)
    print(f"==> Duong di = {duongdi}")



# A C F M H D I --> la dich --> dung tim kiem
timkiem(sodo, "A", "I")
