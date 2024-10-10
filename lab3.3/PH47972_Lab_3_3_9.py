# 9. In dãy Fibonacci
# Sử dụng vòng lặp để in ra dãy Fibonacci đến số thứ n.
n = int(input("Nhập số phần tử của dãy Fibonacci: "))
a, b = 0,1 
fibonacci = []
for _ in range(n):
    fibonacci.append(a)
    a, b = b, a + b
    
print(f"Dãy Fibonacci với {n} phần tử là: {fibonacci}")