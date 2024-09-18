# 13. Nhập nhiệt độ và kiểm tra xem đó là lạnh (dưới 10°C), mát (10-20°C), ấm (20-30°C), hay nóng (trên 30°C).
nhiet_do = int(input("Nhập nhiệt độ: "))

if nhiet_do < 10:
    print("Thời tiết lạnh.")
elif 10 <= nhiet_do <= 20:
    print("Thời tiết mát.")
elif 20 < nhiet_do <= 30:
    print("Thời tiết ấm.")
else:
    print("Thời tiết nóng.")
