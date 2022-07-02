#7월 2일 2022년 
#gcd(60,28) 

def gcd (a,b):
    alist=[] 
    blist=[]
    for i in range(1,a):
        if a%i==0:
            alist.append(i)
    for i in range(1,b):
        if b%i==0:
            blist.append(i)
    print(a,"의 약수:",alist)
    print(b,"의 약수:",blist)
    
    #a의 약수중 큰 값 부터 비교 
    for i in range (len(alist)-1,0,-1):
        if alist[i] in blist: # in 연산자 
            return alist[i]
    return 1
print("최대공약수",gcd(60,28))
print()

####################################################
#두번쨰 방법 
def max(a,b):
    alist=[] 
    blist=[]
    for i in range(1,a):
        if a%i==0:
            alist.append(i)
    print(a,"의 약수",alist)
    
    for i in range(len(alist)-1,0,-1):
        if b%alist[i]==0:
            return alist[i]
    return 1 
print("최대공약수:",max(60,28))
print()

####################################################
#유클리드 알고리즘 이용 
def gcd(a,b): #a>b 
    while b!=0:
        r=a%b
        a=b
        b=r 
    return a 
print(gcd(60,28))


def gcd(a,b):  
    if b>a:
        a,b=b,a
        
    while b!=0:
        r=a%b
        a=b
        b=r 
    return a 
print(gcd(60,28))




    
 
