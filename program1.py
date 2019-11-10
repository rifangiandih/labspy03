a=100000000
sum=0
y=0
laba=[int(0),int(0),int(a)*.1,int(a)*.1,int(a)*.5,int(a)*.5,int(a)*.5,int(a)*.2]
print("modal awal Rp.",a)
for i in laba :
    sum = sum+i
    y+=1
    print("laba bulan ke-",y,"sebulan :",
          i)
print("total laba adalah :", sum)
