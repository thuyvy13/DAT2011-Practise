# 28. Gán một số ngày vào biến và tính tương đương số năm, tháng (1 năm = 365 ngày, 1 tháng = 30 ngày), sau đó in ra kết quả.
so_ngay = 400
nam = so_ngay // 365
thang = (so_ngay % 365) // 30
print(f"{so_ngay} ngày tương đương với {nam} năm và {thang} tháng")