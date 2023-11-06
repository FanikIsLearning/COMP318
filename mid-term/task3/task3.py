from skimage import data
import matplotlib.pyplot as plt
from skimage import filters

# Load coffee data
coffee_hoikit_fan = data.coffee()

# Print coffee data and its attributes
print(coffee_hoikit_fan)
print("Data type:", coffee_hoikit_fan.dtype)
print("Data shape:", coffee_hoikit_fan.shape)

# Display and save the original coffee image
plt.imshow(coffee_hoikit_fan)
plt.axis('off')  # To hide axis values
plt.savefig('Figure1_hoikit_fan.png', bbox_inches='tight', pad_inches=0)
plt.show()

# Apply Gaussian filter with std 5 to blur the image
blurred_image = filters.gaussian(coffee_hoikit_fan, sigma=5)

# Display and save the blurred image
plt.imshow(blurred_image)
plt.axis('off')
plt.savefig('filtered_Figure_coffee_hoikit_fan.png', bbox_inches='tight', pad_inches=0)
plt.show()
