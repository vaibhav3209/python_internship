import numpy as np
import matplotlib.pyplot as plt

#QUESTION 1.)............................................
arr = np.array([[6, -8, 73, -110], [np.nan, -8, 0, 94]])
print("\nGIVEN ARRAY:\n",arr)
arr = np.nan_to_num(arr,nan =0)
print("\nCORRECTED ARRAY: \n",arr)

arr[:,[0,1,2]] = arr[:,[2,1,0]]
print("\nINTERCHANGED ARRAY\n",arr)

arr[[0,1],[2]] = arr[[1,0],[2]]
print("\nchanged 6 and 0 zero only\n",arr)



#QUESTION 2.)............................................
orig = np.arange(1,19).reshape(2,3,3)
print("\nORIGINAL AXES:(2,3,3) \n",orig)

ax = np.moveaxis(orig,0,1)
print("\nchanged to (3, 2, 3)\n",ax)
print(ax.shape)

ax = np.moveaxis(orig,0,2)          #ye transpose k barabar hai
print("\nchanged to (3, 3, 2)\n",ax)
print(ax.shape)

ax = np.moveaxis(orig,1,0)
print("\nchanged to (3, 2, 3) same as previous\n",ax)
print(ax.shape)



#QUESTION 3.)............................................
arr2 = np.array([[np.nan, 5, 15, -110], [0, np.nan, 0, 94],[10,15,20,30]])
res = np.mean(arr2,axis =0)
# res = np.nan_to_num(arr2,nan=np.mean(arr2,axis =0))
print("\nmean replace\n",res)





#QUESTION 4.)............................................
arr = np.array([[1, -2, 3], [-4, 5, -6]])
arr[arr < 0] = 0  # Replace all negative values with 0

print("\nchange array\n",arr)



#QUESTION 5,6,7.)............................................
a = np.array([3, 4])
b = np.array([1, 0])
avg = (a + b) / 2        #har column k  element ko lega
print("Average of  arrays:\n", avg)          #result is 1_d array1x2



# mode median of 2-d arrays
a =np.arange(5,50,5).reshape(3,3)
print("\nFirst array\n",a)

b =np.arange(10,100,10).reshape(3,3)
print("\nsecond array\n",b)

median_cols = np.median(a, axis=0)
print(f"Median along columns of a : {median_cols}")

median_rows = np.median(b, axis=1)
print(f"Median along rows of b: {median_rows}")


#mode
flat = a.flatten()
print("\nto calculate mode flatten the array:\n",flat)
unique_elements, count = np.unique(flat, return_counts=True)
print(f"\nunique elements: {unique_elements}\n\ntheir count:    {count}\n")

max_count = np.max(count)
print("\ncount values that appear max:\n",max_count)

mode = unique_elements[count == max_count]
# mode = [True True True True]  aise banega
print("\nvalues of mode are(cann be more than 1):\n",mode)


#QUESTION 8.)............................................
# x-2y+3z=9
# -x+3y-z=-6
# 2x-5y+5z=17

coeff = np.array([[1,-2,3],[-1,3,-1],[2,-5,5]])
const = np.array([9,-6,17])

result = np.linalg.solve(coeff,const)
print("\nresult by .solve()\n",result)


#MATRIX INVERSION
coeff_inv = np.linalg.inv(coeff)
print("\ninvesse array\n",coeff_inv)
res = np.dot(coeff_inv,const)
print("\nfinal ans by matrix inversion\n",res)

#QUESTION 9.)............................................
subject_sem1 = ['math1','chem','cve','bme','hv']
values_sem1 = [95,90,96,80,85]
grades_sem1 = ['A++','A','A++','B','A']


subject_sem2 = ['math2','cos','bee','phy','pps']
values_sem2 = [86,84,77,90,82]
grades_sem2 = ['A+','A','B+',"A+",'A']

plt.bar(subject_sem1,values_sem1,color = "red")
plt.bar(subject_sem2,values_sem2,color = "blue")

plt.title('sem1 grades')
plt.xlabel("subjects-->>  -->>>")
plt.ylabel("marks-->>  -->>")

plt.show()