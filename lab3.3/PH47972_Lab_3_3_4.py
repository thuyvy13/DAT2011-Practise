# 4. Đếm số lượng ký tự trong chuỗi
# Nhập một chuỗi và sử dụng vòng lặp để đếm số ký tự.
str = input("Nhập vào một chuỗi: ")
count_str = 0
for i in str:
    count_str += 1
print(f"Số kí tụ trong chuỗi là {count_str}")