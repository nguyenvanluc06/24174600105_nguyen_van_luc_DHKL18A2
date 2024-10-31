print("1.Phim tình cảm")
print("2.Phim kinh dị")
print("3.Phim hoạt hình")
print("4.Phim khoa học viễn tưởng")

nhap_so_chon_phim = input("Vui lòng nhập số từ (1-4) để chọn phim: ")

if nhap_so_chon_phim == '1':
    print("Phim tình cảm")
elif nhap_so_chon_phim == '2':
    print("Phim kinh dị")
elif nhap_so_chon_phim == '3':
    print("Phim hoạt hình")
elif nhap_so_chon_phim == '4':
    print("Phim khoa học viễn tưởng")
else:
    print("Bạn nhập số ko hợp lệ, chỉ được nhập từ (1-4)")