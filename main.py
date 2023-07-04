import cv2

# Read image
image = cv2.imread("example.png")
print(image)
original_window_name = "Original Image"

# Show original image in a window
cv2.imshow(original_window_name, image)

# Convert image to grayscale
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert_color = cv2.bitwise_not(img_gray)
