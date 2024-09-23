# 24. Kiểm tra số Armstrong
# Viết chương trình kiểm tra và in ra các số Armstrong từ 1 đến n.
n = int(input("Nhập một số nguyên dương n: "))
for so in range(1, n+1):
    so_str = str(so)
    bac = len(so_str)
    tong = sum(int(chu_so) ** bac for chu_so in so_str)
    if tong == so:
        print(f"{so} là số Armstrong")
