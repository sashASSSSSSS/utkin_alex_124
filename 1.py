a=input()
b=len(a)
x1=0
x2=0
for i in a:
    if i=="o":
        x1+=1
    if i=="x":
        x2+=1
def pp(x1, x2):
    if x1==x2:
        return True
    if x1!=x2:
        return False
print(pp(x1, x2))    
        
    
