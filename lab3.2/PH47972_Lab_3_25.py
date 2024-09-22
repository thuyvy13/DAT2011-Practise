# 25. Lặp qua dictionary: Sử dụng vòng lặp để in ra tất cả các cặp key-value.
my_dict = {
    "name": "Zyy",
    "age": 20,
    "city": "Yên Bái"
}
for key, value in my_dict.items(): #item trả về một đối tượng view chứa tất cả các cặp key-value trong dictionary dưới dạng tuple
    print(f"Key: {key}, Value: {value}")