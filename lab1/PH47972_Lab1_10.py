# 10. Gán một số có ba chữ số (ví dụ: 123), tách các chữ số ra (lấy phần chia dư và phần nguyên) và tính tổng của chúng (1 + 2 + 3).
so = 123
hang_tram = so // 100
hang_chuc = (so // 10) % 10
hang_don_vi = so % 10
tong = hang_tram + hang_chuc + hang_don_vi
print(f"Tổng các chữ số: {tong}")
