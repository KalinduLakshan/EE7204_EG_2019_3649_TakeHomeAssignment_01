import cv2
import numpy as np


# Define the simple_spatial_average function
def simple_spatial_average(image, neighborhood_size):
    # Pad the image to handle the borders of the image
    padded_image = cv2.copyMakeBorder(image, neighborhood_size//2, neighborhood_size//2, neighborhood_size//2, neighborhood_size//2, cv2.BORDER_CONSTANT)

    # Initialize the output image
    output_image = np.zeros_like(image)

    # Apply the spatial averaging for pixels
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            # Extract the current neighborhood
            neighborhood = padded_image[y:y+neighborhood_size, x:x+neighborhood_size]

            # Calculate average and assign it to the output pixel
            output_image[y, x] = np.mean(neighborhood)

    return output_image


# Load the input image
image_path = 'sample.jpg'
input_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if input_image is None:
    print("Sorry: Your given image could not read.")
else:
    cv2.imshow('Original Image', input_image)
    # Perform spatial averaging for 3, 10, 20 neighborhood sizes
    neighborhood_sizes = [3, 10, 20]

    # Loop through different neighborhood sizes
    for size in neighborhood_sizes:
        output_image = simple_spatial_average(input_image, size)

        # Display the result
        cv2.imshow(f'{size}x{size} Neighborhood Image', output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
