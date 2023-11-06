from skimage import filters, util
import numpy as np
from skimage import data
import matplotlib.pyplot as plt
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
