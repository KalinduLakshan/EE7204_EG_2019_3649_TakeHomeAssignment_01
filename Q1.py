import cv2
import numpy as np


# Define the reduce_intensity_levels function
def reduce_intensity_levels(image, q_levels):
    # Calculate the scaling factor
    scale = 255 / (q_levels - 1)

    # Quantize pixel values
    quantized_image = np.round(image / scale) * scale

    # Convert to uint8
    quantized_image = quantized_image.astype(np.uint8)

    return quantized_image


# Loading the image file, assigned the image file name to a variable for a gray scale or color image input
# identification
image_path = 'sample.jpg'

isGray = int(input("Do you need to convert the original image into a gray scale image (Put 1='yes', 0='no'): "))

if isGray:
    input_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check whether the image can be read or not
    if input_image is None:
        print("Sorry: Your given image could not read.")
    else:
        # Enter the number of intensity levels as a power of 2
        Q_levels = int(input("Enter the number of intensity levels (power of 2): "))

        # Check whether the number of intensity levels is a power of 2 or not
        if Q_levels & (Q_levels - 1) != 0:
            print("Error: Number of intensity levels must be a power of 2.")
        else:
            # Reduce the intensity levels by changing the quantization levels
            output_image = reduce_intensity_levels(input_image, Q_levels)

            # Display the original and quantized images
            cv2.imshow('Original Image', input_image)
            cv2.imshow(f'{Q_levels} Levels Reduced Intensity Image', output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    input_image = cv2.imread(image_path)

    # Check whether the input image can be read or not
    if input_image is None:
        print("Sorry: Your given image could not read.")
    else:

        # Enter the number of intensity levels as a power of 2
        Q_levels = int(input("Enter the number of intensity levels (power of 2): "))

        # Check whether the number of intensity levels is a power of 2 or not
        if Q_levels & (Q_levels - 1) != 0:
            print("Error: Number of intensity levels must be a power of 2.")
        else:
            # Reduce the intensity levels by changing the quantization levels
            output_image = reduce_intensity_levels(input_image, Q_levels)

            # Display the original and quantized images
            cv2.imshow('Original Image', input_image)
            cv2.imshow(f'{Q_levels} Levels Reduced Intensity Image', output_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
