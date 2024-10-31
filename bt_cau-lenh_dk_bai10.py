tien_luong = float(input("Nhập lương của nhân viên: "))

if tien_luong > 15:
    tien_thue = tien_luong * 0.3
elif tien_luong >= 7:
    tien_thue = tien_luong * 0.2
else:
    tien_thue = tien_luong * 0.1

luong_con_lai = tien_luong - tien_thue

print("Thuế thu nhập: ", tien_thue, "Triệu Đồng")
print("Lương dòng: ", luong_con_lai, "Triệu Đồng")