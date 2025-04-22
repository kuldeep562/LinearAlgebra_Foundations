#fasle position method
#f(x):x3-9x+1=0


import math
def f(x):
    a=x*x*x -9*x + 1
    return(a)

a=float(input("Enter your first point : "))
b=float(input("Enter your second point : "))
if f(a)*f(b)>0:
    print("Roots doesn't exist between a =",a,"and b =",b)
else:    
    E=float(input("Enter your epsloan : "))
    c=0
    print("TABLUAR FORM : ")
    print("\ta\t\tf(a)\t\tb\t\tf(b)\t\tc\t\tf(c)\t\tdifference")
    print("*********************************************************************************************************************")
    print("*********************************************************************************************************************")
    diff=1
    e=0
    while(True):
        c=(a*f(b)-b*f(a))/(f(b)-f(a))
        diff=abs(c-e)
        print("\t{:.5f}".format(a),"\t{:.5f}".format(f(a)),"\t{:.5f}".format(b),
              "\t{:.5f}".format(f(b)),"\t{:.5f}".format(c),"\t{:.5f}".format(f(c)),"\t{:.5f}".format(diff))
        if f(a)*f(c)<0:
            b=c
        else:
            a=c    
        if diff<E:
            break;
        else:
            e=c
            continue;
    print("Root between given interval is : {:.5f}".format(c))       
 

