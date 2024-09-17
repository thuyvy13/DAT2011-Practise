# 29. Viết một chương trình yêu cầu người dùng nhập hai đường chéo của hình thoi và tính diện tích và chu vi của hình thoi đó. Xuất kết quả ra màn hình.
import math

duong_cheo_1 = float(input("Nhập độ dài đường chéo thứ nhất: "))
duong_cheo_2 = float(input("Nhập độ dài đường chéo thứ hai: "))

s = (duong_cheo_1 * duong_cheo_2) / 2
chieu_dai_canh = math.sqrt((duong_cheo_1 / 2) ** 2 + (duong_cheo_2 / 2) ** 2)
chu_vi = 4 * chieu_dai_canh

print(f"Diện tích của hình thoi là {s:.2f}")
print(f"Chu vi của hình thoi là {chu_vi:.2f}")
