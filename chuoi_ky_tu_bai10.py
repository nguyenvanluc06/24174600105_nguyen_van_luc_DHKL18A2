# Bài 10: Viết chương trình nhập vào một chuỗi ký tự, trả về kết quả chuỗi mới sau khi dồn tất cả số sang bên trái
# Ví dụ: Nhập vào: “Xsn61ssakdu271626s  1231  12”
#              Trả về: “61271626123112Xsnssakdus”

input_string = input("Nhập vào chuỗi ký tự: ")

chu_so = ''.join(char for char in input_string if char.isdigit())  
chu_cai = ''.join(char for char in input_string if not char.isdigit())

cong_tong = chu_so + chu_cai  
print(f"Chuỗi mới sau khi dồn số sang bên trái: {cong_tong}")