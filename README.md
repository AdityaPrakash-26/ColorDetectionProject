# ColorDetectionProject

Greetings!

This is a CLI project made with Python, OpenCV, Pandas and <3

To run the project, you need to write the following command:

  `python3 main.py -i <PATH_TO_IMAGE>`
  
After that, clicking anywhere on the image you provided shall return the name of the color, and the RGB values. Press escape to exit

Dependencies

• Python

• OpenCV

• Numpy

• Pandas

#How it works?

The program listens for a click, and then calculates the shortest distance of the selected pixel from the provided color list in `colors.csv`. It returns the closest match and displays the same in a rectangle at the top of the image.
