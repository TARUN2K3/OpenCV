# Import necessary libraries
import cv2
import numpy as np

# Define function to select region of interest (ROI) and draw lines on the image
def region_of_interest(image, vertices):
    mask = np.zeros_like(image)
    match_mask_color = 255   
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

def draw_lines(image, lines):
    image = np.copy(image)
    line_image = np.zeros_like(image)

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 255), 5)

    image_with_lines = cv2.addWeighted(image, 0.8, line_image, 1, 0.0)
    return image_with_lines

# Define function to process each frame of the video
def process(img):
    # Print shape of the input frame
    print(img.shape)
    # Get height and width of the frame
    height = img.shape[0]
    width = img.shape[1]
    # Define region of interest (ROI) vertices
    region_of_interest_vertices = [
        (0, height),
        (width / 2, height / 2),
        (width, height)
    ]

    # Convert frame to grayscale
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply Canny edge detection
    canny_image = cv2.Canny(gray_image, 50, 150)
    # Detect lines using Hough Transform
    lines = cv2.HoughLinesP(canny_image, 1, np.pi / 180, 150, maxLineGap=10, minLineLength=100)
    # Crop detected lines within the region of interest (ROI)
    cropped_image = region_of_interest(canny_image, np.array([region_of_interest_vertices], np.int32))
    # Draw lines on the original frame
    image_with_lines = draw_lines(img, lines)
    
    # Resize the processed frame for display
    resized_frame = cv2.resize(image_with_lines, (800, 400))
    return resized_frame

# Open the video file
cap = cv2.VideoCapture('road.mp4')
# Loop through each frame of the video
while (cap.isOpened()):
    # Read the frame
    ret, frame = cap.read()
    # Check if the frame is successfully read
    if not ret:
        break
    
    # Process the frame
    processed_frame = process(frame)
    # Display the processed frame
    cv2.imshow('frame', processed_frame)
    
    # Check for user input to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Release video capture object and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
