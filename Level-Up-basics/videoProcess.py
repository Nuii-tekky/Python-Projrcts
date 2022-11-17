
import cv2,time


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

while True:
  frame= video_obj.read()
  gray_version= cv2.cvtColor(video_obj,cv2.COLOR_BGR2GRAY)
  cv2.imshow('New window',gray_version)
  key= cv2.waitKey(1)
  if key== ord('s'):
    break

  
video_obj.release()
cv2.destroyAllWindows()