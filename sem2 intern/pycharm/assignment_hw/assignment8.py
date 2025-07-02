import numpy as np


# question 1.)......................................
a1 = np.empty((4,2))
print("\nempty array1\n",a1)
print("\ndefault datatype\n",a1.dtype)        #deffault float64 hi hoga


a2 =np.full((4,2),"50")
a3 =np.full((4,2),50)

print("\nfull array2 with string\n",a2)
print("\ndefault datatype\n",a2.dtype)     #U2  matlab unicode string with 4 char


print("\nfull array3 with int\n",a3)                #yha par int hai
print("\ndefault datatype\n",a3.dtype)

a4 = np.zeros((3,5))
print("\nfull array4 with zeros\n",a4)
print("\ndefault datatype\n",a4.dtype)

a5 = np.ones((4,3,2))
print("\nfull array4 with ones\n",a5)
print("\ndefault datatype\n",a5.dtype)
# ......................................................





# QUESTION 2.).................................
a6 = np.array([[[2,3,3],[4,5,6],[6,7,7]]])
print("\n3-D array\n",a6)
print("\nshape\n",a6.shape)

#QUESTION 3.)..................................
#METHOD 1
vec = np.zeros(10)
print("\nnull vextor\n",vec)
vec[5]=6            #6th elemetn == index 5
print(vec)

#METHOD 2  WORKS ONLY WHEN M#1 IS COMMENT VARNA WHI PRINT HOGA
vec2 = np.empty(10)
print("\nempty call\n",vec2)
print(vec2.dtype)               #float64 hoga always default
vec2[5]=6            #6th elemetn == index 5
print(vec2)


#QUESTION 4.)..................................
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("\n3-D array\n",arr)
print("shape",arr.shape)


# print("\nLast element \n",arr[-1][-1][-1])            #start wali index zero se start
                                                        #reverse wali -1 se start
# for i in range(3):                ye bhi kuch bna
#     for z in range(2):
#         for p in range(2):
#             print(arr[-p][-z][-i])
print("element s from last:")
for z in range(1,3):
    for p in range(1,3):
        for i in range(1,4):
            print(arr[-z][-p][-i])

reverse = np.zeros(arr.shape)
for z in range(reverse.shape[0]):
    for p in range(2):
        for i in range(3):
            reverse[z][p][i] = arr[-(z+1)][-(p+1)][-(i+1)]
print(reverse)


'''find another way ??/by slicing also '''

#QUESTION 5.)..................................
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("\ntype original\n",arr,arr.dtype)

new2 = np.array(arr,dtype=float)
print("\nfloat type convert\n",new2)
