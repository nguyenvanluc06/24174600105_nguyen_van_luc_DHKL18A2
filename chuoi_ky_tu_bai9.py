# Bài 9: Viết chương trình nhập vào một chuỗi ký tự nhị phân 0 và 1. Kiểm tra xem chuỗi có phải số nhị phân không và chuyển đổi sang số thập phân
# Ví dụ: Nhập vào: “0010”
#              Trả về: “0010 la so nhi phan, chuyen sang thap phan: 2”

input_string = input("Nhap vao mot chuoi ky tu nhi phan: ")

if all(char in '01' for char in input_string):  
    print(f"'{input_string}' là số nhị phân.")  
     
    decimal_num = int(input_string, 2)  
    print(f"Chuyển sang số thập phân: {decimal_num}")  
else:  
    print(f"'{input_string}' không phải là số nhị phân.")