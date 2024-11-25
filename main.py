# def p2(no):
#     if no<=0:
#         return False
#     return (no&(no-1)==0)

# n=int(input("Enter a number:"))

# if p2(n):
#     print("It is power of2")
    
# else:
#     print("It is not power of 2")
    






# def p4(no):
#     count=0
#     if (no&(~(no&(no-1)))):
#         while (no>1):
#             no=no>>1
#             count+=1
#         if (count%2==0):
#             return True
#         else:
#             return False
        
# num=int(input("Enter a number:"))

# if(p4(num)):
#     print("It is power of 4")
# else:
#     print("It is not power of 4")
            
            
            
            
            
            

def po(x,y):
    result=1
    while y>0:
        if y%2==0:
            x=x*x
            y>>=1
        else:
            result=result*x
            y-=1
    return result

x=int(input("Enter number: "))
y=int(input("Enter power: "))

print(po(x,y))