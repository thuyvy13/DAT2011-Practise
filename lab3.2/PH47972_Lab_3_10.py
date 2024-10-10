# 10. Lọc phần tử trong danh sách: Tạo một danh sách và lọc các phần tử lớn hơn một giá trị nhập từ bàn phím.
filter_list = [10, 23, 20, 5, 6]
value = int(input("Nhập các phần tử để lọc phàn từ lớn hơn: "))
filter = [x for x in filter_list if x > value]
print(f"Các phần tử lớn hơn {filter_list}: {value}")