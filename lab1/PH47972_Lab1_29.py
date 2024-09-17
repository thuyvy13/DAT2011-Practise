# 29. Gán bốn số vào bốn biến, tính trung bình của hai số đầu và hai số cuối, sau đó so sánh hai giá trị trung bình và in ra kết quả của phép so sánh (lớn hơn, nhỏ hơn hoặc bằng).
num1 = 10
num2 = 20
num3 = 30
num4 = 40

avg_12 = (num1 + num2) / 2
avg_34 = (num3 + num4) / 2

if avg_12 > avg_34:
    print(f"{avg_12} > {avg_34}")
elif avg_12 < avg_34:
    print(f"{avg_12} < {avg_34}")
else:
    print(f"{avg_12} = {avg_34}")