import cv2
import numpy as np


# Define the spatial_resolution_reduction
def spatial_resolution_reduction(image, block_size):
    # Get the dimensions of the input image
    height, width = image.shape[:2]

    # Calculate the number of blocks in both dimensions
    num_blocks_x = width // block_size  # Integer value is taken
    num_blocks_y = height // block_size

    # Initialize the output image
    output_res_reduction_image = np.zeros_like(image)

    # Iterate over each block
    for y in range(num_blocks_y):
        for x in range(num_blocks_x):
            # Define the coordinates of the current block
            block_top = y * block_size
            block_bottom = (y + 1) * block_size
            block_left = x * block_size
            block_right = (x + 1) * block_size

            # Extract the current block from the image
            current_block = image[block_top:block_bottom, block_left:block_right]

            # Calculate the average pixel value of the block
            average_value = np.mean(current_block)

            # Assign the average value to all pixels in the current block
            output_res_reduction_image[block_top:block_bottom, block_left:block_right] = average_value

    return output_res_reduction_image


'''
Here I have used grayscale for better understandings because while reading images using OpenCV, some color values 
are manipulated.
Therefore the original color image has converted into a grayscale image for better understanding
'''

# Load the input image
image_name = 'cat.jpg'  # Image path
input_image_read = cv2.imread(image_name)
input_image = cv2.cvtColor(input_image_read, cv2.COLOR_BGR2GRAY)

if input_image is None:
    print("Sorry: Your given image could not read.")
else:
    # Original Image
    cv2.imshow("Original Image", input_image)

    # Perform spatial resolution reduction for different block sizes
    block_sizes = [3, 5, 7]

    for size in block_sizes:
        output_image = spatial_resolution_reduction(input_image, size)

        # Display result
        cv2.imshow(f'{size}x{size} Block Size Image', output_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
