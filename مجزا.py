def seperator(listtest1):
    zoj,fard=[],[]
    for i in listtest1:
        if int(i)%2==0:
            zoj.append(i)
        else:
            fard.append(i)
    print(f"({zoj},{fard})")
seperator(list(input().split()))