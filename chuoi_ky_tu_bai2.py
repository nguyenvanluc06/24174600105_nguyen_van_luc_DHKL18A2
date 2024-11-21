# Bài 2: Viết chương trình nhập vào chuỗi ký tự, trả về chuỗi ký tự sau khi loại bỏ tất cả các dấu cách thừa
# Ví dụ: Nhập vào: “Hom nay    troi   mua   ”
#              Trả về: “Hom nay troi mua”

input_string = input("Nhap chuoi ky tu: ")

danh_sach = input_string.split()

xoa_khoang_trang = ' '.join(danh_sach)

print(f"Chuoi ky tu sau khi bi loai bo la: {xoa_khoang_trang}")