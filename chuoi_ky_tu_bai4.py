# Bài 4: Viết chương trình nhập vào chuỗi ký tự, trả về kết quả đếm số ký tự là chữ,
# số ký tự là số và số ký tự là ký tự đặc biệt (Không là số, không là chữ) trong chuỗi

input_string = input("Nhap chuoi ky tu: ")

chu_ky_tu = 0
so_ky_tu = 0
so_ky_tu_dac_biet = 0

for char in input_string:
    if char.isalpha():
        chu_ky_tu += 1
    elif char.isdigit():
        so_ky_tu += 1
    else:
        so_ky_tu_dac_biet += 1

print(f"Chu_cai: {chu_ky_tu}, So: {so_ky_tu}, Ky_tu_dac_biet: {so_ky_tu_dac_biet}") 
