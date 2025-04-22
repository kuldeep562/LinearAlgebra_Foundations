
#Newton raphson method
#f: x^3 -5x +1

import math
def f(x):
    a=x*x*x -5*x + 1
    return(a)
def df(x):
    a=3*x**2 -5
    return(a)
print("fn :  x**3 - 5*x + 1")
print("derivative :  3*x**2 - 5")
x1=float(input("Enter your point : "))
E=float(input("Enter your epsloan : "))
print("TABLUAR FORM : ")
print("\t x1\t\t f(x1)\t\t f'(x1)\t\t x2\t\t difference")
print("*********************************************************************************************************************")
print("*********************************************************************************************************************")
diff=E+1
while(True):
    if df(x1)==0:
        print("Derivative is zero.")
        break
    else:    
        x2=x1-f(x1)/df(x1)
        diff = abs(x2-x1)
        print("\t{:.5f}".format(x1),"\t{:.5f}".format(f(x1)),"\t{:.5f}".format(df(x1)),"\t{:.5f}".format(x2),"\t{:.5f}".format(diff))
        x1=x2
        if diff<E:
            print("Root between given interval is : {:.5f}".format(x2))
            break
        else:    
            continue

