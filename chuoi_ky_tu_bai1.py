# Bài 1: Viết chương trình nhập vào chuỗi ký tự, trả về số các từ trong chuỗi ký tự vừa nhập
# Ví dụ: Nhập vào: “Hom nay    troi   mua   ”          Trả về: 4

input_string = input("Nhap chuoi ky tu: ")

input_string = input_string.strip()

danh_sach = input_string.split()

dem_so_chuoi = len(danh_sach)

print(f"So tu trong chuoi la: {dem_so_chuoi}")