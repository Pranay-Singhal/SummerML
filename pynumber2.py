#!/bin/usr/python3

import numpy as np

start=int(input("Enter starting no. between 100-125 excluding 125:- ")) 
if start in range(100,125): 
	a=np.arange(start,200,5) 
	b=a[0:16].reshape(8,2) 
	print(b) 
else: 
	print("Wrong entry..your no. exceeds the limit of array b/w 100 to 200")
