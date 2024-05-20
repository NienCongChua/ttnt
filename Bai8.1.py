# Dfs
cay = {
    'A': ['B', 'C', 'D'],
    'B': ['M', 'N'],
    'C': ['L'],
    'D': ['O', 'P'],
    'M': ['X', 'Y'],
    'N': ['U', 'V'],
    'L': [],
    'O': ['I', 'J'], 
    'P': [],
    'X': [],
    'Y': ['R', 'S'],
    'U': [],
    'V': ['G', 'H'], 
    'I': [],
    'J': [],
    'R': [],
    'S': [],
    'G': [],
    'H': []
}

def chacon(sodo, con):
    for i in sodo:
        if con in sodo[i]:
            return i
    return []


def dfs(sodo, batdau, ketthuc):
    Mo = [batdau]
    Dong = []
    DuongDi = [ketthuc]
    while Mo:
        Dinh = Mo.pop()
        print(f"{Dinh} ", end='')
        if Dinh == ketthuc:
            print("--> Là đích --> Dừng tìm kiếm!")
            Mo = []
        else:
            if Dinh not in Dong:
                DinhKe = []
                for i in sodo[Dinh]:
                    DinhKe.insert(0, i)
                for i in DinhKe:
                    Mo.append(i)
                Dong.append(Dinh)
            else:
                continue
    
    while DuongDi[0] != batdau:
        print(f"Cha của {DuongDi[0]} là {chacon(sodo, DuongDi[0])}.")
        DuongDi.insert(0, chacon(sodo, DuongDi[0]))
    return DuongDi    


print(f"Đường đi: {dfs(sodo=cay, batdau='A', ketthuc='G')}")
