# import the opencv library
import cv2
  
  
# define a video capture object
vid = cv2.VideoCapture(0)
  
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
    
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()







# import cv2   #include opencv library functions in python

# #Create an object to hold reference to camera video capturing
# vidcap = cv2.VideoCapture(0)

# #check if connection with camera is successfully
# if vidcap.isOpened():
#     ret, frame = vidcap.read()  #capture a frame from live video

#     #check whether frame is successfully captured
#     if ret:
#         # continue to display window until 'q' is pressed
#         while(True):
#             cv2.imshow("Frame",frame)   #show captured frame
            
#             #press 'q' to break out of the loop
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break
#     #print error if frame capturing was unsuccessful
#     else:
#         print("Error : Failed to capture frame")

# # print error if the connection with camera is unsuccessful
# else:
#     print("Cannot open camera")