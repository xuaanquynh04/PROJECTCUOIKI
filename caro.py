ca= [1, 2, 3, 4, 5, 6, 7, 8, 9]
so = 0
ketqua = 0
p = "O"
flag=1
def ss(so,p):
    kq=0
    for i in range(0, 7, 3):
        if (ca[i] == ca[i + 1]):
            if ca[i] == ca[i + 2]:
                if ca[i] == "O":
                    kq = 1
                else:
                    if ca[i]=="X":
                        kq=2
    for i in range (0,3):
        if (ca[i] == ca[i + 3]):
            if ca[i] == ca[i + 6]:
                if ca[i] == "O":
                    kq = 1
                else:
                    if ca[i]=="X":
                        kq=2
    if ca[4]=="O":
        if (ca[0]=="O" and ca[8]=="O") or (ca[2]=="O"and ca[6]=="O"):
            kq=1
    elif (ca[0]=="X" and ca[8]=="X") or (ca[2]=="X"and ca[6]=="X"):
        kq=2
    return kq
def xuly(so, p):
    for i in range(0, 9):
        if so == ca[i]:
            ca.remove(ca[i])
            ca.insert(i, p)
    return ca
def hien(so, p):
    for i in range(0, 8, 3):
        c = str(ca[i]) + " " + str(ca[i + 1]) + " " + str(ca[i + 2])
        print(c)
def xuly(so, p):
    for i in range(0, 9):
        if so == ca[i]:
            ca.remove(ca[i])
            ca.insert(i, p)
    return ca
c = hien(so, p)
while flag == 1:
    a=int(input("nguoi choi 1 muon danh O vao o nao "))
    so = a
    p = "O"
    ca = xuly(so, p)
    ketqua = ss(so, p)
    c=hien(so,p)
    if ketqua!=1:
        b = int(input("nguoi choi 2 muon danh X vao o nao "))
        so = b
    p = "X"
    ca = xuly(so, p)
    ketqua = ss(so, p)
    c = hien(so, p)
    if ketqua == 1 or ketqua == 2:
        flag = 0
if ketqua == 1:
    print("nguoi choi 1 thang ")
else:
    print("nguoi choi 2 thang ")

