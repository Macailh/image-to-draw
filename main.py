import cv2


image = cv2.imread("example.png")
print(image)
original_window_name = "Original Image"

cv2.imshow(original_window_name, image)
