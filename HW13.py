import numpy as np

def convolve2D(image, kernel):
    """
    Perform a 2D convolution operation without padding and without striding.
    Assuming kernel is a 3x3 matrix.
    """
    # Dimensions of the image
    image_height, image_width = image.shape
    
    # Dimensions of the kernel
    kernel_height, kernel_width = kernel.shape
    
    # Calculate the shape of the output matrix
    output_height = image_height - kernel_height + 1
    output_width = image_width - kernel_width + 1
    
    # Initialize the output matrix with zeros
    output = np.zeros((output_height, output_width))
    
    # Perform convolution (without padding and striding)
    for i in range(output_height):
        for j in range(output_width):
            # Element-wise multiplication of the kernel and the image patch
            output[i, j] = np.sum(image[i:i+kernel_height, j:j+kernel_width] * kernel)
    
    return output

# Define a 6x6 image
image = np.array([
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36]
])

# Define a 3x3 filter (kernel)
kernel = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])

# Perform convolution
convolved_image = convolve2D(image, kernel)
convolved_image
