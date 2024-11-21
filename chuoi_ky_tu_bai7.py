# Bài 7: Viết chương trình nhập vào chuỗi ký tự, kiểm tra xem chuỗi đó có phải số thập phân hay không

input_string = input("Nhap chuoi ky tu: ")

if input_string.replace('.', '', 1).isdigit():
    print(f"Day '{input_string}' la so thap phan")
else:
    print(f"Day '{input_string}' ko phai so thap phan")