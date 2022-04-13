import random

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




