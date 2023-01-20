# Drone-Landing-Computer-Vision
Using OpenCV and python, we created an algorithm that can detect bright red triangles as well as differentiate between a light that is on and stagnant compared to one that is blinking all within a video feed.

This project is the initial computer vision algorithms we created to test for proof of concept. 
The wider scope of this project is we hope to create our own landing sequence for a drone that is part of a larger Senior Project. 
Ideally the drone will be able to detect some kind of pattern on a landing doc/station and then re-orientate itself using the indicators detected.

In this code, the bright red triangle is the first indicator.
Differentiating between blinking lights and stagnant lights is important as well and is the second indicator. 
We wanted to use a combination of flashing/blinking lights/LED's and triangle detection as the catalyst for the drone landing sequence being triggered.
This is similar to how a Helicopter landing padoperates, with a Large H in the middle surrounded by blinking LED's.
Thus both of these components had to be detected by computer vision. 

Here is a Youtube video where my partner and I explain how the algorithm works with an example of what the code does:

Triangle Detection Example Time Stamp: https://youtu.be/kZtDb5XoRM8?t=110

Blinking Light Detection/Differentiation Example Time Stamp : https://youtu.be/kZtDb5XoRM8?t=377 

Whole Video link: https://www.youtube.com/watch?v=kZtDb5XoRM8&t=10s&ab_channel=ChristopherCiobanu
