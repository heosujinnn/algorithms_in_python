#7월 22일 (제발 열심히 할래요)
# 최대 공약수 , 최소 공배수 문제  

#6과 45의 최소공배수 문제 
a=45 #최소 배수 
n=0 #약수 
while True:
    if(a%6==0)and(a%45==0):
        n=a 
        break 
    a+=1
print(a)

#42와 120의 최대공약수 
a=42 
n=0 
while True:
    if(42%a==0)and(120%a==0):
        n=a 
        break 
    a-=1 
print(a)

#최대 공약수를 구하는 유클리드 알고리즘 
def gcd(a,b): #a>b 
    while b!=0:
        r=a%b 
        a=b 
        b=r 
    return a 
print(gcd(60,28))