# Bài 3: Viết chương trình nhập vào họ tên đầy đủ, trả về tên và họ riêng
# Ví dụ: Nhập vào: “Vo Van Nam”
#              Trả về: “Ho: Vo, Ten: Nam”

nhap_ho_ten = input("Nhap Ho va Ten : ")

danh_sach = nhap_ho_ten.split()

last_name = danh_sach[0]
first_name = danh_sach[-1]

print(f"Ho: '{last_name}', Ten: '{first_name}'")