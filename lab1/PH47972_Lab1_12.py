# 12. Gán hai thời điểm (giờ, phút) trong ngày vào các biến, sau đó tính và in ra sự chênh lệch thời gian giữa chúng (tính bằng phút).
gio1, phut1 = 9, 30
gio2, phut2 = 11, 45
chenh_lech_phut = (gio2 * 60 + phut2) - (gio1 * 60 + phut1)
print(f"Chênh lệch thời gian: {chenh_lech_phut} phút")
