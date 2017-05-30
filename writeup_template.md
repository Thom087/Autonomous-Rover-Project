## Project: Search and Sample Return
---

**The goals / steps of this project are the following:**  

**Training / Calibration**  

* Download the simulator and take data in "Training Mode"
* Test out the functions in the Jupyter Notebook provided
* Add functions to detect obstacles and samples of interest (golden rocks)
* Fill in the `process_image()` function with the appropriate image processing steps (perspective transform, color threshold etc.) to get from raw images to a map.  The `output_image` you create in this step should demonstrate that your mapping pipeline works.
* Use `moviepy` to process the images in your saved dataset with the `process_image()` function.  Include the video you produce as part of your submission.

**Autonomous Navigation / Mapping**

* Fill in the `perception_step()` function within the `perception.py` script with the appropriate image processing functions to create a map and update `Rover()` data (similar to what you did with `process_image()` in the notebook). 
* Fill in the `decision_step()` function within the `decision.py` script with conditional statements that take into consideration the outputs of the `perception_step()` in deciding how to issue throttle, brake and steering commands. 
* Iterate on your perception and decision function until your rover does a reasonable (need to define metric) job of navigating and mapping.  

[//]: # (Image References)

[image1]: ./misc/rover_image.jpg
[image2]: ./calibration_images/example_grid1.jpg
[image3]: ./calibration_images/example_rock1.jpg 
[image4]: ./calibration_images/rock_sample.jpg 
[image5]: ./misc/obstacle_sample.jpg 
[image6]: ./misc/image_process3.jpg 



## [Rubric](https://review.udacity.com/#!/rubrics/916/view) Points
### Here I will consider the rubric points individually and describe how I addressed each point in my implementation.  

---
### Writeup / README

#### 1. Provide a Writeup / README that includes all the rubric points and how you addressed each one.  You can submit your writeup as markdown or pdf.  

You're reading it!

### Notebook Analysis
#### 1. Run the functions provided in the notebook on test images (first with the test data provided, next on data you have recorded). Add/modify functions to allow for color selection of obstacles and rock samples.

I made 2 new functions, one for obstacles and one for rock samples:

![alt text][image4]

Where I choosed a RGB of (140, 110, 0) to (200, 180, 100) to find this out, I took some bright images and analysed the RGB as well as for a dark rock sample image.
In the image you can see the rock sample in the perspective view as well as thresholded.

For obstacles I mainly did the inverse of the color_thresh:

![alt text][image5]
I just checked if all the RGB's are less or equal than 160 which results than in a list of booleans.

#### 2. Populate the `process_image()` function with the appropriate analysis steps to map pixels identifying navigable terrain, obstacles and rock samples into a worldmap.  Run `process_image()` on your test data using the `moviepy` functions provided to create video output of your result. 

* Apply all the threshold function to the warped picture (rock, obstacle and navigable terrain)
* Convert them to rover centric coordinates, therefore I applied just the rover_coords function to the thresed list what gave 
  me the x and y coordinates of the rover centric view 
* Convert to world coordinates, use the pix_to_world function with the rotation and translation to the expected robot position / yaw
  I did this also for all three function (rock, obstacles and navigable terrain)
  
![alt text][image6]

* The worldmap is then created also for all this three functions with the obstacles on the red layer (255,0,0), the rocks on the green layer and the navigable terrain on the blue layer. The more images it had of the same location to more the color was added, which can be figured out in the video.
* To show the image on the right side I just multiplied it with 255 to see the full color


### Autonomous Navigation and Mapping

#### 1. Fill in the `perception_step()` (at the bottom of the `perception.py` script) and `decision_step()` (in `decision.py`) functions in the autonomous mapping scripts and an explanation is provided in the writeup of how and why these functions were modified as they were.
* I used the function I tested in the notebook. Therefore I defined again the same functions: color_thresh, obstacle_thresh, and rock_thresh. The rotate and the translate functions I also had to modify, because they were empty.
##### For the perception_step() 
* I began with the some variables including the calibration of source to destination
* Next I applied the perspective transform
* Then the three color threshold functions (obstacle, rock and navigable terrain)
* After that the Rover image was constructed with the treshhold variables where I had to multiply those with 255 to see the full colors (red, green and blue).
* Then the thresholded values are converted to rovercentric pix's with the rover_coords function
* In a next step the world coordinates werde calculated with the rover position and the rover yaw
* Then the world map is again updated with those values.
* Next the polar coordinates were calculated out of the function to_polar_coords of the navigable x / y pixesl.
* Finally the rover distance and angles were updated

#### 2. Launching in autonomous mode your rover can navigate and map autonomously.  Explain your results and how you might improve them in your writeup.
The rover could find out 90% of the rocks. So I had after 40% of mapping at least one rock, sometimes even 4 depending where they lie. The fidelity was between 60% and 70%.
To organize the code better I wrote some function of forward motion, steering, stopping and turning. I neglected to make the dicision out of the rover mode instead I used the velocity of the rover.
##### Possible improvement
* To get all rocks the threshold should be more imporved, I should make more images of rocks in different location to analyse the RGB
* To get more fidelity the threshold of navigable terrain, as well as the calibration should maybe rechecked
* Sometimes the robot turned just in a circle, where I analysed that I should take the distorted view of the robot when it fully steers +-15°, therefore I just subtracted the steering angle divided by 3 from the avg_nav_angle. After this improvement the robot did not went again in a circle
* Sometimes the robot got stucked in some rocks, I tried to solve this with some checking of the velo of 0 with some time but unfortunately without success.. I could not store the old velo somewhere and then compare it after a perpendicular time with the actual velo to make a steering.. 

![alt text][image3]

**Note: running the simulator with different choices of resolution and graphics quality may produce different results, particularly on different machines!  Make a note of your simulator settings (resolution and graphics quality set on launch) and frames per second (FPS output to terminal by `drive_rover.py`) in your writeup when you submit the project so your reviewer can reproduce your results.**







