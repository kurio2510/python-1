n = int(input("Nhap mot so nguyen duong: "))
temp = n
so_dao_nguoc = 0
while temp > 0:
    so_dao_nguoc = so_dao_nguoc * 10 + temp % 10
    temp //= 10
if n == so_dao_nguoc:
    print("So vua nhap la so doi xung")
else:
    print("So vua nhap khong phai la so doi xung")
