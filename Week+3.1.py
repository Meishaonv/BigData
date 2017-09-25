
# coding: utf-8

# In[86]:

import numpy as np                                            #1)
input = np.loadtxt("matrix.txt",dtype = 'i',delimiter  = ',')   #2)
print "The matrix is",'\n',(input)
#Split the metrix
lastcolumn = input[:,3]                                       #3) 
print 'Last column:','\n',lastcolumn
otherpart = input[:3,0:3]                                     #3)
print 'Rest metrax is ', '\n',otherpart
#Get solution
x = np.linalg.solve(otherpart,lastcolumn)                     #4)
print "The result is :", '\n',x 
np.allclose(np.dot(otherpart, x), lastcolumn)                 #5)


# In[ ]:




# In[ ]:




# In[ ]:



