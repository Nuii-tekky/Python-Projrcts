
import cv2 ,time

status_list= [None,None]
timestamps= []


first_frame= None
video_obj= cv2.VideoCapture(0)
a=0

while True:
  status= 0
  a= a+1
  check,frame= video_obj.read()
  gray_frame= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  blur_gray= cv2.GaussianBlur(gray_frame,(21,21),0)

  if first_frame is None:
    first_frame= blur_gray
    continue

  delta_frame= cv2.absdiff(first_frame,blur_gray)
  tresh_frame= cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
  tresh_frame= cv2.dilate(tresh_frame,None,iterations=2)

# creating contours out of the tresh_frame
  (contours,_)= cv2.findContours(tresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

# drawing rectangles on the current frame with coordinates from the contours
  for contour in contours:
    if cv2.contourArea(contour)< 7000:
      continue
    status= 1
    (x,y,w,h)= cv2.boundingRect(contour)
    cv2.rectangle(frame,(x,y),(x+w,y+h),(63,255,190),2)
  status_list.append(status)


  cv2.imshow('Anoda window ',delta_frame)
  cv2.imshow('yet another window' , tresh_frame)
  cv2.imshow('Brand new window',frame)
  key= cv2.waitKey(1)
  if key== ord('s'):
    break
  print(status_list)

print(a)  
video_obj.release()
cv2.destroyAllWindows()


