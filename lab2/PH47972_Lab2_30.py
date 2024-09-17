# 30. Viết một chương trình yêu cầu người dùng nhập bán kính đáy và chiều cao của hình nón, sau đó tính diện tích bề mặt và thể tích của hình nón đó. Xuất kết quả ra màn hình.
import math

ban_kinh = float(input("Nhập bán kính đáy của hình nón: "))
chieu_cao = float(input("Nhập chiều cao của hình nón: "))

chieu_cao_nghieng = math.sqrt(ban_kinh ** 2 + chieu_cao ** 2)
s_mat_ben = math.pi * ban_kinh * (ban_kinh + chieu_cao_nghieng)
v = (math.pi * ban_kinh ** 2 * chieu_cao) / 3

print(f"Diện tích bề mặt của hình nón là {s_mat_ben:.2f}")
print(f"Thể tích của hình nón là {v:.2f}")
