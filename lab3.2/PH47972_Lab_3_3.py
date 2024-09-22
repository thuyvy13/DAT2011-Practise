# 3. Xóa phần tử khỏi danh sách: Nhập một giá trị từ bàn phím và xóa phần tử đó khỏi danh sách nếu có.
my_list = []
value = input("Nhập một giá trị từ bàn phím: ")
my_list.append(value)

if value in my_list:
    my_list.remove(value)
    print(f"Đã xoá {value} khỏi danh sách")
else:
    print(f"Phần tử {value} không có trong danh sách")