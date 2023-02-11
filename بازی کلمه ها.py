def hoora(stringtest):
    listtest1=list(stringtest.split())
    listtest2,listtest3=[],[]
    print(listtest1)
    for i in listtest1:
        p=0
        for j in i:
            if 65<=ord(j)<=90 or 97<=ord(j)<=122:
                pass
            else:
                p+=1
        if p>=(len(i)/2):
            listtest2.append(i)
    for i in listtest2:
        listtest1.remove(i)
    for i in listtest1:
        p=0
        for j in i:
            if 65<=ord(j)<=90 or 97<=ord(j)<=122:
                pass
            else:
                listtest3.append(j)
        for t in listtest3:
            if t in i:
                inn=i.translate({ord(t): ""})
                print(inn)
            else:
                print(i)
                p+=1
        if p==0:
            print(inn)
        else:
            print(i)


    print(" ".join(listtest1))
hoora(input())