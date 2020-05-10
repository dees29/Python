# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 16:06:23 2020

@author: Admin
"""

import theano
from theano import tensor

#declare two symbolic floating-point scalars

a=tensor.dscalar()
b=tensor.dscalar()

#creating simple symbolic expression 

c=a+b

#convert expression into callable object
f=theano.function([a,b],c)

#binding 1.5 to a and 2.5 to b and evaluating c

result=f(1.5,2.5)

print(result) 