year = int(input("Nhập năm để tính: "))
if (year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0):
    print("Năm này là năm nhuận")
else:
    print("Năm này không phải là năm nhuận")