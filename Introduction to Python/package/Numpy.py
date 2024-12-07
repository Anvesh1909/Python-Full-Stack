import numpy as np 
print("==Numpy==")
print(dir(np))
print("=========")



# List to array
import numpy as np 

res = np.array([1001,10229,12972,12881])
print(res)

print(res.ndim)

print(type(res))




# hetrogeneous objects
import numpy as np 

res = np.array([1001,"ANVESH","buNNNY",12881])
print(res)

print(res.ndim)


# indexing
import numpy as np 
res = np.array([1001,"ANVESH","buNNNY",12881])

print(res[0],res[2])
print(res[-1],res[-3])




# slicing
import numpy as np 
res = np.array([1001,"ANVESH","buNNNY",12881])
print(res[2:])






# n dimentional data
import numpy as np
L = [ [1,2,3],
      [4,5,6],
      [7,8,9]  ]

res = np.array(L)
print(res)
print("dimentionsa",res.ndim)

print("res(0,2)",res[0][2])



# Shape
import numpy as np
L = [ [1,2,3],
      [4,5,6],
      [7,8,9]  ]

res = np.array(L)


print(res.shape)

print(type(res[0]))





# reshape

import numpy as np

a1 = np.array([1,2,3,4,5,6,7,8,9])
print(a1)

a2 = a1.reshape(3,3)
print(a2)


for i in a2:
    for j in i:
        print(j,end="")
    print()



# ndim
import numpy as np

res = np.array([1,2,3,4,5,6,7,8,9],ndmin=4)
print(res)
print("Dimentions",res.ndim)

