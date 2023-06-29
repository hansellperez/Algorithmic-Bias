#Note: this code does not work very well
# import required libraries
import cv2
import imutils

# Reading the Image
image = cv2.imread("C:\\Users\\shane\\OneDrive\\Desktop\\CECS 174\\pythonProject\\Scripts\\LB CoE all\\Banner_CED_AnnaOrtiz.jpg")
image = imutils.resize(image, width=min(400, image.shape[1]))
# initialize the HOG descriptor
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# detect humans in input image
(humans, _) = hog.detectMultiScale(image, winStride=(4, 10), padding=(4, 4), scale=.5)

# getting no. of human detected
print('Human Detected : ', len(humans))

# loop over all detected humans
for (x, y, w, h) in humans:
   pad_w, pad_h = int(0.15 * w), int(0.01 * h)
   cv2.rectangle(image, (x + pad_w, y + pad_h), (x + w - pad_w, y + h - pad_h), (0, 255, 0), 2)

### Drawing the rectangle regions
##for (x, y, w, h) in humans: 
##   cv2.rectangle(image, (x, y),  
##                  (x + w, y + h),  
##                  (0, 0, 255), 2)
##out = open('C:\\Users\\shane\\OneDrive\\Desktop\\CECS 174\\pythonProject\\Scripts\\Human Detect Output')
###out.write()
##with open(out, "wb") as f:
##   for data in progress.iterable:
##            # write data read to the file
##      f.write(data)
##            # update the progress bar manually
##      progress.update(len(data))
   
# display the output image
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
