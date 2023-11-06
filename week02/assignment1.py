import numpy as np
import pprint
import timeit
import matplotlib.pyplot as plt 
# Activity 1: 
# Create an array using 
# arange, linspace, ones, zeros, eye, and diag. 
# Use the functions len (), and NumPy.shape() on these arrays.
aranageArray=np.arange(1,100,7)
linspaceArray=np.linspace(0,2,11)
onesArray=np.ones((2,4))
zerosArray=np.zeros((3,3))
eyeArray=np.eye(5)
diagArray=np.diag(np.array([1,3,5,7]))
shape=np.shape(diagArray)
print("Activity 1")
print("\n")
pprint.pprint(aranageArray)
pprint.pprint(linspaceArray)
pprint.pprint(onesArray)
pprint.pprint(zerosArray)
pprint.pprint(eyeArray)
print("\n") 
print("Using len() function:")
print(f"Length of aranageArray: {len(aranageArray)}")
print(f"Length of linspaceArray: {len(linspaceArray)}")
print(f"Length of onesArray: {len(onesArray)}")
print(f"Length of zerosArray: {len(zerosArray)}")
print(f"Length of eyeArray: {len(eyeArray)}")
print(f"Length of diagArray: {len(diagArray)}")

print("\nUsing np.shape() function:")
print(f"Shape of aranageArray: {np.shape(aranageArray)}")
print(f"Shape of linspaceArray: {np.shape(linspaceArray)}")
print(f"Shape of onesArray: {np.shape(onesArray)}")
print(f"Shape of zerosArray: {np.shape(zerosArray)}")
print(f"Shape of eyeArray: {np.shape(eyeArray)}")
print(f"Shape of diagArray: {np.shape(diagArray)}")
print("-------------------------------------------")
# Activity 2: 
# Create an array using random numbers.
# Try setting the seed before creating an array with random values.
print("Activity 2")
print("\n")
random_array_without_seed=np.random.rand(5)
print("Array with random numbers (without seed):")
print(random_array_without_seed)

np.random.seed(0)
random_array_with_seed = np.random.rand(5) 
print("\nArray with random numbers (with seed):")
print(random_array_with_seed)
print("-------------------------------------------")
# Activity 3:
# Create an array ‘a’ and use the function timeit to time a**2 and a+1.
print("Activity 3")
print("\n")
setupL='''
import numpy as np
a=np.arange(10000)
'''
time_square = timeit.timeit("[a**2]", setupL,number =100000)
print(f"Time taken for a**2: {time_square:.8f} seconds")

time_add = timeit.timeit("a + 1", setupL, number=10000)
print(f"Time taken for a + 1: {time_add:.8f} seconds")
print("-------------------------------------------")
# Activity 4:
# Create a simple two-dimensional array.
# How about odd numbers counting backward on the first row,
# and even numbers on the second? (Indexing and slicing)
print("Activity 4")
print("\n")
odd_backward=np.arange(9,0,-2)
even_numbers=np.arange(2,11,2)
two_dimensional_array=np.vstack([odd_backward,even_numbers])
print("Two-dimensional array:")
print(two_dimensional_array)
print("\n")
# Get the first row
print("\nFirst row:")
print(two_dimensional_array[0, :])

# Get the second row
print("\nSecond row:")
print(two_dimensional_array[1, :])

# Get the first column
print("\nFirst column:")
print(two_dimensional_array[:, 0])

# Get a specific element (e.g., second row, third column)
print("\nSpecific element (second row, third column):")
print(two_dimensional_array[1, 2])

print("-------------------------------------------")
# Activity 5:
# Create a multidimensional array and use functions like reshape and transposition.
# Compute statistics like std, mean and median across the different axis.

print("Activity 5")
print("\n")

original_array = np.array([[1, 2, 3, 4],
                           [5, 6, 7, 8],
                           [9, 10, 11, 12]])

print("Original Array:")
print(original_array)
reshaped_array = original_array.reshape((2, 6))
print("\nReshaped Array (2x6):")
print(reshaped_array)
transposed_array = original_array.T
print("\nTransposed Array:")
print(transposed_array)
print("\nStatistics for the entire original array:")
print(f"Mean: {np.mean(original_array)}")
print(f"Standard Deviation: {np.std(original_array)}")
print(f"Median: {np.median(original_array)}")

print("\nStatistics across rows (axis=0):")
print(f"Mean: {np.mean(original_array, axis=0)}")
print(f"Standard Deviation: {np.std(original_array, axis=0)}")
print(f"Median: {np.median(original_array, axis=0)}")

print("\nStatistics across columns (axis=-1):")
print(f"Mean: {np.mean(original_array, axis=-1)}")
print(f"Standard Deviation: {np.std(original_array, axis=-1)}")
print(f"Median: {np.median(original_array, axis=-1)}")

print("-------------------------------------------")
# Matplotlib Activities:
# Activity 1: Create a file in idlelib to generate a line and save it as test_matplotlib.
# With ref to file test_matplotlib. Plot the figures with a solid line dotted and ‘-‘and save them as Fig 1, 2, and 3.
x = np.linspace(0, 10, 100)
y = x * 2

# Plot with a solid line and save as Fig 1
plt.figure()
plt.plot(x, y, '-')
plt.title('Solid Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('Fig_1.png')
plt.show()

# Plot with a dotted line and save as Fig 2
plt.figure()
plt.plot(x, y, ':')
plt.title('Dotted Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('Fig_2.png')  
plt.show()

# Plot with '-' and save as Fig 3
plt.figure()
plt.plot(x, y, '--')
plt.title('Dash Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('Fig_3.png')
plt.show()

# Create a random array
random_array = np.random.rand(30, 30)

# Plot the image with a 'viridis' colormap and save as Fig 1
plt.figure()
plt.imshow(random_array, cmap='viridis')
plt.title('Random Array with Viridis Colormap')
plt.colorbar()
plt.savefig('test_matplotlib_img1.png')  # This will save the figure as Fig_1.png in the current directory
plt.show()

# Plot the image with a 'plasma' colormap and save as Fig 2
plt.figure()
plt.imshow(random_array, cmap='plasma')
plt.title('Random Array with Plasma Colormap')
plt.colorbar()
plt.savefig('test_matplotlib_img2.png')  # This will save the figure as Fig_2.png in the current directory
plt.show()

# notes
# https://numpy.org/doc/stable/reference/generated/numpy.linspace.html
