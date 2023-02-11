def masahat(listtest1):
    for i in listtest1:
        if i=="square":
            return(int(input())**2)
            continue
        elif i=="circle":
            num=3.14*(int(input())**2)
            return(num)
            continue
        elif i=="triangle":
            return(int(input())*int(input())*1/2)
            continue
        elif i=="rectangle":
            return(int(input())*int(input()))
            continue
print(masahat(list(input().split())))