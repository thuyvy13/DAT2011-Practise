# 19. Viết một chương trình yêu cầu người dùng nhập hai số nguyên và tính số dư của phép chia số đầu tiên cho số thứ hai. Xuất kết quả số dư ra màn hình.
so_1 = int(input("Nhập số nguyên thứ nhất: "))
so_2 = int(input("Nhập số nguyên thứ hai: "))

so_du = so_1 % so_2

print(f"Số dư của phép chia {so_1} cho {so_2} là: {so_du}")
