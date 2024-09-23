# 18. In số đối xứng
# Viết chương trình kiểm tra và in các số đối xứng từ 1 đến n.
n = int(input("Nhập một số nguyên dương n: "))
for i in range(1, n+1):
    if str(i) == str(i)[::-1]:
        print(i, end=" ")
