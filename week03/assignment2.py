import pandas as pd
import numpy as np
import pprint as pp
import sklearn as skl
import matplotlib.pyplot as plt
from skimage import data, filters, util
from sklearn import datasets
import pprint

#Activity 1: Checkered image. Print the image in the color of your choice.
check = np.zeros((8, 8))
check[::2, 1::2] = 1 
check[1::2, ::2] = 1 
plt.imshow(check, cmap='gray', interpolation='nearest')
plt.show()

#SkLearn Activities:
pprint.pprint(dir(datasets))
# Load different datasets
iris=datasets.load_iris() 

# Display the datasets
print(iris.feature_names)
print(iris.filename)
print(iris.frame)
print(iris.target)
print(iris.target_names)

# Listing all available functions in skimage.data that load images
image_names = [name for name in dir(data) if not name.startswith('_')]
print("Available images in skimage.data:")
print(image_names)

# Display all the available images
for name in image_names:
    image_function = getattr(data, name)
    if callable(image_function):
        try:
            image = image_function()
            plt.imshow(image)
            plt.title(name)
            plt.axis('off')
            plt.show()
        except:
            print(f"{name} is not a displayable image")

# Load the astronaut image
image = data.rocket()

# Print data (This will print the array representation of the image)
print("Data:\n", image)

# Print datatype
print("Datatype:", image.dtype)

# Print shape
print("Shape:", image.shape)

# Plot the image
plt.imshow(image)
plt.title("Original Image")
plt.axis('off')
plt.show()

# Apply gaussian noise
noisy_image = util.random_noise(image, mode='gaussian', var=0.01)

# Plot noisy image
plt.imshow(noisy_image)
plt.title("Image with Gaussian Noise")
plt.axis('off')
plt.show()

# Apply filter with sigma=5
filtered_image = filters.gaussian(noisy_image, sigma=5, channel_axis=-1)

# Plot filtered image
plt.imshow(filtered_image)
plt.title("Filtered Image with Sigma=5")
plt.axis('off')
plt.show()

# Pandas Activities

dates = pd.date_range('20230901', periods=10)

# Create a Series with dates as indices
s = pd.Series(np.random.randn(10), index=dates)

print("Full Series:")
print(s)

# Display values with specific indices (e.g., 3rd and 5th value)
print("\nValues at 3rd and 5th position:")
print(s.iloc[[2, 4]])

# Display values at specific dates (e.g., '20230903' and '20230905')
print("\nValues at '20230903' and '20230905':")
print(s.loc[['2023-09-03', '2023-09-05']])

# Read the .csv file using pandas
df = pd.read_csv('/Users/fanik/development/COMP318/week03/Medals.csv')

# Display the content of the .csv file
print("Content of the .csv file:")
print(df)
