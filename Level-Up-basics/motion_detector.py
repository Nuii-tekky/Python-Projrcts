
import mailbox as mb
import cv2
from datetime import datetime as dt
import pandas

"""
this script has 3 core architectural design
first we wrote the motion detector itself with all the features

secondly we added timestamps to the observed object i.e when the object enters and leaves the camera

thirdly we now pass those collected timestamps to a pandas data frame so that we can do cool things with it like graphs with a library called bokeh
 
although no functions were used in this script it is important to note that several opencv objects have been created accompanied by confusing yet powerful methods and attributes

"""

mailbox_obj= mb.mboxMessage('jumb ship')
print(type(mailbox_obj))
print(mailbox_obj)
# pandas_df= pandas.DataFrame(columns=['Start-Time','End-Time'])
# status_list= [None,None]
# timestamps= []

# first_frame= None
# video_obj= cv2.VideoCapture(0)
# a=0

# while True:
#   status= 0
#   a= a+1
#   check,frame= video_obj.read()
#   gray_frame= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#   blur_gray= cv2.GaussianBlur(gray_frame,(21,21),0)

#   if first_frame is None:
#     first_frame= blur_gray
#     continue

#   delta_frame= cv2.absdiff(first_frame,blur_gray)
#   tresh_frame= cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
#   tresh_frame= cv2.dilate(tresh_frame,None,iterations=2)

# # creating contours out of the tresh_frame
#   (contours,_)= cv2.findContours(tresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

# # drawing rectangles on the current frame with coordinates from the contours
#   for contour in contours:
#     if cv2.contourArea(contour)< 7000:
#       continue
#     status= 1
#     (x,y,w,h)= cv2.boundingRect(contour)
#     cv2.rectangle(frame,(x,y),(x+w,y+h),(63,255,190),2)
#   status_list.append(status)
#   # track the entry object timestamp
#   if status_list[-1]==0 and status_list[-2]==1:
#     timestamps.append(dt.now())
#   if status_list[-1]==1 and status_list[-2]== 0:
#     timestamps.append(dt.now())  

#   cv2.imshow('Delta Frame ',delta_frame)
#   cv2.imshow('Treshold frame' , tresh_frame)
#   cv2.imshow('Original Frame',frame)
#   key= cv2.waitKey(1)
#   if key== ord('s'):
#     if status== 1:
#       timestamps.append(dt.now())
#     break


# # append the timestamps to pandas df
# for timestamp in range(0,len(timestamps),2):
#   pandas_df= pandas_df.append({'Start-Time': timestamps[timestamp],'End-Time': timestamps[timestamp+1]},ignore_index= True)

# pandas_df.to_csv('Timestamp.csv')
# video_obj.release()
# cv2.destroyAllWindows()


