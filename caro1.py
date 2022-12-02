ca= [1, 2, 3, 4, 5, 6, 7, 8, 9]
so =0
ketqua = 0
p = "O"
flag=1
def ss(so,p): #so sánh để biết ai thắng
    kq=0
    for i in range(0, 7, 3): #trường hợp theo hàng ngang
        if (ca[i] == ca[i + 1]):
            if ca[i] == ca[i + 2]:
                if ca[i] == "O":
                    kq = 1
                else:
                    if ca[i]=="X":
                        kq=2
    for i in range (0,3): #trường hợp theo hàng dọc
        if (ca[i] == ca[i + 3]):
            if ca[i] == ca[i + 6]:
                if ca[i] == "O":
                    kq = 1
                else:
                    if ca[i]=="X":
                        kq=2
    if ca[4]=="O": #trường hợp chéo
        if (ca[0]=="O" and ca[8]=="O") or (ca[2]=="O"and ca[6]=="O"):
            kq=1
    elif (ca[0]=="X" and ca[8]=="X") or (ca[2]=="X"and ca[6]=="X"):
        kq=2
    return kq
def xuly(so, p): #cái này để thay thế số bằng dấu X hoặc O
    for i in range(0, 9):
        if so == ca[i]:
            ca.remove(ca[i])
            ca.insert(i, p)
    return ca
def hien(so, p): #này  để hiển thị bàn cờ caro
    for i in range(0, 8, 3):
        c = str(ca[i]) + " " + str(ca[i + 1]) + " " + str(ca[i + 2])
        print(c)
c = hien(so, p)
#nếu flag=1 thì trò chơi vẫn tiếp tục (các câu lệnh trong hàm while vẫn diễn ra), khi có 1 trong 2 người chơi thắng thì flag=0, khi đó hàm while sẽ dừng lại
while flag == 1: #này là cho người chơi nhập vào, gọi các hàm ở trên ra cho nó gọn
    a=int(input("nguoi choi 1 muon danh O vao o nao "))
    so = a
    p = "O"
    ca = xuly(so, p)
    ketqua = ss(so, p)
    c=hien(so,p)
    if ketqua!=1:
        b = int(input("nguoi choi 2 muon danh X vao o nao "))
        while b!=ca[b]: #dành cho trường hợp người chơi thứ 2 nhập vào ô mà người chơi 1 đã nhập rồi
            print("trung voi o cua nguoi choi 1. ")
            b = int(input("nguoi choi 2 muon danh X vao o nao "))
        so = b
    p = "X"
    ca = xuly(so, p)
    ketqua = ss(so, p)
    c = hien(so, p)
    if ketqua == 1 or ketqua == 2:
        flag=0
    #khi mà có 1 trong hai người thắng thì flag=0, khi quay lên đầu hàm while thì điều kiện sẽ sai, do đó hàm while dừng lại
if ketqua == 1: #xuất ai thắng ra màn hình
    print("nguoi choi 1 thang ")
else:
    print("nguoi choi 2 thang ")

