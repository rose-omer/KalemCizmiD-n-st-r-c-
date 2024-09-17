import cv2

image_path = "ERKEK.jpg"
image = cv2.imread(image_path)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

inverted_image = 255 - gray_image

blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

inverted_blurred = 255 - blurred

sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

edges = cv2.Canny(gray_image, threshold1=500, threshold2=500)

final_sketch = cv2.bitwise_or(sketch, edges)

cv2.imshow("Original Image", image)
cv2.imshow("Enhanced Sketch Image", final_sketch)

cv2.imwrite("_resim.jpg", final_sketch)

cv2.waitKey(0)
cv2.destroyAllWindows()
