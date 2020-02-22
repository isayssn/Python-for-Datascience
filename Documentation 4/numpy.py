
import numpy as np

mul=np.array([[5,4,6],[7,8,9],[10,11,12]])
#Check the shape (rows and columns of the array)
print(mul.shape)
#Create an evenly spaced array between 1 and 60 with a difference of 2
dif=np.arange(1,60,2)
#Reshape the above array into a desired shape
dif.reshape(10,3)
#Generate an evenly spaced list between the interval 1 and 8.
gen = np.linspace(1,8,40)
#change the shape of the array in place
gen.resize(10,4)
#Create an array with all elements as ones
onarr = np.ones((4,4))
#Create an array filled with zeros.
zearr = np.zeros((4,4))
#Create a diagonal matrix with diagonal values = 1
dm = np.eye(3)
#Extract only diagonal values from an array.
diag = np.diag(dm)
#Create an array consisting of repeating list
relist = np.array([1,2,3]*7)
#repeat each element of array n number of times using repeat function.
rep = np.repeat([1,2,3],3)
#Generate two arrays of desired shape filled with random values between 0 and 1.
relist = np.random.rand(2,3)
print(relist)
de = np.random.rand(2,3)
print(de)
#Stack the above two arrays created vertically
st = np.vstack([de,relist])
#stack them horizontally.
sh = np.hstack([de,relist])

#/////////////////////////////////////////////////////////////////////////////
r1 = np.random.rand(2,2)
r2 = np.random.rand(2,2)
print(r1)
print(r2)
#element wise addition.
r3 = r1+ r2
r4 = r1 - r2
r5 = r1**3
#dot product of the two arrays r1 and r2.1
r6 = r1.dot(r2)
#create a new array and transpose it.
sh = np.array([[1,2],[3,4]])
trans = sh.T
#check the datatype of elements in the array.
print(sh.dtype)
#Change the datatype of the array.
rs = sh.astype('f')
rs.dtype
#mathematical functions in an array
c = np.array([1,2,3,4,5])
c.sum()
#Maximum of the elements of an array.
c.max()
#Mean of the elements of the array
c.mean()
#index of the maximum value of the array.
c.argmax()
c.argmin()
#array consisting of square of first ten whole numbers
dim = np.arange(10)**2
dim[2]
dim[1:5]
dim[-1:]

dim[1:10:2] #dim[start:stop:stepsize]

#multidimensional array
en = np.arange(36)
en.resize(6,6)
en[1,2]
en[1, 2:6]
en[:2,:-1]
#Select values from array greater than 20
en[en>20]
#Assign value of the array elements as 20 if the element value is greater than 20.
en[en>20] = 20
#copy an array onto another variable
fun = en.copy()
#array with a set of random integers between 1 and 10. Specify the array to be of shape 4*4
gom = np.random.randint(1,10,(4,4))
print(gom)














