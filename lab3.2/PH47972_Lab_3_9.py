# 9. Tạo danh sách từ input: Nhập các phần tử từ bàn phím và lưu vào danh sách cho đến khi người dùng nhập "done".
my_list = []
while True:
    value = input("Nhập phần tử (hoặc 'done' để kết thúc): ")
    if value.lower() == 'done':
        break
    my_list.append(value)

print("Danh sách: ", my_list)    