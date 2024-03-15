import cv2

# Loading the image file
input_file_name = 'cat.jpg'
input_image = cv2.imread(input_file_name)


# Check whether the input image can be read or not
if input_image is None:
    print("Sorry: Your given image could not read.")
else:
    # Original Image
    cv2.imshow("Original Image", input_image)

    # Rotate the image by 90 degrees clockwise
    output_90_img = cv2.rotate(input_image, cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow("Image rotated by 90 clockwise", output_90_img)

    # Rotate the image by 90 degrees counterclockwise or 270 clockwise
    output_counter90_img = cv2.rotate(input_image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imshow("Image rotated by 90 counterclockwise", output_counter90_img)

    '''
    45 degrees rotation(arbitrary rotation) cannot be performed using cv2.rotate() method.
    Here we need to perform the general rotation by giving the angle and the scale factor.
    Need to create a rotation matrix using cv2.getRotationMatrix2D() and apply it to image with cv2.warpAffine()
    '''

    # Rotate the image by 45 degrees clockwise
    (height, width, channel) = input_image.shape
    center = (width/2, height/2)

    clockwise_angle = 45
    scale = 1.0

    img_clockwise_matrix = cv2.getRotationMatrix2D(center, clockwise_angle, scale)
    output_45_img = cv2.warpAffine(input_image, img_clockwise_matrix, (width, height))
    cv2.imshow("Image rotated by 45 clockwise", output_45_img)

    # Rotate the image by 45 degrees clockwise
    counterclockwise_angle = -45

    img_counterclockwise_matrix = cv2.getRotationMatrix2D(center, counterclockwise_angle, scale)
    output_counter_45_img = cv2.warpAffine(input_image, img_counterclockwise_matrix, (width, height))
    cv2.imshow("Image rotated by 45 counterclockwise", output_counter_45_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
