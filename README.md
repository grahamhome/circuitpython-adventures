# CircuitPython Lessons
A collection of programming lessons designed to teach CircuitPython programming on the MakerPi RP2040 and some basic hardware components. Intended for use at the It Begins In Brockport makerspace.

## Lesson Structure
Each lesson is divided into 4 parts. Each part builds upon the previous part to build up the code incrementally and introduce new concepts one at a time.

## Lessons

### People Counter
A digital door chime which counts visitors to a shop using an ultrasonic sensor. Parts 1 and 2 assume the shop has separate entry and exit doors for simplicity, while parts 3 and 4 assume a single door and introduce the use of a Boolean variable to track whether or not the sensor is recording an entry or an exit event. A reset button is introduced to reset the visitor count at the end of each day.

### Light Entertainment
A simple game using a NeoPixel strip with 8 LEDs. The goal is to get the blue light to stop in the red lighted area by pushing a button at the right time. The speed of the blue light increases with each level while the size of the red lighted area decreases.

### Your Biggest Fan
Pushbuttons are used to control the speed and direction of a DC motor with attached fan blades. The final part of this exercise adds a servo motor whose position is updated to indicate the current fan speed. Driving a servo and a DC motor simultaneously requires an external power supply as the USB power is not sufficient. 