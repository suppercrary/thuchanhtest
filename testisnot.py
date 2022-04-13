#p1 1
"""from datetime import date
x=input("nhap tên")
y=int(input("nhap tuổi hay năm sinh "))
t=100-y
t1=y+100
today=date.today()
year=today.year +t
if 1000>y>=100:
    print(x ,"bạn đã bằng hoặc hơn 100 tuổi, tuổi hiện giờ đã",y)
elif y>=1000:
    print("bạn ",x,"phải sống tới năm ",t1,"mới được 100 tuổi")
else:
    print("bạn ",x,"phải sống tới năm ",year,"mới được 100 tuổi")

#2
    #c1
def main():
    x=[1,2,3,4,5,6,7]
    list1 = x[:3]+x[-1:]
    print(list1)
if __name__=="__main__":
    main()
    #c2
def list(x):
    list1 = x[:3]+x[-1:]
    print(list1)
def main():
    x=[1,2,3,4,5,6,7]
    #list1 = x[:3]+x[-1:]
    #print(list1)
    list(x)

#3
KH={'Albert Einstein':'28/10/1955','Bill Gates':'19/10/1955','Steve Jobs':'12/9/1999'}
list=["Albert Einstein","Bill Gates","Steve Jobs"]
print("Welcome to the birthday dictionary. We know the birthdays of:")
for i in list:
    print(i)
x=input("Who's birthday do you want to look up?")
print(x,"'s birthday is", KH[x])
print(f'{x}s birthday is {KH[x]}')
print('{}s sn is {}'.format(x,KH[x]))
#4

def xh(list,l,r,x):
    if r>=l:
        m=l+(r-l)//2
        if list[m]==x:
            return m
        elif list[m]>x:
            return xh(list,l,m-1,x)
        else:
            return xh(list,m+1,r,x)
    else:
        return -1
list=[1,3,7,8,9]
x=8

result= xh(list,0,len(list)-1,x)
if result != -1:
    print("True")
else:
    print(" Fla")
    """
#p2 1
"""
x=int(input("xin bạn nhập số nguyên dương : "))
list=[]
list1=[]
i=1
while i != (x+1):
    t=x%i
    if t==0:
        list.append(i)
    i +=1
print(list)

#2
x=str(input("nhập chuỗi kí tự : "))
listx=list(x)
y= x.lower()
listy=list(y)
if listy==listx:
    print("True")
else:
    print("False")
#3
#thử nghiệm
a=[]
x=str(input("nhap 1 dãy số "))
y=list(x)
for i in y:
    if i !=",":
        i1=int(i)
        a.append(i1)
print(a)
#thử nghiệm
#lời giải cho câu 3
a = [1, 1, 2, 3, 5, 9, 12, 23, 35, 56, 88]
a1=[]
a2=[]
for i in a:
    if i< 5:
        a1.append(i)

print(a1)
x=int(input("nhập số nhỏ hơn số trên: "))
for r in a1:
    if r < x:
        a2.append(r)
print(a2)
#4
a=int(input("người dùng cần tạo bao nhiêu số trong dãy Fibonacci "))
z=[1,1]
j=2
if a<=0:
    print("sai rồi nha méo có đâu")
elif a==1:
    print(z[0])
elif a==2:
    print(z[1])
elif a>2:
    while j != a:
        e = z[j - 1]
        e1 = z[j - 2]
        z.append(e + e1)
        j += 1
print(z)

#5
def hamlist(x):
    l=list(x)
    s=set(l)
    print(s)
r=str(input("nhap 1 chuỗi kí tự"))
hamlist(r)
"""
#p3 1
"""import random

def hamluat(r,r1,a,b,c):
    if (r == c) and (r1 == a):
        z = "thua"
    elif (r1 == c) and (r1 == a):
        z = "thắng"
    elif r == r1:
        z = "hòa"
    elif r > r1:
        z = "thắng"
    else:
        z = "thua"
    print("máy ra: ",r)
    print("bạn ra: ",r1)
    print("kết quả ")
    print("bạn: ",z)
def hoi(a1):
     a2=a1.lower()
def main():
    r = random.choice("abc")
    r1 = str(input("nhập kết quả: "))
    print(" a= kéo, b= búa, c= bao ")
    hamluat(r,r1,1,2,3)
    a = str(input("bạn có muốn chơi nửa yes or no "))
    a3=hoi(a)
    while a3 =="no":
        r1 = str(input("nhập kết quả: "))
        print(" a= kéo, b= búa, c= bao ")
        hamluat(r, r1, 1, 2, 3)
        a = str(input("bạn có muốn chơi nửa yes or no "))

if __name__=="__main__":
    main()

#2
def dayso(x,i):

    list = []

    while i != (x + 1):
        t = x % i
        if t == 0:
            list.append(i)
        i += 1
    print("ước của số ",list)
    return list

def main():
    x = int(input("xin bạn nhập số nguyên dương : "))
    i = 1
    t=dayso(x,i)
    a=len(t)
    if x==1:
        print("lỗi ")
    elif a==2:
        print("nó là số nguyên tố ", t)
    else:print("nó không phải là số nguyên tố ",t)
if __name__=="__main__":
    main()

#3
a=str(input("nhap chuỗi kí tự "))
a1=list(a)
a1.reverse()
a3="".join(a1)
print(a)
print(a1)
print(a3)
"""
#4
"""
import  random
def ssanh(a,a1):
    l = list(str(a))
    l1 = list(str(a1))
    i = 0
    w = 0
    h = 0
    while i != 4:
        if l1[i] == l[i]:
            w += 1
        else:
            h += 1
        i += 1
    print("số ẩn: ",a)
    print("số đoán ",a1)
    print(w, " cows", h, "bulls")

def main():
    a1 = random.randint(1000, 9999)
    a=int(input("nhập 4 số mà bạn đoán : "))
    while 999>a or a>10000:
        print("phai lớn hon 999 và nhỏ hơn 10000")
        a=int(input(" nhập lại 4 số mà bạn đoán :"))
    ssanh(a,a1)
    hoi=str(input(" chơi tiếp hay không yes or no"))
    while hoi!="no":
        a = int(input("nhập 4 số mà bạn đoán : "))
        while 999 > a or a > 10000:
            print("phai lớn hon 999 và nhỏ hơn 10000")
            a = int(input(" nhập lại 4 số mà bạn đoán :"))
        ssanh(a, a1)
        hoi = str(input(" chơi tiếp hay không yes or no "))
if __name__=="__main__":
    main()
"""
#5
"""
import random
stri=str("qwertyuiopasdfghjklmnbvcxz")
kitu=str("!@#$%^&*()_+<>?")
pss=stri.upper()
so=str("1234567890")
a=str(input("bạn có cần reset mật khẩu yes or no : "))
while a!="no":
    pss1 = random.choice(pss)
    pss2 = random.choice(stri)
    pss3 = random.choice(kitu)
    pss4 = random.choice(so)
    print(pss1 + pss2 + pss3 + pss4)
    a = str(input("bạn có cần reset mật khẩu yes or no : "))
"""

