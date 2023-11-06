import numpy as np

# 1. Generate a NumPy array with 50 elements
a_hoikit_fan = np.arange(50)
print(a_hoikit_fan)

# 2. Display Median, mean and std dev for array a_hoikit_fan
print("Median:", np.median(a_hoikit_fan))
print("Mean:", np.mean(a_hoikit_fan))
print("Std Dev:", np.std(a_hoikit_fan))

# 3. Reshape it 5x10 and 10x5
b_hoikit_fan = a_hoikit_fan.reshape(5, 10)
print(b_hoikit_fan)

c_hoikit_fan = a_hoikit_fan.reshape(10, 5)
print(c_hoikit_fan)

# 4. Display element [3,7] from array b_hoikit_fan
print("Element [3,7] of b_hoikit_fan:", b_hoikit_fan[3,7])

# 5. Give the sum of the row 8 from array c_hoikit_fan
print("Sum of row 8 in c_hoikit_fan:", np.sum(c_hoikit_fan[7,:]))

# 6. Print the elements of the last row for the array b_hoikit_fan and 5th column for the array c_hoikit_fan
print("Last row of b_hoikit_fan:", b_hoikit_fan[-1,:])
print("5th column of c_hoikit_fan:", c_hoikit_fan[:,4])
