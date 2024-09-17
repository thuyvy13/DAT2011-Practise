number = int(input("Nhập một số nguyên 4 chữ số: "))
hang_nghin = number // 1000
hang_tram = (number % 1000) // 100
hang_chuc = (number % 100) // 10
hang_don_vi = number % 10

chuyen_doi = hang_don_vi * 1000 + hang_chuc * 100 + hang_tram * 10 + hang_nghin

print("Số nghịch đảo là:", chuyen_doi)