import cv2
import numpy as np

# Load the image
image = cv2.imread('img6.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Use adaptive thresholding to better handle varying lighting conditions
binary = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY_INV, 11, 2)

# Define a kernel for morphological operations
kernel = np.ones((3, 3), np.uint8)

# Perform morphological operations to enhance dots
cleaned = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=1)
cleaned = cv2.morphologyEx(cleaned, cv2.MORPH_CLOSE, kernel, iterations=1)

# Find contours of the dots
contours, _ = cv2.findContours(cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a mask for the dots
dot_mask = np.zeros_like(image)
for contour in contours:
    # Filter contours by area and aspect ratio to ensure they are dots
    area = cv2.contourArea(contour)
    x, y, w, h = cv2.boundingRect(contour)
    aspect_ratio = float(w) / h

    if area < 100 and 0.5 < aspect_ratio < 2:  # Adjust the area and aspect ratio thresholds as needed
        cv2.drawContours(dot_mask, [contour], -1, 255, -1)

# Inpaint the dots using the mask
result = cv2.inpaint(image, dot_mask, inpaintRadius=3.5, flags=cv2.INPAINT_TELEA)

# Show the original image, mask, and result
cv2.imshow("Binary Image", binary)
cv2.imshow("Cleaned Image", cleaned)
cv2.imshow("Original Image", image)
cv2.imshow("Dot Mask", dot_mask)
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the result if needed
cv2.imwrite("result_image.jpg", result)
