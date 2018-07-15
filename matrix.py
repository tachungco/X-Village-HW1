import random

from copy import deepcopy

class Matrix:

    def __init__(self, nrows, ncols):
        """Construct a (nrows X ncols) matrix"""
        self.rows = int(nrows)
        self.cols = int(ncols)

    def add(self, m):
        """return a new Matrix object after summation"""
        if len(self.mtx) != len(m) or len(self.mtx[0]) != len(m[0]) :
            print('Matrix size should be in the same size !')
            return

        result = []
        for i in range(len(m)) :
            tmp = []
            for j in range(len(m[0])) :
                x = self.mtx[i][j] + m[i][j]
                tmp.append(x)  # row i
            result.append(tmp) # add row i into result
        for i in result :
            print(i)
 
    def sub(self, m):
        """return a new Matrix object after substraction"""
        if len(self.mtx) != len(m) or len(self.mtx[0]) != len(m[0]) :
            print('Matrix size should be in the same size !')
            return
        
        result = []
        for i in range(len(m)) :
            tmp =[]
            for j in range(len(m[0])) :
                x = self.mtx[i][j] - m[i][j]
                tmp.append(x)
            result.append(tmp)
        for i in result :
            print(i)

    def mul(self, m):
        """return a new Matrix object after multiplication"""
        self.stat = True
        if len(self.mtx) != len(m[0]) :
            print('ILLEGAL MATRIX !')
            self.stat = False
            return self.stat # for def transpose
        else :
            self.mul = []
            for i in range(len(self.mtx)) :
                tmp =[]
                for j in range(len(m[0])) :
                    y = 0
                    for k in range(len(m)) :
                        x = self.mtx[i][k] * m[k][j]
                        y = y + x  # y = mul[i][j]
                    tmp.append(y) # row i
                self.mul.append(tmp)

            for i in self.mul :
                print(i)

    def transpose(self):
        """return a new Matrix object after transpose"""
        if self.stat == False :  #  if mul illegal, neither do transpose
            print('ILLEGAL MATRIX !')
            return 

        self.tran =[]
        for i in range(len(self.mul[0])) : # rows of tran = cols of mul
            tmp = []
            for j in range(len(self.mul)) : # cols of tran = rows of mul
                tmp.append(self.mul[j][i]) # element of row i 
            self.tran.append(tmp) # add row i into tran
        for i in self.tran :
            print(i)

    def display(self):
        """Display the content in the matrix"""
        self.mtx =[]
        for i in range(1, self.rows+1) :
            tmp = []
            for j in range(1, self.cols+1) :
                a = random.randint(1,9)
                tmp.append(a)
            self.mtx.append(tmp)
        for i in self.mtx :
            print(i)
        return(self.mtx)

    
row_a = input("Enter A matrix's rows: ")
col_a = input("Enter A matrix's cols: ")
mtx_a = Matrix(row_a,col_a)
print('Matrix A', '(',row_a, ',', col_a, '):' )
A = mtx_a.display() # A = mtxA

row_b = input("Enter B matrix's rows: ")
col_b = input("Enter B matrix's cols: ")
mtx_b = Matrix(row_b,col_b)
print('Matrix B', '(',row_b, ',', col_b, '):' )
B = mtx_b.display()

print('========== A + B ==========')
mtx_a.add(B)

print('========== A - B ==========')
mtx_a.sub(B)

print('========== A * B ==========')
mtx_a.mul(B)

print('=== The transpose of A*B ===')
mtx_a.transpose()




