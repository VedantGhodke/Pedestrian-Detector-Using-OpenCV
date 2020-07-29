import cv2
import sys

imagePath = sys.argv[1]
cascPath = "haarcascade_pedestrian.xml"
# cascPath = "pedestrian_another.xml"
# cascPath = "haarcascade_fullbody.xml"

pedsCascade =  cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect pedestrian in pic

peds = pedsCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=9,
        minSize=(30, 30)
)

print("Found {0} pedestrian!".format(len(peds)))

# Draw a rectangle around the peds
for (x, y, w, h) in peds:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# cv2.imshow("Faces found", image)
status = cv2.imwrite('peds_saved.jpg', image)
print ("Image written to file-system : ",status)
