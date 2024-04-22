def giaipt(a, b):
    if a == 0:
        if b == 0:
            print("Phuong trinh co vo so nghiem.")
        else:
            print("Phuong trinh vo nghiem.")
    else:
        print("Phuong trinh co nghiem duy nhat: x = {}".format(-b / a))


c, d = map(float, input("Nhap he so a, b: ").split(" "))
giaipt(c, d)
