list1=[1,2,3,4,5,6,7,8,9] #quy dinh O la so 0 con X la so 12 #player 1 thang thi kq=1 player2 thang thi kq=2
lista=[]
listb=[]
p1=int(input("nguoi choi chon O nhap so 0 "))
p2=int(input("nguoi choi chon X nhap so 12 "))
print(list1[0],list1[1], list1[2])
print(list1[3], list1[4], list1[5])
print(list1[6], list1[7], list1[8])
flag=1
kq=0
so=0
def lisst(so,p):
    i = 0
    for i in range(0, 8):
        if so == list1[i]:
            list1.remove(list1[i])
            list1.insert(i, p)
    return list1
while flag==1:
    a=int(input("nguoi choi 1 muon danh O vao o nao? "))
    so=a
    p=p1
    list1=lisst(so,p)
    b = int(input("nguoi choi 2 muon danh X vao o nao "))
    so=b
    p=p2
    list1=lisst(so,p)
    print(list1[0], list1[1], list1[2])
    print(list1[3], list1[4], list1[5])
    print(list1[6], list1[7], list1[8])
    flag=0
#print(list1) tu khuc nay tro len dung roi nha gio chi con so sanh index thoai!!!!






