import numpy as np

#1. Matrix Dimensions

#1.1
A = np.array([[1,2,3],[2,7,4]])
print A.shape
#(2,3)

#1.2
B = np.array([[1,-1],[0,1]])
print B.shape
#(2,2)

#1.3
C = np.array([[5,-1],[9,1],[6,0]])
print C.shape
#(3,2)

#1.4
D = np.array([[3,-2,-1],[1,2,3]])
print D.shape
#(2,3)

#1.5
u = np.array([[6,2,-3,5]])
print u.shape
#(1,4)

#1.6
w = np.array([[1],[8],[0],[5]])
print w.shape
#(4,1)

#2. Vector Operations
v = np.array([[3,5,-1,4]])
#2.1
print u + v
#[9,7,-4,9]

#2.2
print u - v
#[3,-3,-2,1]

#2.3
print 6*u
#[36,12,-18,30]

#2.4
print u * v
#[18,10,3,20]

#2.5
print np.linalg.norm(u)
#8.6023

#3. Matrix Operations
A = np.matrix('1,2,3; 2,7,4')
B = np.matrix('1,-1;0,1')
C = np.matrix('5,-1;9,1;6,0')
D = np.matrix('3,-2,-1;1,2,3')

#3.1
print A + C
#not defined

#3.2
print A - C.transpose()
#[[-4,-7,-3],[3,6,4]]

#3.3
print C.transpose() + 3*D
#[[14,3,3],[2,7,9]]

#3.4
print np.dot(B,A)
#[[-1,-5,-1],[2,7,4]]

#3.5
print np.dot(B,A.transpose())
#not defined

#3.6
print np.dot(B,C)
#not defined

#3.7
print np.dot(C,B)
#[[5,-6],[9,-8],[6,-6]]

#3.8
print B**4
#[[1,-4],[0,1]]

#3.9
print np.dot(A,A.transpose())
#[[14,28],[28,69]]

#3.10
print np.dot(D.transpose(),D)
#[[10,-4,0],[-4,8,8],[0,8,10]]
