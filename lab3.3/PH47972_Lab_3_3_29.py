# 29. In các số Fibonacci nhỏ hơn n
# Sử dụng vòng lặp để in ra các số Fibonacci nhỏ hơn n.
n = int(input("Nhập một số nguyên dương n: "))
a, b = 0, 1
while a < n:
    print(a, end=" ")
    a, b = b, a + b
