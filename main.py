import cv2  # image loading and displaying
import pandas as pd  # quick calculation
import argparse  # taking arguments

# Creating argument parser to take image path from command line
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args["image"]

# Reading the image with opencv
img = cv2.imread(img_path)
height, width, _ = img.shape

# square root of sums of squares of the sides is the actual max 
#  (Pythagoras Theorem) but that requires importing the math module
max_distance = height * width

print("Press Esc to exit the program!  :)")

# declaring global variables (are used later on)
clicked = False
r = g = b = xpos = ypos = 0

# Reading csv file with pandas and giving names to each column
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv("colors.csv", names=index, header=None)


# function to calculate minimum distance from all colors and get the most matching color
def getColorName(R, G, B):
    minimum = max_distance
    for i in range(len(csv)):
        d = (
            abs(R - int(csv.loc[i, "R"]))
            + abs(G - int(csv.loc[i, "G"]))
            + abs(B - int(csv.loc[i, "B"]))
        )
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname


# function to get x,y coordinates of mouse double click
def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global b, g, r, xpos, ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

# driver code
cv2.namedWindow("Photo")
cv2.setMouseCallback("Photo", draw_function)

while True:
    cv2.imshow("Photo", img)
    if clicked:
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)
        colorName = getColorName(r, g, b) + " R=" + str(r) + " G=" + str(g) + " B=" + str(b)
        cv2.putText(img, colorName, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        if r + g + b >= 600:
            cv2.putText(img, colorName, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        clicked = False

    # Exit Program if esc key is pressed
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
