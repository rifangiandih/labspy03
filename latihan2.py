print("perogram menampilkan bilangan terbesar ")
a=1
max=0
while a !=0:
    if a > max:
        max = a
        a= int(input("masukan bilangan :"))
        if a == 0:
            break
print("nilai terbesarnya adalah:",max)
