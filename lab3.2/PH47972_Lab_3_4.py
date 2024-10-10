# 4. Tìm kiếm phần tử trong danh sách: Nhập một giá trị từ bàn phím và kiểm tra xem nó có trong danh sách hay không.
my_list = []
value = input("Nhập một giá trị: ")
my_list.append(value)

if value in my_list:
    print(f"{value} có trong danh sách")
else:
    print(f"{value} không có trong danh sách")
