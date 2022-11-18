
import cv2


# to capture  1 frame at a time i.e image
# video_obj= cv2.VideoCapture(0)
# check,frame= video_obj.read()

# time.sleep(3)

# cv2.imshow('New window',frame)
# cv2.waitKey(0)
# video_obj.release()
# cv2.destroyAllWindows()

# capture a full video
video_obj= cv2.VideoCapture(0)
a=0

while True:
  a= a+1
  check,frame= video_obj.read()
  cv2.imshow('New window',frame)
  key= cv2.waitKey(1)
  if key== ord('s'):
    break

print(a)  
video_obj.release()
cv2.destroyAllWindows()