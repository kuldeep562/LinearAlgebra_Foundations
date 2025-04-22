# Q3 FIND THE TRANSPOSE OF MATRICES

def trans(r,c,mat):
    mat1=[]
    for i in range(r):
        m=[]
        for j in range(c):
            ele=mat[j][i]
            m.append(ele)
        mat1.append(m)
    return (prin(r,c,mat1))   

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
            
r1=int(input("Enter row of matices : "))
c1=int(input("Enter colmn of matrices : "))
m1=mat_ent(r1,c1)
prin(r1,c1,m1)
print("Transpose of your matrices : ")
trans(r1,c1,m1)
     