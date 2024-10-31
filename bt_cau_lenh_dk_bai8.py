nhap_diem = input("Nhập điểm để phân loại xếp hạng chỉ nhập các kí tự (A, B, C, D, E, F) :")

if nhap_diem == 'A':
    print("Là học sinh xuất sắc")
elif nhap_diem == 'B':
    print("Là học sinh giỏi")
elif nhap_diem == 'C':
    print("Là học sinh khá")
elif nhap_diem == 'D':
    print("Là học sinh trung bình")
elif nhap_diem == 'E':
    print("Là học sinh yếu")
elif nhap_diem == 'F':
    print("Là học sinh kém")
else:
    print("Bạn nhập kí tự ko hợp lệ, chỉ được nhập các kí tự (A, B, C, D, E, F)")