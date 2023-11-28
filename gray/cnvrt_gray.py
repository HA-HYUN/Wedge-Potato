#Convert the image to a black and white photo.
import cv2

def cvgray(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("The image cannot be loaded. Check the route.")
        return
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("Gray", gray)

    cv2.waitKey()
    cv2.destroyAllWindows()