# 27. Sắp xếp dictionary: Tạo một dictionary và sắp xếp theo key hoặc value.
number_dict = {"a": 10, "c": 20, "b": 30}
short_dict = dict(sorted(number_dict.items()))
print("Dictionary sắp xếp theo key:", short_dict)