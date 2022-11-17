
import cv2

cascade_obj= cv2.CascadeClassifier(r'C:\Users\ekomobong\Documents\My Projects\Python\Python-sandboxes\Level-Up-basics\haarcascade_frontalface_default.xml')

image_obj= cv2.imread(r'C:\Users\ekomobong\Documents\My Projects\Python\Python-sandboxes\Level-Up-basics\news.jpg')

gray_scale_version= cv2.cvtColor(image_obj,cv2.COLOR_BGR2GRAY)

faces=cascade_obj.detectMultiScale(gray_scale_version,
scaleFactor= 1.1,
minNeighbors= 5
)

for x,y,w,h in faces:
  image_obj= cv2.rectangle(image_obj,(x,y),(x+w,y+h),(34,103,150),2)

# print(type(faces))
# print(faces)


cv2.imshow('jndkc',image_obj)
cv2.waitKey(0)
cv2.destroyAllWindows()
