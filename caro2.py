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
hien(so, p)
#nếu flag=1 thì trò chơi vẫn tiếp tục (các câu lệnh trong hàm while vẫn diễn ra), khi có 1 trong 2 người chơi thắng thì flag=0, khi đó hàm while sẽ dừng lại
while flag == 1: #này là cho người chơi nhập vào, gọi các hàm ở trên ra cho nó gọn
    a=10
    while a>9:
        try:
            a=int(input("nguoi choi 1 muon danh O vao o nao "))
        except ValueError:
            a=int(input("ban da nhap chu. nhap lai so "))
    so = a
    p = "O"
    ca = xuly(so, p)
    ketqua = ss(so, p)
    hien(so,p)
    b=10
    if ketqua!=1:
        while b>9:
            try:
                b = int(input("nguoi choi 2 muon danh X vao o nao "))
            except ValueError:
                b=int(input("ban da nhap chu. nhap lai so "))
        so = b
    p = "X"
    ca = xuly(so, p)
    ketqua = ss(so, p)
    hien(so, p)
    k=int(0)
    for i in range(0,9):
        if ca[i]=="O" or ca[i]=="X":
            k=k+1
    if k==9:
        ketqua=3
    if ketqua == 1 or ketqua == 2 or ketqua==3:
        flag=0
    #khi mà có 1 trong hai người thắng thì flag=0, khi quay lên đầu hàm while thì điều kiện sẽ sai, do đó hàm while dừng lại
if ketqua == 1: #xuất ai thắng ra màn hình
    print("nguoi choi 1 thang ")
elif ketqua==2:
    print("nguoi choi 2 thang ")
elif ketqua==3:
    print("hoa")

