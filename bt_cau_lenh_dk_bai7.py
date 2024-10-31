# Nhập các hệ số từ người dùng  
a_1 = float(input("Nhập a1: "))  
b_1 = float(input("Nhập b1: "))  
c_1 = float(input("Nhập c1: "))  
a_2 = float(input("Nhập a2: "))  
b_2 = float(input("Nhập b2: "))  
c_2 = float(input("Nhập c2: "))  

D = a_1 * b_2 - a_2 * b_1
D_1 = c_1 * b_2 - c_2 * b_1
D_2 = a_1 * c_2 - a_2 * c_1

if D != 0:  
    x = D_1 / D  
    y = D_2 / D  
    print(f"Nghiệm duy nhất: x = {x}, y = {y}")  
elif D_1 == 0 and D_2 == 0:  
    print("Hệ phương trình có vô số nghiệm.")  
else:  
    print("Hệ phương trình vô nghiệm.")