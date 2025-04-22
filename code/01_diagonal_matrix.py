# Q1) FIND TRACE AND DIAGONAL OF MATRICE


def prin(r,c,mat):
    print("Your matrice is : ")
    for i in range(r):
            for j in range(c):
                print("\t",mat[i][j],end='')
            print()
def dia(mat,r):
    dia=[]
    for i in range(r):
        dia.append(mat[i][i])
    return (dia)

def trac(dia):
    for i in dia:
        tra=tra + i
    return (tra)
    
    
while(True):
    r=int(input("Enter the number of rows : "))
    c=int(input("Enter the number of columns : "))
    if (r!=c):
        print("rows and columns are not equal.")
        continue;
    else :
        print("Enter the element row wise : ")
        mat=[]
        for i in range(r):
            m=[]
            for j in range(c):
                ele=int(input("Enter the element : "))
                m.append(ele)
            mat.append(m)
        while(True):
            print("\n\n-----------------------------------------------")
            print("Select the following options you want to do :\n")
            print("1-> Printing of matrices ")
            print("2-> Printing of diagonal ")
            print("3-> Finding trace ")
            print("4-> EXIT ")
            print("-----------------------------------------------\n")
            choice=int(input("\nEnter your choice : "))
            if (choice==1):
                prin(r,c,mat)
                continue;
            elif (choice==2):
                print("\nDiagonal of your matrice is : ",dia(mat,r))
                continue;
            elif (choice==3):
                print("Trace of your matrice is : ",tra)
                continue;
            elif (choice==4):
                print("\nThank you.")
                break;
            else :
                print("\nEnter valid choice ")
                continue;
        break;      
