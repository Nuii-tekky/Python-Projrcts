
import cv2

# read image file
image_obj= cv2.imread(r'C:\Users\ekomobong\Documents\My Projects\Python\Python-sandboxes\Level-Up-basics\nature.jpg',0)

# display original image
# cv2.imshow('cool image',image_obj)
# cv2.waitKey(40000)
# cv2.destroyAllWindows()

# some methods
print(image_obj.shape)
print(image_obj.ndim)

# resize image
resized_img_obj= cv2.resize(image_obj,(1366,768))

# Display resized image 
cv2.imshow('Nature Bro',resized_img_obj)
cv2.waitKey(12000)
cv2.destroyAllWindows()

# write resized image to another file

cv2.imwrite('Operatedimage.jpeg',resized_img_obj)




