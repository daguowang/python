import math

def quadratic(a,b,c):
    if(b*b-4*a*c)>0:
        x1=(-b+math.sqrt(b*b-4*a*c))/2*a
        x2=(-b-math.sqrt(b*b-4*a*c))/2*a
        return(x1,x2)
    elif(b*b-4*a*c)==0:
        x=(-b)/2*a
        return x
    else:
        return('此方程没有根')