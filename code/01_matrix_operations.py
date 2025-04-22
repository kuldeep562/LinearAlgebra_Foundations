
# Q-4. Write a generalized menu based program to perform the following operations without using numpy functions.


def mat_ent(r,c):
    print()
    mat=[]
    for i in range(r):
        m=[]
        for j in range(c):
            ele=int(input("Enter the element : "))
            m.append(ele)
        mat.append(m)
    return(mat)

def prin(r,c,mat):
    print("Your matrice is : ")
    for i in range(r):
            for j in range(c):
                print("\t",mat[i][j],end='')
            print()

def multi(row1,col2,col1,mat1,mat2):
    mat3=[]
    for i in range(row1):
        m=[]
        for j in range(col2):
            sum=0
            for k in range(col1):
                c=mat1[i][k]*mat2[k][j]
                sum=sum + c
            m.append(sum)
        mat3.append(m)
       
    return (prin(row1,col2,mat3)) 
        
def scal_multi(r,c,mat,s):
    matscale=[]
    for i in range(r):
        mat1=[]
        for j  in range(c):
            ele=mat[i][j]*s
            mat1.append(ele)
        matscale.append(mat1)    
    return(prin(r,c,matscale))

r=int(input("Enter the number of rows : "))
c=int(input("Enter the number of columns : "))
mat1=mat_ent(r,c)

while(True):
        print("\n\n-----------------------------------------------")
        print("Select the following options you want to do :\n")
        print("1-> Re-enter your matrices")
        print("2-> PRINTING of matrices ")
        print("3-> SCALAER MATRICES ")
        print("4-> MATRIX MULTIPLICATION ")
        print("5-> EXIT ")
        print("-----------------------------------------------\n")
        choice=int(input("\nEnter your choice : "))
        if(choice==1):
            mat1=mat_ent(r,c)
        if (choice==2):
            prin(r,c,mat1)
            continue;
        elif (choice==3):
            s=int(input("Enter YOUR REAL SCALAR : "))
            scal_multi(r,c,mat1,s)
            continue;
        elif (choice==4):
            print("Enter second matrices : ")
            r1=int(input("Enter the rows of second matrices : "))
            c1=int(input("Enter the columns of second matrices : "))
            mat2=mat_ent(r1,c1)
            if (c==r1):
                print("Multiplication of both matrices : ")
                multi(r,c1,c,mat1,mat2)
            else:
                print("maltiplication not possible.")
            continue;    

        elif (choice==5):
            print("\nThank you.")
            break;
        else :
            print("\nEnter valid choice ")
            continue;
