import cv2

def detect_text_regions(input_image_path, output_image_path):
    # Read the image
    image = cv2.imread(input_image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Image Thresholding (for emphasizing text regions)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Find contours (detect text regions)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw rectangles around detected contours
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw rectangles around the contours

    # Display the image with contours
    cv2.imshow('Contours', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the resulting image with contours
    cv2.imwrite(output_image_path, image)

    return image  # Return the image with drawn contours (optional)

input_path = 'opencvtest.png'  # Input image file
output_path = 'result_with_contours.png'  # Output file to save the result
result_image = detect_text_regions(input_path, output_path)
