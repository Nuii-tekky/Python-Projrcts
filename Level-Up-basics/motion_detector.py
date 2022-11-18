
import cv2 ,time

first_frame= None
video_obj= cv2.VideoCapture(0)
a=0

while True:
  a= a+1
  check,frame= video_obj.read()
  gray_frame= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  blur_gray= cv2.GaussianBlur(gray_frame,(21,21),0)

  if first_frame is None:
    first_frame= blur_gray
    continue

  delta_frame= cv2.absdiff(first_frame,blur_gray)
  tresh_frame= cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
  tresh_frame= cv2.dilate(tresh_frame,None,iterations=1)

  (contours,_)= cv2.findContours(tresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

  for contour in contours:
    if cv2.contourArea(contour)> 1000:
      continue
    (x,y,w,h)= cv2.boundingRect(contour)
    cv2.rectangle(frame,(x,y),(x+w,y+h),(63,255,190),2)


  cv2.imshow('Anoda window ',delta_frame)
  cv2.imshow('yet another window' , tresh_frame)
  cv2.imshow('Brand new window',frame)
  key= cv2.waitKey(1)
  if key== ord('s'):
    break

print(a)  
video_obj.release()
cv2.destroyAllWindows()


