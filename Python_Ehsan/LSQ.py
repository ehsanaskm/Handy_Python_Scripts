import numpy as np
import matplotlib.pyplot as plt

x=np.array([-2,-1,2,3,4])
y=np.array([4,3,4,1,2])

x2=x**2

xy=x * y

xi=sum(x)
yi=sum(y)

xi2=sum(x2)
xiyi=sum(xy)


A=np.matrix([[len(x),xi],[xi,xi2]])

B=np.matrix([[yi],[xiyi]])


print (np.linalg.inv(A)*B)
