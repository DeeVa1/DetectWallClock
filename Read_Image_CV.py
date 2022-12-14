import cv2
from matplotlib import pyplot as plt

# Opening image
img = cv2.imread("OIP1.jpg")



stop_data = cv2.CascadeClassifier('haarcascade_wallclock.xml')

#We will use the detectMultiScale() function of OpenCV to recognize
#big wall clocks as well as small ones:

# Use minSize because for not
# bothering with extra-small
# dots that would look like wall clocks

found = stop_data.detectMultiScale(img,minSize =(20, 20))

# Don't do anything if there's
# no wall clock
amount_found = len(found)

if amount_found != 0:
	
	# There may be more than one
	# wall clock in the image
	for (x, y, width, height) in found:
		
		# We draw a green rectangle around
		# every recognized sign
		cv2.rectangle(img, (x, y),  (x + height, y + width),
					(0, 255, 0), 5)
	
# Creates the environment of
# the picture and shows it
plt.subplot(1, 1, 1)
plt.imshow(img)
plt.show()


