def find(num1,num2,num3):
    if(int(num1)!=1 and int(num2)!=1 and int(num3)!=1):
        print(1)
    elif(int(num1)!=2 and int(num2)!=2 and int(num3)!=2):
        print(2)
    elif(int(num1)!=3 and int(num2)!=3 and int(num3)!=3):
        print(3)
    elif(int(num1)!=4 and int(num2)!=4 and int(num3)!=4):
        print(4)
listtest1=list(input().split())
find(listtest1[0],listtest1[1],listtest1[2])