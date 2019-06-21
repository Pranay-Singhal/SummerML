mport numpy as np 
import random

rows=int(input("enter no. of rows:"))
columns=int(input("enter no. of columns:")) 

x=np.random.rand(rows,columns)
np.savetext("file1.txt",x)
