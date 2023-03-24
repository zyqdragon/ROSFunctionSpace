import numpy as np
a=np.array([[0, 1,2],
       [3, 4, 5],
       [6, 7, 8]])
b = a*2
print("----b=",b)

c=np.array([1,3,4])
c=c.reshape(1,3)


t1=np.concatenate((a,b),axis=1)
print("----t1=",t1)
t2=np.concatenate((a,b),axis=0)
print("----t2=",t2)

t3=np.concatenate((a,c),axis=0)
print("----t3=",t3)




