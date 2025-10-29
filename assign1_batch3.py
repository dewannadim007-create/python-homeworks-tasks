# 1//Implement the sigmoid activation function and determine the activation value of Z,
#  where Z = last 2 digit of your Student ID mod 5 A sigmoid function can be expressed with the
#  following equation (Z) = 11+e-Z Here, e = Epsilon. 
# [You can use NumPy or Pytorch] id:2022100000084 % 5 = 4

import numpy as np
z= 84 % 5
divisor = 1 + np.exp(-z)
result= (1/divisor)
print (result)

# 2// Consider the array below and slice it such that the resultant array contains elements
#  only with even row indices and odd column indices of the given array. 
# [You must use PyTorch and Negative indexing] 
# [ [14, 8, 5, 17], [13, 13, 19, 3], [15, 17, 9, 2], [12, 8, 18, 16] ]

import torch
t = torch.Tensor([ [14, 8, 5, 17],
[13, 13, 19, 3],
[15, 17, 9, 2],
[12, 8, 18, 16] ])

print(t[-3::2, -4::2])

# 3// Consider the 2 array below and do do some arithmetic operations: a = [ [14, 8, 5, 17], [13, 13, 19, 3], [12, 8, 18, 16] ] b = shape(3,4)
#For b array, use a random function to create an array. The range of random values is the last 2 digits of your Student ID.
#  Perform the following operations: i.) a+b  ii.) a-b  iii.) ab [Element wise multiplication] iv.)  a(Transpose of b) [Matrix multiplication]
#  v.) Transpose of (iv Question) / last 2 digits of your Student ID [Only Matrix Multiplication]; [You must use PyTorch]

a = torch.Tensor([ [14, 8, 5, 17],
[13, 13, 19, 3],
[12, 8, 18, 16] ])
b= torch.randint(0,85,(3,4)) #last 2 digit= 84
c= b.t()

print(torch.add (a,b)) #i
print(torch.sub (a,b)) #ii

d= a.mul(b)
print (d) #iii

e= torch.mm(a,c)
print (e) #iv


print (torch.divide(e.t(),84 ) ) #v


# I always get data type related error message . but the formula seems ok
# too me since i followed the base code structure from the provided notebook. how to fix