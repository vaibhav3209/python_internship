import numpy as np
#question1)......................
# arr1 = np.array(range(1,6,2))
#
# arr2 =  np.array([[12,13,14],[4,6,8],[5,5,5]])
# print(arr1.shape)
# print(arr1,"\n",arr2)
# arr1 = np.reshape(arr1,(1,3))
# res = np.concatenate(arr2,arr1)
# print(res)
#



#QUESTION2.)......
a = np.array([[12,13,14],[4,6,8],[5,5,5]])
print("2-d numpy array",a)
b = np.reshape(a,-1)
print("1d array from above 2-d array",b)


#question 3.............................
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("original array",arr)
print("\nREVERSE ARRAY\n",arr[-1::-1,-1::-1,-1::-1])

#question4)......................
