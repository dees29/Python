import numpy as np
a=np.array([[3,1,-5],[1,-2,3],[7,5,-3]])
b=np.array([13,13,26])
c=np.linalg.solve(a,b)
print(c)
