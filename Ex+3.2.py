
# coding: utf-8

# In[176]:

import numpy as np
from scipy import interpolate
from scipy import optimize
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import pylab 

file = np.loadtxt("3.2.txt") 
x = file[:len(file),0]
y = file[:len(file),1]
plt.scatter(x,y)

def f(x,A,B,C,D):
      return A*x**3 + B*x*x + C*x + D
A, B, C, D = optimize.curve_fit(f, x, y)[0]

def function(x):
      return A*x**3 + B*x*x + C*x + D

y = A*x**3 + B*x*x + C*x + D   
plt.plot(x, y,"Orange")

print "A",A,"B",B,"C",C,"D",D
print "===================="
print "Function: y =",A,"x**3 +",B,"*x*x +",C,"*x +",D
print "-----------------"

pylab.xlim([-4,4])
pylab.ylim([-250,250])

root = fsolve(function,[-10])  #the function which can get root
print "The root is ",root

plt.xlabel('The x value')
plt.ylabel('The y value')
plt.legend(('Polynomial function', 'txt value'),loc='best')
plt.plot([root], [0], marker='^', markersize=6, color="red")

plt.show()





# In[ ]:



