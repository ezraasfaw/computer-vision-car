# Computer Vision Car Project

This project is about creating a car that follows the directions of the car in front by tracking its red back light. The project is part of a Mechatronics course and is developed by Ezra-Fikru Asfaw.

## Project Overview

The project uses a sensor to capture images and track the red back light of the car in front. The car's movements are controlled by two motors, which are managed based on the position of the red light in the captured images.

## Code Structure

The code is structured as follows:

- **Importing necessary modules**: The necessary modules such as sensor, image, time, and Motor from tb6612 are imported.
- **Motor Initialization**: Two motors are initialized using the Motor class from tb6612.
- **Variable Initialization**: Variables for storing the x and y coordinates of the red light in two different regions of interest (ROIs) are initialized.
- **Color Thresholds**: Thresholds for color tracking are set. Currently, only the thresholds for red color are set.
- **Main Loop**: In the main loop, the sensor captures images and finds blobs of the red color in the two ROIs. Depending on the positions of the blobs, the speeds of the two motors are adjusted to control the car's movements.

## Running the Code

To run the code, simply execute the `car.py` script. Make sure that the necessary modules are installed and the hardware (sensor and motors) are properly set up.

## Future Work

This is a basic implementation and there's room for improvement. Future work may include improving the color tracking mechanism, refining the motor control logic, and adding more features like obstacle avoidance.

Please note that this is a student project and is meant for educational purposes. Use it at your own risk. Contributions and suggestions are welcome! 

## Contact

For any queries or suggestions, please contact Ezra-Fikru Asfaw. 

Happy Coding! 🚗💨
